from lxml import html


class AddElements:
    def add_element_above_tag_type(self, *, type: str, add: str) -> None:
        i = 0

        while i < len(self.elements):
            if self.elements[i].tag == type:
                self.elements.insert(i, html.fromstring(add))
                i += 1

            i += 1
    
    def wrap_li_content_in_p_tag(self) -> None:
        """
        Transform:

            <ul>
                <li>content</li>
            </ul>

        To:
        
            <ul>
                <li><p>content</p></li>
            </ul>
        """
        for element in self.elements:
            if element.tag == 'ul':
                for li in element:
                    # Create a new <p> element
                    p_content = html.Element('p')

                    # Move text (if any) of the <li> element to the <p> element
                    if li.text:
                        p_content.text = li.text.strip()
                        li.text = None  # Clear the text from the <li> after moving it

                    # Move all children of the <li> element to the <p> element
                    for child in list(li):
                        p_content.append(child)
                        li.remove(child)

                    li.append(p_content)
