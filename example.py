from gdtch import Cleaner

cleaner = Cleaner("testing/Google-Doc-HTML-Files/V2 The Most Underused CSS Media Queries_ Hover & Any-Hover (3)/V2TheMostUnderusedCSSMediaQueriesHoverAnyHove.html")
cleaner.remove_top_of_document()
cleaner.clean_p_tags()
cleaner.pretty_save(file_path='.')