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

    def clean_p_tags_and_text(self) -> None:
        i = 0

        while i < len(self.elements):
            tag = self.elements[i]

            for span in tag.xpath('.//span'):
                span.drop_tag()

            if len(tag.xpath('.//text()')) != 0 and not tag.xpath('.//text()')[0].isspace():
                html_string = html.tostring(tag, encoding='utf-8', method='html').decode('utf-8')

                html_string = re.sub(r'\s+</p>', '</p>', html_string)
                html_string = self.process_html(html_string)

                self.elements[i] = html.fromstring(html_string)
            
            i += 1

    @staticmethod
    def convert_quotes(text):
        text = re.sub(r'(?<!\w)"', '“', text)
        text = re.sub(r'"(?!\w)', '”', text)
        text = re.sub(r"(?<!\w)'", '‘', text)
        text = re.sub(r"'(?!\w)", '’', text)
        return text

    @staticmethod
    def process_html(html_string):
        parts = re.split(r'(<[^>]+>)', html_string)  # Split by HTML tags
        for i, part in enumerate(parts):
            if not re.match(r'<[^>]+>', part):  # If it's not a tag
                parts[i] = RemoveJunkTags.convert_quotes(part)  # Convert quotes in text
        return ''.join(parts)