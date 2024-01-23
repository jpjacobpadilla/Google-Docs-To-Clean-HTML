from gdtch import Cleaner


html_file = "testing/Google-Doc-HTML-Files/Copy of How to Set Up Free Monitoring and Alerting for Your Website (1)/CopyofHowtoSetUpFreeMonitoringandAlertingforY.html"

cleaner = Cleaner(html_file)

# cleaner.remove_top_of_document(element_break='hr')
# cleaner.turn_spans_into_formatting_tags(strong='', strikethrough='', italics='', underline='')
cleaner.clean_all_attributes()
cleaner.add_target_to_outgoing_links(origin="jacobpadilla.com", target='_blank')
cleaner.remove_span_tags()
cleaner.clean_p_text()
cleaner.generate_header_id_attributes()
cleaner.insert_inline_code()
cleaner.create_highlightjs_code_blocks()
cleaner.remove_empty_tags()
cleaner.create_images(article_file_name='hover-media-query')
cleaner.add_element_above_tag(tag='img', add='<br>')

cleaner.pretty_save(file_path='.')