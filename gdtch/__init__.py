from __future__ import annotations

from typing import TYPE_CHECKING
from pathlib import Path
import logging
import io

from lxml import html
import cssutils

from gdtch.exceptions import WrongFilePathToHTML

from gdtch.mixins.remove_junk_tags import RemoveJunkTags
from gdtch.mixins.remove_top_of_document import RemoveTopOfDocument
from gdtch.mixins.clean_attributes import CleanAttributes
from gdtch.mixins.clean_text import CleanText
from gdtch.mixins.alter_text import AlterText
from gdtch.mixins.multiline_transform import MultiLineTransformations
from gdtch.mixins.add_elements import AddElements
from gdtch.mixins.add_attributes import AddAttributes
from gdtch.mixins.alter_attributes import AlterAttributes

if TYPE_CHECKING:
    from lxml.html import HtmlElement
    from cssutils.css import CSSStyleRule


class Cleaner(
    RemoveJunkTags,
    RemoveTopOfDocument,
    CleanAttributes,
    AlterText,
    CleanText,
    MultiLineTransformations,
    AddElements,
    AddAttributes,
    AlterAttributes
):

    def __init__(self, file_path: str, *args, **kwargs):
        self.html_file_path = file_path
        self.elements, self.styles = self.get_elements(file_path)

        super().__init__(*args, **kwargs)

    @staticmethod
    def get_elements(file_path: str) -> tuple[list[HtmlElement], list[CSSStyleRule]]:
        if not Path(file_path).exists() or Path(file_path).suffix != '.html':
            raise WrongFilePathToHTML()

        with open(file_path, mode='r', encoding='utf-8') as file:
            root = html.parse(file).getroot()

        style = root.find('./head/style').text

        cssutils.log.setLevel(logging.CRITICAL)
        return list(root.body.iterchildren()), list(cssutils.CSSParser().parseString(style))

    def pretty_save(self, file_path: str | None = None) -> str | None:
        buffer = self._pretty_save()
        buffer.seek(0)

        if file_path:
            with open(file_path, mode='w', encoding='utf-8') as file:
                file.write(buffer.read())
                buffer.close()
        else:
            content = buffer.getvalue()
            buffer.close()
            return content

    def _pretty_save(self) -> io.StringIO:
        indent = 0
        file = io.StringIO()

        for item in self.elements:
            match item.tag:
                case _ if item.tag.startswith('h') and item.tag[-1].isnumeric():
                    indent = int(item.tag[-1])
                    formatted_item = f"\n{' ' * 4 * (indent - 1)}{self._get_line(item)}\n\n"

                case 'pre':
                    formatted_item = f"\n{' ' * 4 * indent}{self._get_line(item)}\n\n"

                case 'br':
                    formatted_item = f"\n{' ' * 4 * indent}{self._get_line(item)}\n"

                case 'img':
                    formatted_item = f"{' ' * 4 * indent}{self._get_line(item)}\n\n"

                case 'ul' | 'ol':
                    line = self._get_line(item, pretty_print=True)

                    lines = line.splitlines()
                    for i in range(1, len(lines) - 1):
                        lines[i] = ' ' * 4 * indent + ' '  *  4 + lines[i]

                    lines[-1] = ' ' * 4 * indent +  lines[-1]

                    formatted_line = '\n'.join(lines)
                    formatted_item = f"\n{' ' * 4 * indent}{formatted_line}\n\n"

                case _:
                    formatted_item = f"{' ' * 4 * indent}{self._get_line(item).replace('\u00A0', ' ')}\n"

            file.write(formatted_item)

        return file

    @staticmethod
    def _get_line(element: HtmlElement, **kwargs) -> str:
        return html.tostring(element, method='html', encoding='utf-8', **kwargs).decode('utf-8')

