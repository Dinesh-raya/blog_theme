
import re

with open('redesigned-theme.xml', 'r') as f:
    content = f.read()

original_header = """<header class='header-animate sticky-top navbar py-0 navbar-expand-lg' content='itemid' id='header' itemid='#header' itemscope='itemscope' itemtype='https://schema.org/WPHeader'>
<input class='d-none' id='navbar-toggle' type='checkbox'/>
<b:section class='container position-relative px-3 flex-nowrap' id='header-main' maxwidgets='3' showaddelement='no'>
  <b:widget id='HTML10' locked='true' title='Logo' type='HTML' version='2' visible='true'>
    <b:widget-settings>
      <b:widget-setting name='content'>https://1.bp.blogspot.com/-mo6pIle8rXw/YLplHDA1ZCI/AAAAAAAAATo/JPbzsy_srC8gFem56vJZ3wua-A5qClFxACLcBGAsYHQ/w175-h55/jettheme-logo.png</b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
        <b:include name='JetLogo'/>
      </b:includable>
  </b:widget>
  <b:widget id='LinkList10' locked='true' title='Icons, Dark, Search' type='LinkList' version='2' visible='true'>
    <b:widget-settings>
      <b:widget-setting name='sorting'>NONE</b:widget-setting>
      <b:widget-setting name='text-1'>instagram</b:widget-setting>
      <b:widget-setting name='link-1'>#</b:widget-setting>
      <b:widget-setting name='text-0'>facebook</b:widget-setting>
      <b:widget-setting name='link-0'>#</b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
      <b:include name='JetSearch'/>
    </b:includable>
    <b:includable id='content'/>
  </b:widget>
  <b:widget id='LinkList11' locked='true' title='Menu' type='LinkList' version='2' visible='true'>
    <b:widget-settings>
      <b:widget-setting name='text-8'>Contact</b:widget-setting>
      <b:widget-setting name='link-7'>/p/sitemap.html</b:widget-setting>
      <b:widget-setting name='link-8'>/p/contact.html</b:widget-setting>
      <b:widget-setting name='link-5'>#</b:widget-setting>
      <b:widget-setting name='link-6'>#sub-end</b:widget-setting>
      <b:widget-setting name='link-3'>#sub-start</b:widget-setting>
      <b:widget-setting name='link-4'>#</b:widget-setting>
      <b:widget-setting name='text-1'>About</b:widget-setting>
      <b:widget-setting name='text-0'>Home</b:widget-setting>
      <b:widget-setting name='text-3'>Sub Menu 1</b:widget-setting>
      <b:widget-setting name='text-2'>Tech</b:widget-setting>
      <b:widget-setting name='text-5'>DropDown</b:widget-setting>
      <b:widget-setting name='text-4'>DropDown</b:widget-setting>
      <b:widget-setting name='text-7'>Sitemap</b:widget-setting>
      <b:widget-setting name='text-6'>Sub Menu 1</b:widget-setting>
      <b:widget-setting name='sorting'>NONE</b:widget-setting>
      <b:widget-setting name='link-1'>/p/about.html</b:widget-setting>
      <b:widget-setting name='link-2'>/search/label/Tech?max-results=10</b:widget-setting>
      <b:widget-setting name='link-0'>/</b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
      <b:include name='JetMenu'/>
    </b:includable>
    <b:includable id='content'/>
  </b:widget>
</b:section>
</header>"""

new_header = """<header class='header-animate sticky-top navbar py-0 navbar-expand-lg' content='itemid' id='header' itemid='#header' itemscope='itemscope' itemtype='https://schema.org/WPHeader'>
<input class='d-none' id='navbar-toggle' type='checkbox'/>
<b:section class='container position-relative px-3 flex-nowrap' id='header-main' maxwidgets='3' showaddelement='no'>
  <b:widget id='HTML10' locked='true' title='Logo' type='HTML' version='2' visible='true'>
    <b:widget-settings>
      <b:widget-setting name='content'>SyntaxLight</b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
        <b:include name='JetLogo'/>
      </b:includable>
  </b:widget>
  <b:widget id='LinkList11' locked='true' title='Menu' type='LinkList' version='2' visible='true'>
    <b:widget-settings>
      <b:widget-setting name='text-8'>Contact</b:widget-setting>
      <b:widget-setting name='link-7'>/p/sitemap.html</b:widget-setting>
      <b:widget-setting name='link-8'>/p/contact.html</b:widget-setting>
      <b:widget-setting name='link-5'>#</b:widget-setting>
      <b:widget-setting name='link-6'>#sub-end</b:widget-setting>
      <b:widget-setting name='link-3'>#sub-start</b:widget-setting>
      <b:widget-setting name='link-4'>#</b:widget-setting>
      <b:widget-setting name='text-1'>About</b:widget-setting>
      <b:widget-setting name='text-0'>Home</b:widget-setting>
      <b:widget-setting name='text-3'>Sub Menu 1</b:widget-setting>
      <b:widget-setting name='text-2'>Tech</b:widget-setting>
      <b:widget-setting name='text-5'>DropDown</b:widget-setting>
      <b:widget-setting name='text-4'>DropDown</b:widget-setting>
      <b:widget-setting name='text-7'>Sitemap</b:widget-setting>
      <b:widget-setting name='text-6'>Sub Menu 1</b:widget-setting>
      <b:widget-setting name='sorting'>NONE</b:widget-setting>
      <b:widget-setting name='link-1'>/p/about.html</b:widget-setting>
      <b:widget-setting name='link-2'>/search/label/Tech?max-results=10</b:widget-setting>
      <b:widget-setting name='link-0'>/</b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
      <b:include name='JetMenu'/>
    </b:includable>
    <b:includable id='content'/>
  </b:widget>
  <b:widget id='LinkList10' locked='true' title='Icons, Dark, Search' type='LinkList' version='2' visible='true'>
    <b:widget-settings>
      <b:widget-setting name='sorting'>NONE</b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
      <b:include name='JetSearch'/>
    </b:includable>
    <b:includable id='content'/>
  </b:widget>
</b:section>
</header>"""

content = content.replace(original_header, new_header)

with open('redesigned-theme.xml', 'w') as f:
    f.write(content)
