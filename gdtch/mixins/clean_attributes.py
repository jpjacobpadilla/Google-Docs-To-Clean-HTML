from urllib.parse import urlparse, parse_qs


class CleanAttributes:
    def clean_element_attributes(self) -> None:
        self.remove_junk_attrs()
        self.clean_a_tag_attrs()
        self.clean_img_tag_attrs()

    def remove_junk_attrs(self, exclude: set[str] = {'a', 'img'}) -> None:
        for element in self.elements:
            for item in element.iter(): 
                if item.tag not in exclude:
                    item.attrib.clear()
            
    def clean_img_tag_attrs(self) -> None:
        for element in self.elements:
            for img in element.iterfind('.//img'):
                src = img.attrib['src']
                img.attrib.clear()
                img.attrib['src'] = src


    def clean_a_tag_attrs(self) -> None:
        for element in self.elements:
            for a in element.iterfind('.//a[@href]'):
                href = a.attrib['href']
                a.attrib.clear()
                parsed_url = urlparse(href)
                query_params = parse_qs(parsed_url.query)
                
                if 'q' in query_params:
                    actual_link = query_params['q'][0]
                    a.attrib['href'] = actual_link 
                    a.attrib['class'] = 'blue-link'