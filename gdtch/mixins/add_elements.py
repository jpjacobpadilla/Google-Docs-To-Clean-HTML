from lxml import html


class AddElements:
    def add_strong_tags(self) -> None:
        for tag in self.elements:
            if tag.tag.startswith('h') and tag.tag[-1].isnumeric():
                continue

            for span in tag.xpath('.//span'):
                if self._get_styles(list(span.classes)).get('font-weight', 0) >= 700 and span.text:
                    strong_tag = html.Element('strong')
                    strong_tag.text = span.text.replace('&nbsp;', ' ')

                    parent  = span.getparent()
                    parent.replace(span, strong_tag)

    def _get_styles(self, classes) -> dict:
        properties = {}
        for rule in self.styles:
            if rule.type == rule.STYLE_RULE:
                for selector in rule.selectorText.split(','):
                    if self.selector_matches_element(selector.strip(), classes):
                        for property in rule.style:
                            # This overwrites properties if multiple rules apply
                            properties[property.name] = int(property.value) if \
                                property.value.isnumeric() else property.value
        return properties

    def selector_matches_element(self, selector, classes):
        return selector.startswith('.') and selector[1:] in classes

    def add_element_above_tag_type(self, *, type: str, add: str) -> None:
        i = 0

        while i < len(self.elements):
            if self.elements[i].tag == type:
                self.elements.insert(i, html.fromstring(add))
                i += 1

            i += 1
    