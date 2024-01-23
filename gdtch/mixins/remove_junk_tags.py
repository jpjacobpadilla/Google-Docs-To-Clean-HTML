from lxml import html
import re


class RemoveJunkTags:
    def remove_empty_tags(self) -> None:
        i = 0

        while i < len(self.elements):
            tag = self.elements[i]

            if (img := tag.xpath('.//img')):
                self.elements[i] = img[0]
                i += 1

            elif len(tag.xpath('.//text()')) == 0 or tag.xpath('.//text()')[0].isspace():
                self.elements.pop(i)

            else:
                i += 1

    def remove_span_tags(self) -> None:
        for tag in self.elements:
            for span in tag.xpath('.//span'):
                span.drop_tag()