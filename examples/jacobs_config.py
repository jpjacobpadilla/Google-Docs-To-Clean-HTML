from gdtch import Cleaner


HTML_FILE = '/path/to/html.html'

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
cleaner.give_images_unique_names() 
cleaner.alter_image_attributes(path_template='articles/example/{original}')
cleaner.add_element_above_tag_type(type='img', add='<br>')

cleaner.pretty_save(file_path='/clean_html.html')

# Or you can get back the result as a string by not specifying a file path:
content = cleaner.pretty_save()
print(content)