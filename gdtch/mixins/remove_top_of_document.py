class RemoveTopOfDocument:
    def remove_top_of_document(self, element_break: str = 'hr') -> None:
        while self.elements[0].tag != element_break:
            self.elements.pop(0)

        if self.elements[0].tag != element_break:
            self.elements.pop(0)