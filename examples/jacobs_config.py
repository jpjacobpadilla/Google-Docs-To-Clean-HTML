from gdtch import Cleaner


HTML_FILE = ''
URL_NAME = 'test'

cleaner = Cleaner(HTML_FILE)

cleaner.remove_top_of_document(element_break='hr')
cleaner.clean_element_attributes()
cleaner.add_class_to_element(element='a', class_attr='blue-link')
cleaner.add_target_to_outgoing_links(origin="jacobpadilla.com", target='_blank')
cleaner.remove_span_tags()
cleaner.clean_p_text()
cleaner.generate_header_id_attributes()
cleaner.insert_inline_code()
cleaner.insert_highlightjs_code_blocks()
cleaner.remove_empty_tags()
cleaner.wrap_list_text_in_p_tag()

# Super messy template for flask's Jinja server side rendering engine
cleaner.alter_image_attributes(path_template=f"{{{{{{{{url_for('articles.static',filename='{URL_NAME}/static/{{original}}')}}}}}}}}")

cleaner.add_element_above_tag_type(type='img', add='<br>')

cleaner.pretty_save(file_path='.')