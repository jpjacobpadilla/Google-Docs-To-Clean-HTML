import re
from lxml import html


class MultiLineTransformations:
    def create_highlightjs_code_blocks(self) -> None:
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

    def create_images(self) -> None:
        pass
