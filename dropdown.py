pip install PyPDF2


import streamlit as st
from PyPDF2 import PdfFileMerger
import io

st.title('PDF文檔合併工具')

# 创建一个上传文件的控件
uploaded_files = st.file_uploader(
    label='请选择要合併的PDF文檔（可以選擇多個）',
    accept_type=['pdf'],
    type='pdf',
    multiple_files=True
)

# 如果没有上传文件则显示提示信息
if uploaded_files is None:
    st.info('请上传您要合併的PDF文檔')

# 创建一个按钮用于合併PDF文档
if st.button('合併PDF文档'):
    try:
        # 创建一个PDF合并器对象
        merger = PdfFileMerger()

        # 将上传的PDF文档添加到合并器对象中
        for uploaded_file in uploaded_files:
            pdf_reader = io.BytesIO(uploaded_file.read())
            merger.append(pdf_reader)

        # 将合并后的PDF文档保存到本地
        output_pdf = io.BytesIO()
        merger.write(output_pdf)

        # 显示合并后的PDF文档
        st.success('PDF文档合并完成！')
        st.download_button(
            label='下载合并后的PDF文档',
            data=output_pdf.getvalue(),
            file_name='merged_document.pdf',
            mime='application/pdf'
        )

    except Exception as e:
        st.error(e)
