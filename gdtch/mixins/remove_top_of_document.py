class RemoveTopOfDocument:
    def remove_top_of_document(self, element_break: str = 'hr') -> None:
        for item in self.root.iterfind('./body/*'):
            item.drop_tree()
            if item.tag == element_break:
                break