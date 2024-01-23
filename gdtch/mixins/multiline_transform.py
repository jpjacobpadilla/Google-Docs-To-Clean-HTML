import re


class MultiLineTransformations:
    def create_highlightjs_code_blocks(self):
        i = 0

        while i < len(self.elements):
            if (text := self.elements[i].text) and re.match(r'```[a-zA-Z]+$', text):
                code = ''
                self.elements.pop(i)
                while not re.match(r'```$', self.elements[i].text):
                    code += self.elements[i].text + '\n'
                    self.elements.pop(i)
                self.elements.pop(i)
                print(code)

            i += 1


    def create_images(self):
        pass

    def create_bullet_point_lists(self):
        pass