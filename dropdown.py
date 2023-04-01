import streamlit as st

# 定义下拉菜单的选项
options = {
    'Link 1': 'https://www.ilovepdf.com/zh-tw/merge_pdf',
    'Link 2': 'https://en.y2mate.is/52/',
    'Link 3': 'https://scholar.google.com/'
}

# 创建下拉菜单
selected_option = st.selectbox('请选择一个链接', list(options.keys()))

# 获取用户选择的链接
selected_link = options[selected_option]

# 在浏览器中打开链接
if st.button('前往链接'):
    st.write('正在前往链接，请稍候...')
    js = f"window.open('{selected_link}')"  # 构建JavaScript代码
    html = f"<script>{js}</script>"  # 将JavaScript代码插入HTML
    st.write(html, unsafe_allow_html=True)  # 在Streamlit中显示HTML代码
