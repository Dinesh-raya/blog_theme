import re

def replace_main_content_text(filepath):
    try:
        # Read the original XML file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Define the new content for the JetBlog includable
        # This includes the conditional logic for the homepage
        new_jetblog_content = """<b:includable id='JetBlog'>
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
                    <!-- Trending posts will be loaded here -->
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
      <b:with value='(data:widgets where (w => w.type == data:widget.type and w.id == data:widget.instanceId )).first' var='jwidget'>
        <b:if cond='data:view.isError OR data:numPosts == 0'>
          <b:include name='JetBreadcrumbs'/>
          <b:include name='Jet404'/>
        <b:elseif cond='data:view.isMultipleItems'/>
          <b:include name='JetBreadcrumbs'/>
          <div class='widget-content'>
            <div class='row row-cols-sm-2' id='blog-content'>
              <b:loop values='data:posts' var='post'>
                <article class='item-post mb-4'>
                  <b:include data='post' name='JetArchive'/>
                </article>
              </b:loop>
            </div>
            <b:include name='JetPagination'/>
          </div>
        <b:else/>
          <b:loop values='data:posts' var='post'>
            <b:if cond='data:view.isPost'>
              <b:include data='post' name='JetBreadcrumbs'/>
              <b:include data='post' name='JetPost'/>
              <b:include name='JetPagination'/>
              <b:include data='post' name='JetComments'/>
              <b:include data='post' name='JetRelatedPost'/>
            <b:elseif cond='data:view.isPage'/>
              <b:include data='post' name='JetPage'/>
              <b:include data='post' name='JetComments'/>
            </b:if>
          </b:loop>
       </b:if>
      </b:with>
    </b:if>
</b:includable>"""

        # Use a more flexible regex to find the JetBlog includable section
        # This accounts for potential attributes like var='top'
        pattern = re.compile(r"<b:includable\s+id='JetBlog'[^>]*>.*?</b:includable>", re.DOTALL)

        # Check if the pattern is found
        if pattern.search(content):
            updated_content = pattern.sub(new_jetblog_content, content)

            # Write the updated content back to the file
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print("Main content replaced successfully using text replacement.")
        else:
            print("JetBlog includable section not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    xml_file_path = 'redesigned-theme.xml'
    replace_main_content_text(xml_file_path)
