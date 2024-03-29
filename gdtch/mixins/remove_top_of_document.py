from gdtch.exceptions import NoBreakElementFound


class RemoveTopOfDocument:
    def remove_top_of_document(self, element_break: str = 'hr') -> None:
        while len(self.elements) > 0 and self.elements[0].tag != element_break:
            self.elements.pop(0)

        if len(self.elements) == 0:
            raise NoBreakElementFound()

        self.elements.pop(0)