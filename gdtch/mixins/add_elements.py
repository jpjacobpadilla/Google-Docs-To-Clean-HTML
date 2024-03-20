from lxml import html


class AddElements:
    def add_strong_tags(self) -> None:
        for tag in self.elements:
            if tag.tag.startswith('h') and tag.tag[-1].isnumeric():
                continue

            for span in tag.xpath('.//span'):
                if self._get_styles(list(span.classes)).get('font-weight', 0) >= 700 and span.text:
                    strong_tag = html.Element('strong')
                    strong_tag.text = span.text

                    parent  = span.getparent()
                    parent.replace(span, strong_tag)

    def _get_styles(self, classes: list) -> dict:
        properties = {}
        for rule in self.styles:
            if rule.type != rule.STYLE_RULE:
                continue

            for selector in rule.selectorText.split(','):
                selector = selector.strip()
                if not self.selector_matches_element(selector, classes):
                    continue

                for css_property in rule.style:
                    # Convert numeric values to integers, otherwise keep the original value
                    value = css_property.value
                    properties[css_property.name] = int(value) if value.isnumeric() else value

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
    