from gdtch import Cleaner


HTML_FILE = ''
URL_NAME = 'test'

cleaner = Cleaner(HTML_FILE)

cleaner.remove_top_of_document(element_break='hr')
cleaner.add_strong_tags()
cleaner.clean_element_attributes()
cleaner.add_class_to_element(element='a', class_attr='blue-link')
cleaner.add_target_to_outgoing_links(origin="jacobpadilla.com", target='_blank')
cleaner.remove_span_tags()
cleaner.clean_text()
cleaner.generate_header_id_attributes()
cleaner.insert_inline_code()
cleaner.insert_highlightjs_code_blocks()
cleaner.remove_empty_tags()
cleaner.make_code_block_quotes_straight()

# Super messy template for flask's Jinja server-side rendering engine
cleaner.give_images_unique_names()  # For cache busting
cleaner.alter_image_attributes(path_template=f"{{{{{{{{url_for('articles.static',filename='{URL_NAME}/static/{{original}}')}}}}}}}}")

cleaner.add_element_above_tag_type(type='img', add='<br>')

cleaner.pretty_save(file_path='.')