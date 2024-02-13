from lxml import html


class AddElements:
    def add_element_above_tag_type(self, *, type: str, add: str) -> None:
        i = 0

        while i < len(self.elements):
            if self.elements[i].tag == type:
                self.elements.insert(i, html.fromstring(add))
                i += 1

            i += 1
    
    def wrap_list_text_in_p_tag(self) -> None:
        """
        Transform elements inside of ul or ol elements with a p tag like such:

            <ul>
                <li>content</li>
            </ul>

        To:
        
            <ul>
                <li><p>content</p></li>
            </ul>
        """
        for element in self.elements:
            if element.tag in ('ul', 'ol'):
                for sub_element in element:
                    p_content = html.Element('p')

                    if sub_element.text:
                        p_content.text = sub_element.text.strip()
                        sub_element.text = None 

                    # Move all children of the <li> element to the <p> element
                    for child in list(sub_element):
                        p_content.append(child)
                        sub_element.remove(child)

                    sub_element.append(p_content)
