import re
from lxml import html, etree

class AlterText:
    def insert_inline_code(self) -> None:
        pattern = re.compile(r'`(.*?)`')

        for i, element in enumerate(self.elements):
            if element.text:
                text = html.tostring(element, method='html', encoding='utf-8').decode('utf-8')
                text = pattern.sub(r'<code class="inline-code">\1</code>', text)
                self.elements[i] = html.fromstring(text)