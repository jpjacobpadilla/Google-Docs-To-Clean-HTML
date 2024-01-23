import html as phtml
from lxml import html
import re


class RemoveJunkTags:
    def clean_p_tags_and_text(self):
        i = 0
        while i < len(self.elements):
            p = self.elements[i]
            if p.tag != 'p':
                i += 1
                continue

            if len(p.xpath('.//text()')) > 0 and not p.xpath('.//text()')[0].isspace():
                cleaned_p = self.clean_html(p)

                text = html.tostring(cleaned_p, encoding='utf-8', method='html').decode('utf-8')

                text = re.sub(r'\s+</p>', '</p>', text)
                text = re.sub(r'(?<!\w)"', '“', text)  # Opening double quotes
                text = re.sub(r'"', '”', text)  # Closing double quotes
                text = re.sub(r"(?<!\w)'", '‘', text)  # Opening single quotes
                text = re.sub(r"'", '’', text)  # Closing single quotes

                p = html.fromstring(phtml.escape(text, quote=False))

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