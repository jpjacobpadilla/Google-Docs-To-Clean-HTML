class RemoveTopOfDocument:
    def remove_top_of_document(self, element_break: str = 'hr') -> None:
        for item in self.elements:
            if item.tag == element_break:
                break
            item.drop_tree()