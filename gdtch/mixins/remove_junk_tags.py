import html as phtml
from lxml import html
import re


class RemoveJunkTags:
    def clean_p_tags_and_text(self):
        i = 0
        while i < len(self.elements):
            tag = self.elements[i]

            for span in tag.iterfind('span'):
                span.drop_tag()

            if len(tag.xpath('.//text()')) == 0 or tag.xpath('.//text()')[0].isspace():
                self.elements.pop(i)

            else:
                html_string = html.tostring(tag, encoding='utf-8', method='html').decode('utf-8')

                # html_string = re.sub(r'<span[^>]*>|</span>', '', html_string)
                html_string = re.sub(r'\s+</p>', '</p>', html_string)
                html_string = re.sub(r'(?<!\w)"', '“', html_string)  # Opening double quotes
                html_string = re.sub(r'"', '”', html_string)  # Closing double quotes
                html_string = re.sub(r"(?<!\w)'", '‘', html_string)  # Opening single quotes
                html_string = re.sub(r"'", '’', html_string)  # Closing single quotes

                self.elements[i] = html.fromstring(html_string)

                i += 1
