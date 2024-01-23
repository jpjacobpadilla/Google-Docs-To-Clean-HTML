from urllib.parse import urlparse


class AddAttributes:
    def add_target_to_outgoing_links(self, /, origin: str, target: str) -> None:
        for element in self.elements:
            for a in element.iterfind('.//a[@href]'):
                if urlparse(a.attrib['href']).hostname != origin:
                    a.attrib['target'] = target

    def generate_header_id_attributes(self):
        pass
