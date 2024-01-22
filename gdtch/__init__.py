from __future__ import annotations
from typing import TYPE_CHECKING

from lxml import html
import re

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
        indent = 0

        with open(f'{file_path}/cleaned_html.html', mode='w', encoding='utf-8') as file:
            for item in self.root.iterfind('./body/*'):
                if re.match(r'h[1-6]$', item.tag): 
                    indent = int(item.tag[-1]) - 1

                    file.write('\n')
                    file.write(' ' * 4 * indent + html.tostring(item, method='html', encoding='utf-8').decode('utf-8') + '\n')
                    file.write('\n')

                    indent = int(item.tag[-1]) 

                else:
                    file.write(' ' * 4 * indent + html.tostring(item, method='html', encoding='utf-8').decode('utf-8') + '\n')
