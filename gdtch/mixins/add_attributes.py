from urllib.parse import urlparse
import re


class AddAttributes:
    def add_target_to_outgoing_links(self, /, origin: str, target: str) -> None:
        for element in self.elements:
            for a in element.iterfind('.//a[@href]'):
                if urlparse(a.attrib['href']).hostname != origin:
                    a.attrib['target'] = target

    def generate_header_id_attributes(self) -> None:
        for element in self.elements:
            if re.match(r'h[1-6]$', element.tag):
                element.attrib['id'] = '-'.join(element.text.lower().split())
