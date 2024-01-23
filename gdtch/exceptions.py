class GoogleDocsToCleanHTML(Exception):
    """Base Exception"""

    START_COLOR = "\033[95m"
    END_COLOR = "\033[0m"

    REPORT_MSG = """\n\t
        Feel free to submit a report here:
        https://github.com/jpjacobpadilla/Google-Docs-To-Clean-HTML/issues/new
    """

    def __init__(self, message: str = ''):
        if not message:
            message = f'\n\n\t{self.__doc__.replace('\n', '\n    ')}'
        super().__init__(f'{self.START_COLOR}{message}{self.REPORT_MSG}{self.END_COLOR}')

    
class NoBreakElementFound(GoogleDocsToCleanHTML):
    """
    This Exception is raised when the method remove_top_of_document 
    goes through all of the elements in the self.elements list
    but can't find the element_break tag.
    """
    pass