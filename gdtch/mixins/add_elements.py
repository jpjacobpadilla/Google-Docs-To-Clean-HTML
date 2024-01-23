from lxml import html


class AddElements:
    def add_element_above_tag(self, /, tag: str, add: str) -> None:
        i = 0

        while i < len(self.elements):
            if self.elements[i].tag == tag:
                self.elements.insert(i, html.fromstring(add))
                i += 1

            i += 1
