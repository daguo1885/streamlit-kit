
# -*- coding: utf-8 -*-
"""
辅助管理系统示例
基于 Streamlit 框架构建

@author: Daguo (大国)
@version: 1.0.0
@project: 辅助管理系统示例
@description: 
    本项目为 Streamlit 学习示例，展示了客舱部辅助管理系统的架构设计。
    如需部署或修改，请保留此头部信息。
    
@copyright: Copyright 2024-2026 Daguo. All rights reserved.
@create_time: 2024-01-01
@last_modified: 2026-05-21
"""
import streamlit as st
import sys
import os

# 导入配置和数据库模块
from config import (
    SYSTEM_CONFIG,
    ACCESS_CODE_CONFIG,
    MENU_CONFIG,
    CURRENT_PATH
)
import db_utils

# 导入子页面模块（直接从单个文件导入）
from subpages.subpages import (
    show_home,
    data_update_page, data_query_page, log_view_page,
    example_page_1, example_page_2, example_page_3,
    tool_page_1, tool_page_2,
    query_page_1, query_page_2, query_page_3
)


def init_settings():
    """
    初始化设置：Streamlit 页面基本配置
    """
    st.set_page_config(
        page_title=SYSTEM_CONFIG["page_title"],
        page_icon=SYSTEM_CONFIG["page_icon"],
        layout="wide",
        initial_sidebar_state="auto"
    )
    
    # 隐藏菜单和页脚的样式
    hide_streamlit_style = """
        <style>
        /* @追溯标记: DG-CSS-HIDE-MENU */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        div[data-testid=stVerticalBlock]{gap: 0.6rem;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # 调整主页面位置
    st.markdown("""
        <style>
            /* @追溯标记: DG-CSS-STYLE */
            html {
            font-size: 14px;}
            .st-emotion-cache-1mi2ry5{
            padding: 1rem 1rem 1rem; height: 0;}
            .st-emotion-cache-12fmjuu{
            height: 1rem}
            .st-emotion-cache-1jicfl2{
            padding-left: 1rem; padding-right: 1rem; padding-top: 1rem;}                                    
        </style>
        <!-- @追溯标记: DG-HTML-COMMENT -->""", unsafe_allow_html=True)
    
    # 初始化 session_state
    if 'first_visit' not in st.session_state:
        st.session_state.first_visit = True
    else:
        st.session_state.first_visit = False
    
    if st.session_state.first_visit:
        st.session_state.func_code = "首页"
        st.session_state.access_flag = False
        st.session_state.access_code = ""
        st.session_state.user_id = ""


def verify_access_code(input_code):
    """
    验证授权码
    """
    # 尝试使用 st.secrets（如果有配置）
    try:
        # 从 secrets 读取授权码配置
        if hasattr(st, 'secrets') and 'access_codes' in st.secrets:
            for role, config in st.secrets.access_codes.items():
                if input_code == config.get('code', ''):
                    return True, config.get('name', role), config.get('menu', 'user')
    except Exception:
        pass
    
    # 使用配置文件中的默认配置
    for role, config in ACCESS_CODE_CONFIG.items():
        if input_code == config['code']:
            return True, config['name'], config['menu']
    
    return False, "", ""


def sidebar():
    """
    侧边栏：授权码验证、菜单导航
    """
    # 侧边栏标题
    st.sidebar.title(f":blue[{SYSTEM_CONFIG['sidebar_title']}]")
    
    info = st.sidebar.empty()
    
    # 授权码输入
    if not st.session_state.access_flag:
        with info:
            with st.container():
                input_code = st.text_input(
                    '请输入使用授权码，按Enter键确认',
                    type='password',
                    help='请联系管理员获取授权码'
                )
                st.session_state.access_code = input_code
        
        # 验证授权码
        if st.session_state.access_code:
            valid, user_name, menu_type = verify_access_code(st.session_state.access_code)
            if valid:
                st.session_state.access_flag = True
                st.session_state.user_id = user_name
                st.session_state.menu_type = menu_type
                info.empty()
                info.markdown('<br>', unsafe_allow_html=True)
                info.write(f'Welcome {st.session_state.user_id}')
                render_menu(menu_type, info)
            else:
                st.sidebar.error('请输入正确的授权码！')
    else:
        info.markdown('<br>', unsafe_allow_html=True)
        info.write(f'Welcome {st.session_state.user_id}')
        render_menu(st.session_state.menu_type, info)
    
    # 版权信息
    st.sidebar.caption(SYSTEM_CONFIG["copyright"])


def render_menu(menu_type, info):
    """
    根据菜单类型渲染侧边栏菜单
    """
    menu_config = MENU_CONFIG.get(menu_type, [])
    
    for section in menu_config:
        with st.sidebar.expander(
            f"{section['icon']} {section['name']}",
            expanded=section['expanded']
        ):
            # 计算列数（最多2列）
            col_count = min(2, len(section['items']))
            if col_count > 1:
                cols = st.columns(col_count)
            else:
                cols = [st]
            
            for idx, item in enumerate(section['items']):
                col_idx = idx % col_count
                if cols[col_idx].button(item['label'], use_container_width=True):
                    info.caption(f'{item["label"]}')
                    st.session_state.func_code = item['code']
                    # 记录操作日志
                    db_utils.add_operation_log(
                        st.session_state.user_id,
                        item['code'],
                        f'点击了{item["label"]}'
                    )


def main():
    """
    主程序
    
    @追溯标记: DG-MAIN-EXEC
    """
    init_settings()
    sidebar()
    
    # 初始化数据库
    try:
        db_utils.init_database()
    except Exception as e:
        pass
    
    if st.session_state.access_flag:
        # 根据 func_code 显示对应页面
        func_code = st.session_state.func_code
        
        if func_code == '首页':
            show_home()
        elif func_code == 'data_update':
            data_update_page()
        elif func_code == 'data_query':
            data_query_page()
        elif func_code == 'log_view':
            log_view_page()
        elif func_code == 'func1':
            example_page_1()
        elif func_code == 'func2':
            example_page_2()
        elif func_code == 'func3':
            example_page_3()
        elif func_code == 'tool1':
            tool_page_1()
        elif func_code == 'tool2':
            tool_page_2()
        elif func_code == 'query1':
            query_page_1()
        elif func_code == 'query2':
            query_page_2()
        elif func_code == 'query3':
            query_page_3()
        else:
            show_home()
    else:
        show_home()


# ============================================================
# 追溯信息（不可见）
# @追溯标记: DG-PROJECT-SIGNATURE
# 项目代号: DG-CABIN-SYSTEM
# 作者: Daguo
# 版本: 1.0.0
# ============================================================


if __name__ == '__main__':
    main()
