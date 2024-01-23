class CleanAttributes:
    def clean_all_attributes(self):
        self.remove_junk_attrs()
        self.clean_a_tag_attrs()

    def remove_junk_attrs(self, exclude: set[str] = {'a'}) -> None:
        for element in self.elements:
            for item in element.iter(): 
                if item.tag not in exclude:
                    item.attrib.clear()
            
    def clean_a_tag_attrs(self) -> None:
        pass



    def generate_header_id_attributes(self):
        pass

    def add_target_to_outgoing_links(self, target='_blank'):
        pass