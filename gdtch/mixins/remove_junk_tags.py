from urllib.parse import urlparse, parse_qs
import html as phtml
from lxml import html
import re

class RemoveJunkTags:
    def clean_p_tags(self):
        # remove junk tags and white space at end but also add
            # 1. strong
            # 2. underline
            # 3. italics
            # 4. strikethrough

        # Function to recursively remove all tags except <p> and <a>
        def clean_html(element):
            if element.tag not in ['p', 'a']:
                if element.tail:  # Preserve the tail text
                    previous = element.getprevious()
                    if previous is not None:
                        previous.tail = (previous.tail or '') + (element.text or '') + (element.tail or '')
                    else:
                        parent = element.getparent()
                        if parent is not None:
                            parent.text = (parent.text or '') + (element.text or '') + (element.tail or '')
                element.drop_tag() 

            else:
                # Remove specific attributes
                for attribute in ["id", "class", "style"]:
                    if element.get(attribute):
                        element.attrib.pop(attribute)

                for child in list(element):
                    clean_html(child)

            return element


        # Iterate over each <a> tag
        for a in self.root.xpath('//a[@href]'):
            href = a.attrib['href']
            parsed_url = urlparse(href)
            query_params = parse_qs(parsed_url.query)
            
            # Check if 'q' parameter is in the URL
            if 'q' in query_params:
                actual_link = query_params['q'][0]  # Extract the first 'q' parameter
                a.attrib['href'] = actual_link  # Replace href attribute
                a.attrib['class'] = 'blue-link'

        for p in self.root.xpath('.//p[not(ancestor::table)]'):
            if len(p.xpath('.//text()')) > 0 and not p.xpath('.//text()')[0].isspace():
                cleaned_p = clean_html(p)
                cleaned_p.text = phtml.escape(cleaned_p.text, quote=False)

                decoded_string = html.tostring(cleaned_p, encoding='utf-8', method='html').decode('utf-8')
                final_string = re.sub(r'\s+</p>', '</p>', decoded_string)
                # Use regular expression to remove whitespace before the closing </p> tag
                no_extra_space_string = re.sub(r'\s+</p>', '</p>', decoded_string)

                # Replace left single quotation mark with straight single quote
                # Ensure you're using the correct character
                final_string = no_extra_space_string.replace("‘", "'").replace("’", "'")


                # add inline code
                pattern = r'`(.*?)`'
                p.text = re.sub(pattern, r'<code class="inline-code">\1</code>', final_string)

            else:
                p.drop_tree()