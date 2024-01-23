from __future__ import annotations

from typing import TYPE_CHECKING
import re

from lxml import html

from gdtch.mixins.remove_junk_tags import RemoveJunkTags
from gdtch.mixins.remove_top_of_document import RemoveTopOfDocument
from gdtch.mixins.clean_attributes import CleanAttributes
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
    MultiLineTransformations,
    AddElements,
    AddAttributes
):

    def __init__(self, file_path: str):
        self.elements = self.get_elements(file_path)

    @staticmethod
    def get_elements(file_path: str) -> list[HtmlElement]:
        with open(file_path, mode='r', encoding='utf-8') as file:
            root = html.parse(file).getroot()
        return list(root.body.iterchildren())

    def pretty_save(self, file_path: str = '.') -> None:
        indent = 0

        with open(f'{file_path}/cleaned_html.html', mode='w', encoding='utf-8') as file:
            for item in self.elements:
                if re.match(r'h[1-6]$', item.tag): 
                    indent = int(item.tag[-1]) - 1
                    file.write(f"\n{' ' * 4 * indent}{html.tostring(item, method='html', encoding='utf-8').decode('utf-8')}\n\n")
                    indent = int(item.tag[-1]) 

                elif item.tag == 'pre':
                    file.write(f"\n\n{html.tostring(item, method='html', encoding='utf-8').decode('utf-8')}\n\n\n")

                else:
                    file.write(f"{' ' * 4 * indent}{html.tostring(item, method='html', encoding='utf-8').decode('utf-8')}\n")