class CleanAttributes:
    def clean_all_attributes(self):
        self.remove_junk_attrs(self, exclude={'a'})
        self.clean_a_tag_attrs(self)

    def generate_header_id_attributes(self):
        pass

    def add_target_to_outgoing_links(self, target='_blank'):
        pass