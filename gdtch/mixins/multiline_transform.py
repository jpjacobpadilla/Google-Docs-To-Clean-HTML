import re
import itertools
from lxml import html

from gdtch.exceptions import NoImageMetadata


class MultiLineTransformations:
    def insert_highlightjs_code_blocks(self) -> None:
        i = 0

        while i < len(self.elements):
            if (text := self.elements[i].text) and re.match(r'```[a-zA-Z]+$', text):
                lang = self.elements[i].text.removeprefix('```').lower()
                self.elements.pop(i)

                code = ''
                while self.elements[i].text is None or not re.match(r'```$', self.elements[i].text):
                    code += f'{"" if not (text := self.elements[i].text) else text}\n'
                    self.elements.pop(i)

                self.elements.pop(i)

                pre_element = html.Element("pre")
                code_element = html.Element("code")

                code_element.text = code.removesuffix('\n')
                code_element.attrib['class'] = f'language-{lang} hljs'
                pre_element.append(code_element)
                self.elements.insert(i, pre_element)

            i += 1

    def make_code_block_quotes_straight(self) -> None:
        for element in self.elements:
            if element.tag == 'pre':
                code_element = element.find('./code')
                code = code_element.text 

                # Change all curly quotes to straight quotes for code
                code = code.replace('“', '"')
                code = code.replace('”', '"')
                code = code.replace('‘', "'")
                code = code.replace('’', "'")

                code_element.text = code

    def alter_image_attributes(self, path_template: str = '{}') -> None:
        i = 0

        while i < len(self.elements):
            if self.elements[i].tag == 'img':
                meta_data = self.elements[i - 1].text
                if not meta_data: raise NoImageMetadata()

                pairs = self.make_pairs(meta_data)
                for key, val in itertools.batched(pairs, 2):
                    formatted_key = key.strip('"”” ')
                    formatted_val = val.strip('"”” ')
                    self.elements[i].attrib[formatted_key] = formatted_val
                
                original_src = self.elements[i].attrib['src']
                self.elements[i].attrib['src'] = path_template.format(original=original_src)

                self.elements.pop(i - 1)
                i -= 1

            i += 1

    @staticmethod
    def make_pairs(meta_data: str) -> list[str]:
        pairs = []
        part = ''
        inserted = False

        for letter in meta_data:
            if letter in '[]':
                continue
            if letter in '=""”“':
                if not inserted:
                    pairs.append(part.strip())
                    inserted = True
            else:
                if inserted:
                    part = ''
                    inserted = False

                part += letter

        return pairs
