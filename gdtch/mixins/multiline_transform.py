import re
import itertools
from lxml import html


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

    def add_image_attributes(self, article_file_name: str) -> None:
        i = 0

        while i < len(self.elements):
            if self.elements[i].tag == 'img':
                meta_data = self.elements[i - 1].text
                if not meta_data:
                    i += 1
                    continue

                pairs = meta_data.strip('[]').split('=')

                result_dict = {}
                for key, val in itertools.batched(pairs, 2):
                    fkey = key.strip('"”” ')
                    fval = val.strip('"”” ')
                    result_dict[fkey] = fval

                self.elements.pop(i - 1)
                i -= 1

                for attr, val in result_dict.items():
                    self.elements[i].attrib[attr] = val

            i += 1
