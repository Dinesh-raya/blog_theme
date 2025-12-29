
import re

with open('redesigned-theme.xml', 'r') as f:
    content = f.read()

# 1. Add Font Import
original_font_block = """/*
-----------------------------------------------
JetTheme Blogger Template
Name		: JetTheme Core
Version		: 2.9
Designer	: jettheme
URL			: www.jettheme.com
-----------------------------------------------
*/"""
new_font_block = """/*
-----------------------------------------------
JetTheme Blogger Template
Name		: JetTheme Core
Version		: 2.9
Designer	: jettheme
URL			: www.jettheme.com
-----------------------------------------------
*/
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&amp;family=Nunito+Sans:wght@300;400;600;700;800&amp;display=swap');"""
content = content.replace(original_font_block, new_font_block)

# 2. Update Color Variables
original_colors = """<Group description="_Main Color">
<Variable name="keycolor" description="Main Color" type="color" default="#f67938" value="#f67938"/>
<Variable name="body.background" description="Body Background Color" type="color" default="#ffffff" value="#ffffff"/>
<Variable name="body.text.color" description="Font Color" type="color" default="#686868" value="#686868"/>
<Variable name="posts.title.color" description="Heading Color" type="color" default="#343a40" value="#000000"/>
<Variable name="body.link.color" description="Link Color" type="color" default="$(keycolor)" value="#f67938"/>
<Variable name="body.hover.color" description="Link Hover" type="color" default="#f46013" value="#f46013"/>
<Variable name="border.color" description="Border Color" type="color" default="#efefef" value="#efefef"/>
<Variable name="posts.text.color" description="Blockquote Border Color" type="color" default="$(keycolor)" value="#f67938"/>
</Group>"""
new_colors = """<Group description="_Main Color">
<Variable name="keycolor" description="Main Color" type="color" default="#0d6efd" value="#0d6efd"/>
<Variable name="body.background" description="Body Background Color" type="color" default="#ffffff" value="#f8f9fa"/>
<Variable name="body.text.color" description="Font Color" type="color" default="#686868" value="#212529"/>
<Variable name="posts.title.color" description="Heading Color" type="color" default="#343a40" value="#000000"/>
<Variable name="body.link.color" description="Link Color" type="color" default="$(keycolor)" value="#0d6efd"/>
<Variable name="body.hover.color" description="Link Hover" type="color" default="#0a58ca" value="#0a58ca"/>
<Variable name="border.color" description="Border Color" type="color" default="#efefef" value="#dee2e6"/>
<Variable name="posts.text.color" description="Blockquote Border Color" type="color" default="$(keycolor)" value="#0d6efd"/>
</Group>"""
content = content.replace(original_colors, new_colors)

original_header_colors = """<Group description="_Header Color">
<Variable name="header.bg" description="Background" type="color" default="#ffffff" value="#ffffff"/>
<Variable name="header.color" description="Font Color " type="color" default="#686868" value="#686868"/>
<Variable name="header.border" description="Border Color" type="color" default="#efefef" value="#efefef"/>
</Group>"""
new_header_colors = """<Group description="_Header Color">
<Variable name="header.bg" description="Background" type="color" default="#ffffff" value="#ffffff"/>
<Variable name="header.color" description="Font Color " type="color" default="#686868" value="#212529"/>
<Variable name="header.border" description="Border Color" type="color" default="#efefef" value="#dee2e6"/>
</Group>"""
content = content.replace(original_header_colors, new_header_colors)

original_menu_colors = """<Group description="_Menu">
<Variable name="tabs.font" description="Menu Font" type="font" default="normal bold 16px var(--bs-font-sans-serif)" value="normal bold 16px var(--bs-font-sans-serif)"/>
<Variable name="tabs.color" description="Font Color" type="color" default="$(body.text.color)" value="#686868"/>
<Variable name="tabs.hover" description="Font Hover" type="color" default="$(keycolor)" value="#f67938"/>
<Variable name="tabs.selected.color" description="Font Selected" type="color" default="$(keycolor)" value="#f67938"/>
</Group>"""
new_menu_colors = """<Group description="_Menu">
<Variable name="tabs.font" description="Menu Font" type="font" default="normal bold 16px 'Nunito Sans', sans-serif" value="normal bold 16px 'Nunito Sans', sans-serif"/>
<Variable name="tabs.color" description="Font Color" type="color" default="$(body.text.color)" value="#212529"/>
<Variable name="tabs.hover" description="Font Hover" type="color" default="$(keycolor)" value="#0d6efd"/>
<Variable name="tabs.selected.color" description="Font Selected" type="color" default="$(keycolor)" value="#0d6efd"/>
</Group>"""
content = content.replace(original_menu_colors, new_menu_colors)

original_dropdown_colors = """<Group description="_Dropdown Menu">
<Variable name="dropdown.font" description="Font Size" type="length" default="16px" min="12px" max="50px" value="15px"/>
<Variable name="dropdown.bg" description="Background Color" type="color" default="$(body.text.color)" value="#ffffff"/>
<Variable name="dropdown.color" description="Font Color" type="color" default="$(keycolor)" value="#686868"/>
<Variable name="dropdown.hover" description="Font Hover" type="color" default="$(keycolor)" value="#f67938"/>
<Variable name="dropdown.selected" description="Dropdown Selected Color" type="color" default="$(keycolor)" value="#f67938"/>
</Group>"""
new_dropdown_colors = """<Group description="_Dropdown Menu">
<Variable name="dropdown.font" description="Font Size" type="length" default="16px" min="12px" max="50px" value="15px"/>
<Variable name="dropdown.bg" description="Background Color" type="color" default="$(body.text.color)" value="#ffffff"/>
<Variable name="dropdown.color" description="Font Color" type="color" default="$(keycolor)" value="#212529"/>
<Variable name="dropdown.hover" description="Font Hover" type="color" default="$(keycolor)" value="#0d6efd"/>
<Variable name="dropdown.selected" description="Dropdown Selected Color" type="color" default="$(keycolor)" value="#0d6efd"/>
</Group>"""
content = content.replace(original_dropdown_colors, new_dropdown_colors)

original_footer_colors = """<Group description="_Footer Color">
<Variable name="footer.bg" description="Background Color" type="color" default="#212529" value="#212529"/>
<Variable name="footer.color" description="Font Color" type="color" default="#9fa6ad" value="#9fa6ad"/>
<Variable name="footer.link" description="Link Color" type="color" default="#9fa6ad" value="#9fa6ad"/>
<Variable name="footer.border" description="Border Color" type="color" default="#323539" value="#323539"/>
</Group>"""
new_footer_colors = """<Group description="_Footer Color">
<Variable name="footer.bg" description="Background Color" type="color" default="#212529" value="#0a1828"/>
<Variable name="footer.color" description="Font Color" type="color" default="#9fa6ad" value="#ffffff"/>
<Variable name="footer.link" description="Link Color" type="color" default="#9fa6ad" value="#ffffff"/>
<Variable name="footer.border" description="Border Color" type="color" default="#323539" value="#323539"/>
</Group>"""
content = content.replace(original_footer_colors, new_footer_colors)

original_socket_colors = """<Group description="_Socket Color">
<Variable name="socket.bg" description="Background Color" type="color" default="#09080c" value="#09080c"/>
<Variable name="socket.color" description="Font Color" type="color" default="#9fa6ad" value="#9fa6ad"/>
</Group>"""
new_socket_colors = """<Group description="_Socket Color">
<Variable name="socket.bg" description="Background Color" type="color" default="#09080c" value="#0a1828"/>
<Variable name="socket.color" description="Font Color" type="color" default="#9fa6ad" value="#ffffff"/>
</Group>"""
content = content.replace(original_socket_colors, new_socket_colors)

original_button_colors = """<Group description="_Button">
<Variable name="posts.icons.color" description="Button Color" type="color" default="$(keycolor)" value="#f67938"/>
<Variable name="labels.background.color" description="Button Hover"  type="color"  default="#f46013" value="#f46013"/>
</Group>"""
new_button_colors = """<Group description="_Button">
<Variable name="posts.icons.color" description="Button Color" type="color" default="$(keycolor)" value="#0d6efd"/>
<Variable name="labels.background.color" description="Button Hover"  type="color"  default="#0a58ca" value="#0a58ca"/>
</Group>"""
content = content.replace(original_button_colors, new_button_colors)

# 3. Update Typography
original_typography = """<Group description="_Typography">
<Variable name="body.text" description="Body Font" type="font" default="normal normal 16px system-ui,-apple-system,Segoe UI,Helvetica Neue,Arial,Noto Sans,Liberation Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji" value="normal normal 16px system-ui,-apple-system,Segoe UI,Helvetica Neue,Arial,Noto Sans,Liberation Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji"/>
<Variable name="posts.title" description="Heading Font" type="font" default="normal bold 40px var(--bs-font-sans-serif)" value="normal bold 40px var(--bs-font-sans-serif)"/>
<Variable name="title.h2" description="H2 Size" type="length" default="26px" min="12px" max="50px" value="26px"/>
<Variable name="title.h3" description="H3 Size" type="length" default="22px" min="12px" max="50px" value="22px"/>
<Variable name="title.h4" description="H4 Size" type="length" default="20px" min="12px" max="50px" value="20px"/>
<Variable name="title.h5" description="H5 Size" type="length" default="18px" min="12px" max="50px" value="18px"/>
<Variable name="title.h6" description="H6 Size" type="length" default="16px" min="12px" max="50px" value="16px"/>
</Group>"""
new_typography = """<Group description="_Typography">
<Variable name="body.text" description="Body Font" type="font" default="normal normal 16px 'Poppins', sans-serif" value="normal normal 16px 'Poppins', sans-serif"/>
<Variable name="posts.title" description="Heading Font" type="font" default="normal bold 40px 'Nunito Sans', sans-serif" value="normal bold 40px 'Nunito Sans', sans-serif"/>
<Variable name="title.h2" description="H2 Size" type="length" default="26px" min="12px" max="50px" value="26px"/>
<Variable name="title.h3" description="H3 Size" type="length" default="22px" min="12px" max="50px" value="22px"/>
<Variable name="title.h4" description="H4 Size" type="length" default="20px" min="12px" max="50px" value="20px"/>
<Variable name="title.h5" description="H5 Size" type="length" default="18px" min="12px" max="50px" value="18px"/>
<Variable name="title.h6" description="H6 Size" type="length" default="16px" min="12px" max="50px" value="16px"/>
</Group>"""
content = content.replace(original_typography, new_typography)


# 4. Add Custom CSS
custom_css = """/*Your custom CSS is here*/
.hero-section {
    background-color: #0a1828;
    color: #fff;
    padding: 60px 0;
}
.hero-section .hero-title {
    font-size: 48px;
    font-weight: 700;
}
.hero-section .hero-subtitle {
    font-size: 24px;
    font-weight: 300;
}
.trending-section {
    padding: 60px 0;
}
.trending-section .trending-title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 30px;
}
.latest-posts-section {
    padding: 60px 0;
}
.latest-posts-section .latest-posts-title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 30px;
}
.post-card {
    border: 1px solid #dee2e6;
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 30px;
    background-color: #fff;
}
.post-card .post-card-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}
.post-card .post-card-body {
    padding: 20px;
}
.post-card .post-card-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
}
.post-card .post-card-text {
    font-size: 16px;
    color: #6c757d;
    margin-bottom: 15px;
}
.post-card .post-card-meta {
    font-size: 14px;
    color: #6c757d;
}
.post-card .post-card-meta a {
    color: #6c757d;
    text-decoration: none;
}
.post-card .post-card-meta a:hover {
    color: #0d6efd;
}
.about-section {
    padding: 60px 0;
}
.about-section .about-title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 30px;
}
.about-section .about-text {
    font-size: 18px;
    line-height: 1.6;
}
.post-page .post-header {
    margin-bottom: 30px;
}
.post-page .post-title {
    font-size: 40px;
    font-weight: 700;
}
.post-page .post-meta {
    font-size: 14px;
    color: #6c757d;
}
.post-page .post-content {
    font-size: 18px;
    line-height: 1.7;
}
.post-page .post-content img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin: 20px 0;
}
"""
content = content.replace("/*Your custom CSS is here*/", custom_css)

# 5. Fix xlink:href
content = content.replace('xlink:href', 'href')

with open('redesigned-theme.xml', 'w') as f:
    f.write(content)
