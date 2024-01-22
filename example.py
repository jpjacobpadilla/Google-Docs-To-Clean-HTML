from gdtch import Cleaner

cleaner = Cleaner("testing/Google-Doc-HTML-Files/V2 The Most Underused CSS Media Queries_ Hover & Any-Hover (3)/V2TheMostUnderusedCSSMediaQueriesHoverAnyHove.html")

cleaner.remove_top_of_document(element_break='hr')
cleaner.clean_all_attributes(exclude={})
cleaner.clean_p_tags(a_attrs={'class': 'blue-link'})
cleaner.standardize_quotes(single="'", double='"')
cleaner.encode_text(encoding='utf-8')
cleaner.insert_inline_code(attrs={'class': 'inline-code'})
cleaner.generate_header_id_attributes()
cleaner.add_target_to_outgoing_links(target='_blank')
cleaner.create_highlightjs_code_blocks()
cleaner.create_bullet_point_lists(attrs={'class': 'article-bullet-point'})
cleaner.create_images()
cleaner.add_element_above_tag(tag='img', add='br')

cleaner.pretty_save(file_path='.')