from gdtch import Cleaner


HTML_FILE = '/PATH/TO/HTML/FILe/NAME.html'

cleaner = Cleaner(HTML_FILE)

cleaner.clean_element_attributes()
cleaner.remove_span_tags()
cleaner.clean_p_text()
cleaner.remove_empty_tags()

cleaner.pretty_save(file_path='.')