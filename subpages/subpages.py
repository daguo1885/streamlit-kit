
# -*- coding: utf-8 -*-
"""
子页面模块：所有子页面函数集中在此文件

@author: Daguo (大国)
@version: 1.0.0
@create_time: 2024-01-01
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import db_utils


def show_home():
    """
    显示首页
    
    @追溯标记: DG-HOME-RENDER
    """
    from config import SYSTEM_CONFIG
    st.empty()
    st.subheader(f":rainbow[{SYSTEM_CONFIG['sidebar_title']}]", divider='rainbow')
    st.caption('这是一个项目示例，展示了原项目的架构和设计模式！')
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 展示一些示例链接
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("> <font size=4 color=darkgreen><b>常用链接</b></font>", unsafe_allow_html=True)
        st.page_link("https://streamlit.io", label='Streamlit 官方网站')
        st.page_link("https://pandas.pydata.org", label='Pandas 文档')
        st.page_link("https://www.sqlite.org", label='SQLite 官网')
    
    with col2:
        st.markdown("> <font size=4 color=darkblue><b>开发资源</b></font>", unsafe_allow_html=True)
        st.page_link("https://github.com", label='GitHub')
        st.page_link("https://pypi.org", label='PyPI')
        st.page_link("https://stackoverflow.com", label='Stack Overflow')
    
    with col3:
        st.markdown("> <font size=4 color=darkred><b>项目信息</b></font>", unsafe_allow_html=True)
        st.info(f"""
        **项目特点：**
        - 使用 Streamlit 构建
        - SQLite 数据库示例
        - 菜单配置化
        - 授权码验证
        """)


def data_update_page():
    """
    数据更新页面
    """
    st.subheader("🔄 数据更新")
    st.write("这是数据管理功能页面示例。")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("初始化数据库", type="primary"):
            db_utils.init_database()
            st.success("数据库初始化完成！")
    
    with col2:
        st.write("")


def data_query_page():
    """
    数据查询页面
    """
    st.subheader("📋 数据查询")
    st.write("查询示例数据表。")
    
    st.divider()
    
    df = db_utils.get_example_data()
    if not df.empty:
        st.dataframe(df, use_container_width=True)
        
        # 下载数据
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "下载数据 (CSV)",
            csv,
            "example_data.csv",
            "text/csv",
            key='download-csv'
        )
    else:
        st.warning("暂无数据，请先初始化数据库")


def log_view_page():
    """
    日志查看页面
    """
    st.subheader("📝 日志查看")
    st.write("查看用户操作日志。")
    
    st.divider()
    
    df = db_utils.get_operation_logs(100)
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("暂无操作日志")


def example_page_1():
    """
    示例功能页面1
    """
    st.subheader("🔢 功能链接示例1")
    st.write("这是一个示例功能页面，展示数据查询和展示功能。")
    
    st.divider()
    
    # 显示示例数据
    df = db_utils.get_example_data()
    if not df.empty:
        st.write("**示例数据表：**")
        st.dataframe(df, use_container_width=True)
        
        # 简单图表
        st.divider()
        st.write("**数据可视化：**")
        chart_data = df.set_index('name')['value']
        st.bar_chart(chart_data)
    else:
        st.warning("暂无数据")


def example_page_2():
    """
    示例功能页面2
    """
    st.subheader("📊 功能链接示例2")
    st.write("这是另一个示例功能页面。")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**提示：** 这是一个信息提示框")
        number = st.number_input("输入一个数字", value=100)
    
    with col2:
        st.success("**成功：** 这是一个成功提示框")
        text = st.text_input("输入一些文本", "Hello World")
    
    st.divider()
    if st.button("点击测试", type="primary"):
        st.write(f"你输入的数字是：{number}")
        st.write(f"你输入的文本是：{text}")


def example_page_3():
    """
    示例功能页面3
    """
    st.subheader("📈 功能链接示例3")
    st.write("这是第三个示例功能页面，展示一些交互组件。")
    
    st.divider()
    
    # 日期选择
    date = st.date_input("选择日期", datetime.now())
    st.write(f"选择的日期：{date}")
    
    # 下拉选择
    option = st.selectbox(
        "选择一个选项",
        ["选项A", "选项B", "选项C"]
    )
    st.write(f"选择的选项：{option}")
    
    # 多选
    options = st.multiselect(
        "选择多个选项",
        ["选项1", "选项2", "选项3", "选项4"],
        ["选项1"]
    )
    st.write(f"选择的选项：{', '.join(options)}")


def tool_page_1():
    """
    工具示例1
    """
    st.subheader("🔧 工具示例1")
    st.write("这是一个实用工具示例页面。")
    
    st.divider()
    
    uploaded_file = st.file_uploader("上传文件（示例）", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.success(f"文件已上传：{uploaded_file.name}")
        # 尝试读取文件
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.write("文件预览：")
            st.dataframe(df.head(), use_container_width=True)
        except Exception as e:
            st.error(f"读取文件失败：{e}")


def tool_page_2():
    """
    工具示例2
    """
    st.subheader("⚙️ 工具示例2")
    st.write("这是另一个实用工具示例。")
    
    st.divider()
    
    text = st.text_area("输入文本", height=150)
    if text:
        st.write(f"文本长度：{len(text)} 字符")
        st.write(f"单词数（按空格分隔）：{len(text.split())}")
        st.write(f"行数：{len(text.splitlines())}")


def query_page_1():
    """
    查询示例1
    """
    st.subheader("🔍 查询示例1")
    st.write("这是一个查询功能示例页面。")
    
    st.divider()
    
    df = db_utils.get_example_data()
    if not df.empty:
        # 筛选选项
        category = st.selectbox(
            "选择分类筛选",
            ["全部"] + list(df['category'].unique())
        )
        
        filtered_df = df
        if category != "全部":
            filtered_df = df[df['category'] == category]
        
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("暂无数据")


def query_page_2():
    """
    查询示例2
    """
    st.subheader("📊 查询示例2")
    st.write("这是第二个查询功能示例。")
    
    st.divider()
    
    df = db_utils.get_example_data()
    if not df.empty:
        # 统计信息
        st.write("**统计信息：**")
        col1, col2, col3 = st.columns(3)
        col1.metric("总记录数", len(df))
        col2.metric("平均值", f"{df['value'].mean():.2f}")
        col3.metric("总计", f"{df['value'].sum():.2f}")
        
        st.divider()
        st.write("**按分类统计：**")
        category_stats = df.groupby('category')['value'].agg(['sum', 'mean', 'count'])
        st.dataframe(category_stats, use_container_width=True)
    else:
        st.warning("暂无数据")


def query_page_3():
    """
    查询示例3
    """
    st.subheader("📈 查询示例3")
    st.write("这是第三个查询功能示例。")
    
    st.divider()    
    st.info("这是一个占位页面，您可以根据需要实现具体的查询功能。")


