
import re

def replace_main_includable(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_includable_pattern = re.compile(
            r"<b:includable id='main' var='top'>\s*<b:include name='JetBlog'/>\s*</b:includable>",
            re.DOTALL
        )

        replacement_includable = """<b:includable id='main' var='top'>
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
              <div class='d-lg-flex' id='main-content-home'>
                <div class='col-lg-8' id='main-home'>
                  <h2 class='latest-posts-title mb-4'>Latest Posts</h2>
                  <div class='row'>
                      <b:loop values='data:posts' var='post'>
                          <div class='col-lg-6 mb-4'>
                              <b:include data='post' name='JetArchive'/>
                          </div>
                      </b:loop>
                  </div>
                </div>
                <div class='col-lg-4 ps-lg-4' id='sidebar-home'>
                  <b:section class='pt-4' id='sidebar-static-home' itemscope='itemscope' showaddelement='yes'>
                     <b:widget id='HTML19' locked='false' title='Recent Posts' type='HTML' visible='true'>
                        <b:widget-settings>
                          <b:widget-setting name='content'><![CDATA[<div data-title="Recent Posts" class="custom-posts visually-hidden" data-items="5" data-func="sidebar_temp"></div>]]></b:widget-setting>
                        </b:widget-settings>
                        <b:includable id='main'>
                          <b:include name='JetHtml'/>
                        </b:includable>
                      </b:widget>
                      <b:widget id='Label11' locked='false' title='Tags' type='Label' visible='true'>
                        <b:widget-settings>
                          <b:widget-setting name='sorting'>ALPHA</b:widget-setting>
                          <b:widget-setting name='display'>CLOUD</b:widget-setting>
                          <b:widget-setting name='selectedLabelsList'/>
                          <b:widget-setting name='showType'>ALL</b:widget-setting>
                          <b:widget-setting name='showFreqNumbers'>true</b:widget-setting>
                        </b:widget-settings>
                        <b:includable id='main'>
                          <b:include name='JetLabel'/>
                        </b:includable>
                      </b:widget>
                  </b:section>
                </div>
              </div>
            </div>
        </div>
      <b:else/>
        <b:include name='JetBlog'/>
      </b:if>
    </b:includable>"""

        new_content, count = re.subn(original_includable_pattern, replacement_includable, content)

        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully replaced {count} main includable section(s).")
        else:
            print("Error: Could not find the main includable section to replace.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    xml_file_path = 'redesigned-theme.xml'
    replace_main_includable(xml_file_path)
