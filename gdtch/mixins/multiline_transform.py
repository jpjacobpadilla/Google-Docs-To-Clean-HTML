import re
from lxml import html


class MultiLineTransformations:
    def create_highlightjs_code_blocks(self):
        i = 0

        while i < len(self.elements):
            if (text := self.elements[i].text) and re.match(r'```[a-zA-Z]+$', text):
                self.elements.pop(i)

                code = ''
                while not re.match(r'```$', self.elements[i].text):
                    code += self.elements[i].text + '\n'
                    self.elements.pop(i)

                self.elements.pop(i)

                pre_element = html.Element("pre")
                code_element = html.Element("code")
                code_element.text = code.removesuffix('\n')
                pre_element.append(code_element)
                self.elements.insert(i, pre_element)

            i += 1

    def create_images(self):
        pass

    def create_bullet_point_lists(self):
        pass