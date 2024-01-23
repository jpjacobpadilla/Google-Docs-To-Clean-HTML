from urllib.parse import urlparse, parse_qs
import html as phtml
from lxml import html
import re

class RemoveJunkTags:
    def clean_p_tags(self):
        i = 0
        while i < len(self.elements):
            p = self.elements[i]
            if p.tag != 'p':
                i += 1
                continue

            if len(p.xpath('.//text()')) > 0 and not p.xpath('.//text()')[0].isspace():
                cleaned_p = self.clean_html(p)
                decoded_string = html.tostring(cleaned_p, encoding='utf-8', method='html').decode('utf-8')
                no_extra_space_string = re.sub(r'\s+</p>', '</p>', decoded_string)
                new_html = no_extra_space_string.replace("‘", "'").replace("’", "'")
                p = html.fromstring(new_html)
                i += 1

            else:
                self.elements.pop(i)

    @staticmethod
    def clean_html(element):
        if element.tag not in ['p', 'a']:
            if element.tail:  # Preserve the tail text
                previous = element.getprevious()
                if previous is not None:
                    previous.tail = (previous.tail or '') + (element.text or '') + (element.tail or '')
                else:
                    parent = element.getparent()
                    if parent is not None:
                        parent.text = (parent.text or '') + (element.text or '') + (element.tail or '')

            element.drop_tag() 

        else:
            for attribute in ["id", "class", "style"]:
                if element.get(attribute):
                    element.attrib.pop(attribute)

            for child in list(element):
                RemoveJunkTags.clean_html(child)

        return element