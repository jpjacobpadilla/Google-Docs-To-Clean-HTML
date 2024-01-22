from __future__ import annotations
from typing import TYPE_CHECKING

from lxml import html

from gdtch.mixins.remove_extra_tags import RemoveExtraTags
from gdtch.mixins.remove_top_of_document import RemoveTopOfDocument

if TYPE_CHECKING:
    from lxml.html import HtmlElement


class Cleaner(
    RemoveExtraTags,
    RemoveTopOfDocument
):

    def __init__(self, file_path: str):
        self.root = self.create_tree(file_path)

    @staticmethod
    def create_tree(file_path: str) -> HtmlElement:
        with open(file_path, mode='r', encoding='utf-8') as file:
            root = html.parse(file).getroot()
        
        root.find('./head/style').drop_tree()
        return root

    def pretty_save(self, file_path: str = '.') -> None:
        html_string = html.tostring(self.root, pretty_print=True, method='html', encoding='utf-8').decode('utf-8')

        with open(f'{file_path}/cleaned_html.html', mode='w', encoding='utf-8') as file:
            file.write(html_string)
