from __future__ import annotations

from typing import TYPE_CHECKING
from pathlib import Path

from lxml import html

from gdtch.exceptions import WrongFilePathToHTML

from gdtch.mixins.remove_junk_tags import RemoveJunkTags
from gdtch.mixins.remove_top_of_document import RemoveTopOfDocument
from gdtch.mixins.clean_attributes import CleanAttributes
from gdtch.mixins.clean_text import CleanText
from gdtch.mixins.alter_text import AlterText
from gdtch.mixins.multiline_transform import MultiLineTransformations
from gdtch.mixins.add_elements import AddElements
from gdtch.mixins.add_attributes import AddAttributes

if TYPE_CHECKING:
    from lxml.html import HtmlElement


class Cleaner(
    RemoveJunkTags,
    RemoveTopOfDocument,
    CleanAttributes,
    AlterText,
    CleanText,
    MultiLineTransformations,
    AddElements,
    AddAttributes
):

    def __init__(self, file_path: str):
        self.elements = self.get_elements(file_path)
        
    @staticmethod
    def get_elements(file_path: str) -> list[HtmlElement]:
        if not Path(file_path).exists() or Path(file_path).suffix != '.html':
            raise WrongFilePathToHTML()

        with open(file_path, mode='r', encoding='utf-8') as file:
            root = html.parse(file).getroot()
        return list(root.body.iterchildren())

    def pretty_save(self, file_path: str = '.') -> None:
        indent = 0

        with open(f'{file_path}/cleaned_html.html', mode='w', encoding='utf-8') as file:
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
                        formatted_item = f"{' ' * 4 * indent}{self._get_line(item)}\n"

                file.write(formatted_item)
    
    @staticmethod
    def _get_line(element: HtmlElement, **kwargs) -> str:
        return html.tostring(element, method='html', encoding='utf-8', **kwargs).decode('utf-8')
                    