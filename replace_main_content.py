import xml.etree.ElementTree as ET
import os

def replace_main_content(filepath):
    try:
        # Register namespaces to ensure they are preserved on output
        namespaces = {
            '': 'http://www.w3.org/1999/xhtml',
            'b': 'http://www.google.com/2005/gml/b',
            'data': 'http://www.google.com/2005/gml/data',
            'expr': 'http://www.google.com/2005/gml/expr',
        }
        for prefix, uri in namespaces.items():
            if prefix == '':
                continue
            ET.register_namespace(prefix, uri)

        # Parse the XML file
        tree = ET.parse(filepath)
        root = tree.getroot()

        # Find the JetBlog includable using the correct namespace
        # The find method requires the namespace URI in curly braces
        jetblog_includable = root.find(".//*[@id='JetBlog']")

        if jetblog_includable is not None:
            # Store original content by deep copying to avoid modification issues
            original_content = [ET.fromstring(ET.tostring(child)) for child in jetblog_includable]

            # Clear the existing content
            jetblog_includable.clear()

            # The new homepage structure as a string.
            # This needs to be valid XML, so we wrap it in a div with namespaces
            homepage_structure_string = """
<div xmlns:b="http://www.google.com/2005/gml/b" xmlns:data="http://www.google.com/2005/gml/data" xmlns:expr="http://www.google.com/2005/gml/expr">
    <b:if cond='data:view.isHomepage'>
        <div class='hero-section'>
            <div class='container text-center'>
                <h1 class='hero-title'>SyntaxLight</h1>
                <p class='hero-subtitle'>Exploring the world of code, one line at a time.</p>
            </div>
        </div>
        <div class='trending-section py-5'>
            <div class='container'>
                <h2 class='trending-title text-center mb-4'>Trending Posts</h2>
                <div class='custom-posts' data-func='related_temp' data-label='trending' data-items='4' data-title='Trending'>
                    <!-- Trending posts content will be loaded here -->
                </div>
            </div>
        </div>
        <div class='latest-posts-section py-5'>
            <div class='container'>
                <h2 class='latest-posts-title mb-4'>Latest Posts</h2>
                <div class='row'>
                    <b:loop values='data:posts' var='post'>
                        <div class='col-lg-6 mb-4'>
                            <b:include data='post' name='JetArchive'/>
                        </div>
                    </b:loop>
                </div>
            </div>
        </div>
        <b:else/>
        <!-- This is a placeholder for the original content -->
    </b:if>
</div>
"""
            # Parse the new structure from the string
            new_structure_wrapper = ET.fromstring(homepage_structure_string)

            # The parsed structure is a div containing b:if. We want the b:if.
            new_if_statement = new_structure_wrapper.find('{http://www.google.com/2005/gml/b}if')

            if new_if_statement is not None:
                # Find the b:else tag inside the new b:if
                else_tag = new_if_statement.find('{http://www.google.com/2005/gml/b}else')

                if else_tag is not None:
                    # Append the original content into the b:else tag
                    for child in original_content:
                        else_tag.append(child)

                # Append the complete b:if statement to the jetblog_includable
                jetblog_includable.append(new_if_statement)

            # Write the changes back to the file
            # Use the default namespace for the html element
            tree.write(filepath, encoding='unicode', xml_declaration=True, default_namespace=namespaces[''])
            print("Main content replaced successfully with conditional logic.")
        else:
            print("JetBlog includable not found.")

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    xml_file_path = 'redesigned-theme.xml'
    replace_main_content(xml_file_path)
