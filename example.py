from gdtch import Cleaner


html_file = "testing/Google-Doc-HTML-Files/V2 The Most Underused CSS Media Queries_ Hover & Any-Hover (3)/V2TheMostUnderusedCSSMediaQueriesHoverAnyHove.html"

cleaner = Cleaner(html_file)

cleaner.remove_top_of_document(element_break='hr')
cleaner.clean_all_attributes()
# cleaner.clean_p_tags()
# cleaner.standardize_quotes()
# cleaner.encode_text()
# cleaner.insert_inline_code()
# cleaner.generate_header_id_attributes()
# cleaner.add_target_to_outgoing_links(target='_blank')
# cleaner.create_highlightjs_code_blocks()
# cleaner.create_bullet_point_lists()
# cleaner.create_images()
# cleaner.add_element_above_tag(tag='img', add='br')

cleaner.pretty_save(file_path='.')