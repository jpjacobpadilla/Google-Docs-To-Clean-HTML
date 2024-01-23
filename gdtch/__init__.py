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
            # for item in self.elements:
            #     if re.match(r'h[1-6]$', item.tag): 
            #         indent = int(item.tag[-1]) - 1

            #         file.write('\n')
            #         file.write(' ' * 4 * indent + html.tostring(item, method='html', encoding='utf-8').decode('utf-8') + '\n')
            #         file.write('\n')

            #         indent = int(item.tag[-1]) 

            #     elif item.tag == 'pre':
            #         file.write('\n\n')
            #         file.write(' ' * 4 * indent + html.tostring(item, method='html', encoding='utf-8').decode('utf-8') + '\n')
            #         file.write('\n\n')

            #     else:
            #         file.write(' ' * 4 * indent + html.tostring(item, method='html', encoding='utf-8').decode('utf-8') + '\n')
            for item in self.elements:
                if re.match(r'h[1-6]$', item.tag): 
                    indent = int(item.tag[-1]) - 1

                    file.write('\n')
                    file.write(' ' * 4 * indent + html.tostring(item, method='html', encoding='utf-8').decode('utf-8') + '\n')
                    file.write('\n')

                    indent = int(item.tag[-1]) 

                elif item.tag == 'pre':
                    # Find the <code> element within the <pre> element
                    code_element = item.find('.//code')

                    # Split the text into lines
                    lines = code_element.text_content().split('\n')
                    code_element.clear()  # Clear existing text in <code>

                    for line in lines:
                        # Create an <i> element for each line
                        i_element = html.Element('i')
                        i_element.text = line

                        # Append the <i> element to the <code> element
                        code_element.append(i_element)

                        # Add a line break (using tail) for formatting
                        br_element = html.Element('br')
                        code_element.append(br_element)
                        br_element.tail = '\n' + ' ' * 4 * indent

                    # Convert back to a string
                    updated_html_content = html.tostring(item, encoding='utf-8').decode('utf-8')

                    file.write('\n')
                    file.write('\n')
                    file.write(' ' * 4 * indent + updated_html_content)
                    file.write('\n')
                    file.write('\n')

                else:
                    file.write(' ' * 4 * indent + html.tostring(item, method='html', encoding='utf-8').decode('utf-8') + '\n')