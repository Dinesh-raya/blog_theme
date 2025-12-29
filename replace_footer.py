import re

def replace_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the new footer content
    new_footer = """
<footer content='itemid' id='footer' itemid='#footer' itemscope='itemscope' itemtype='https://schema.org/WPFooter'>
<div class='py-5 fs-7' id='footer-main'>
  <div class='container px-3'>
    <b:section class='row' id='footer-widget' showaddelement='yes'>
      <div class='col-lg-4 mb-4'>
        <b:widget id='HTML21' locked='false' title='About Us' type='HTML' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<p>Exploring the world of code, one line at a time.</p>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
        <b:include name='JetHtml'/>
      </b:includable>
        </b:widget>
      </div>
      <div class='col-lg-8'>
        <div class='row'>
          <div class='col-md-4 mb-4'>
            <b:widget id='LinkList13' locked='false' title='Learn More' type='LinkList' version='2' visible='true'>
              <b:widget-settings>
                <b:widget-setting name='sorting'>NONE</b:widget-setting>
                <b:widget-setting name='text-1'>About</b:widget-setting>
                <b:widget-setting name='link-1'>/p/about.html</b:widget-setting>
                <b:widget-setting name='text-0'>Contact</b:widget-setting>
                <b:widget-setting name='link-0'>/p/contact.html</b:widget-setting>
                <b:widget-setting name='text-2'>Sitemap</b:widget-setting>
                <b:widget-setting name='link-2'>/p/sitemap.html</b:widget-setting>
              </b:widget-settings>
              <b:includable id='main'>
                <b:include name='JetLinkList'/>
              </b:includable>
              <b:includable id='content'/>
            </b:widget>
          </div>
          <div class='col-md-4 mb-4'>
            <b:widget id='LinkList14' locked='false' title='Follow Us' type='LinkList' version='2' visible='true'>
              <b:widget-settings>
                <b:widget-setting name='sorting'>NONE</b:widget-setting>
                <b:widget-setting name='text-0'>github</b:widget-setting>
                <b:widget-setting name='link-0'>#</b:widget-setting>
                <b:widget-setting name='text-1'>twitter</b:widget-setting>
                <b:widget-setting name='link-1'>#</b:widget-setting>
                <b:widget-setting name='text-2'>instagram</b:widget-setting>
                <b:widget-setting name='link-2'>#</b:widget-setting>
              </b:widget-settings>
              <b:includable id='main'>
                <b:include name='JetSocial'/>
              </b:includable>
              <b:includable id='content'/>
            </b:widget>
          </div>
          <div class='col-md-4 mb-4'>
            <b:widget id='HTML22' locked='false' title='Newsletter' type='HTML' version='2' visible='true'>
              <b:widget-settings>
                <b:widget-setting name='content'>Stay up to date with the latest news and relevant updates from us.</b:widget-setting>
              </b:widget-settings>
              <b:includable id='main'>
            <b:include name='JetFollowIt'/>
          </b:includable>
            </b:widget>
          </div>
        </div>
      </div>
    </b:section>
  </div>
</div>
<div class='py-3 fs-7 text-center' id='socket'>
<b:section class='container px-3' id='copyright' maxwidgets='1' showaddelement='no'>
  <b:widget id='HTML23' locked='true' title='Copyright' type='HTML' version='2' visible='true'>
    <b:widget-settings>
      <b:widget-setting name='content'><![CDATA[Copyright &copy; 2024 SyntaxLight. All rights reserved.]]></b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
      <b:include name='JetCopyRight'/>
    </b:includable>
  </b:widget>
</b:section>
</div>
</footer>
"""

    # Use regex to find and replace the footer section
    updated_content = re.sub(r"<footer.*?</footer>", new_footer, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

if __name__ == "__main__":
    replace_footer('redesigned-theme.xml')
