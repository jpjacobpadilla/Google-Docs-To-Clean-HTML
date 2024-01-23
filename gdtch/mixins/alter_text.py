import re
from lxml import html

class AlterText:
    def insert_inline_code(self) -> None:
        pattern = r'`(.*?)`'

        for element in self.elements:
            if element.text:
                text = element.text
                text = re.sub(pattern, r'<code class="inline-code">\1</code>', text)
                element.clear()
                element.append(html.fromstring(text))