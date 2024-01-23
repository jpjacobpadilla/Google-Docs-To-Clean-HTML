from gdtch import Cleaner


html_file = "testing/Google-Doc-HTML-Files/testing (1)/testing.html"

cleaner = Cleaner(html_file)

# cleaner.remove_top_of_document(element_break='hr')
cleaner.clean_all_attributes()
cleaner.add_target_to_outgoing_links(origin="jacobpadilla.com", target='_blank')
cleaner.clean_p_tags_and_text() # TODO: a bit too much coupling
cleaner.generate_header_id_attributes()
cleaner.insert_inline_code()
cleaner.create_highlightjs_code_blocks()
cleaner.remove_empty_tags()
cleaner.create_images(article_file_name='hover-media-query')
cleaner.add_element_above_tag(tag='img', add='<br>')

cleaner.pretty_save(file_path='.')