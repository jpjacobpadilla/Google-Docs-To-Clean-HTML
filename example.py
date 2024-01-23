from gdtch import Cleaner


html_file = "testing/Google-Doc-HTML-Files/Notes.html"

cleaner = Cleaner(html_file)

cleaner.remove_top_of_document(element_break='hr')
cleaner.clean_element_attributes()
cleaner.add_target_to_outgoing_links(origin="jacobpadilla.com", target='_blank')
cleaner.remove_span_tags()
cleaner.clean_p_text()
cleaner.generate_header_id_attributes()
cleaner.insert_inline_code()
cleaner.insert_highlightjs_code_blocks()
cleaner.remove_empty_tags()
cleaner.add_image_attributes(article_file_name='hover-media-query')
cleaner.add_element_above_tag_type(type='img', add='<br>')

cleaner.pretty_save(file_path='.')