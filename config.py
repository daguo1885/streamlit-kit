
# -*- coding: utf-8 -*-
"""
配置文件：菜单配置、授权码配置、系统配置

@author: Daguo (大国)
@version: 1.0.0
@create_time: 2024-01-01
"""
import os

# 当前目录路径
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

# 系统配置
SYSTEM_CONFIG = {
    "page_title": "辅助管理系统示例",
    "page_icon": "🌈",
    "sidebar_title": "辅助管理系统示例",
    "copyright": "© 2025 示例系统"
}

# 授权码配置（明码）
ACCESS_CODE_CONFIG = {
    "admin": {
        "name": "管理员",
        "code": "admin",
        "menu": "admin"
    },
    "user1": {
        "name": "功能角色1",
        "code": "user1",
        "menu": "user"
    },
    "user2": {
        "name": "功能角色2",
        "code": "user2",
        "menu": "query"
    }
}

# 菜单配置
MENU_CONFIG = {
    "admin": [
        {
            "name": "数据管理",
            "icon": "🔢",
            "expanded": True,
            "items": [
                {"label": "数据更新", "code": "data_update"},
                {"label": "数据查询", "code": "data_query"},
                {"label": "日志查看", "code": "log_view"}
            ]
        },
        {
            "name": "功能模块",
            "icon": "📊",
            "expanded": True,
            "items": [
                {"label": "功能链接示例1", "code": "func1"},
                {"label": "功能链接示例2", "code": "func2"},
                {"label": "功能链接示例3", "code": "func3"},
            ]
        },
        {
            "name": "实用工具",
            "icon": "🔨",
            "expanded": False,
            "items": [
                {"label": "工具示例1", "code": "tool1"},
                {"label": "工具示例2", "code": "tool2"}
            ]
        }
    ],
    "user": [
        {
            "name": "主要功能",
            "icon": "📈",
            "expanded": True,
            "items": [
                {"label": "功能链接示例1", "code": "func1"},
                {"label": "功能链接示例2", "code": "func2"}
            ]
        },
        {
            "name": "查询功能",
            "icon": "🔍",
            "expanded": True,
            "items": [
                {"label": "查询示例1", "code": "query1"},
                {"label": "查询示例2", "code": "query2"}
            ]
        }
    ],
    "query": [
        {
            "name": "数据查询",
            "icon": "🔍",
            "expanded": True,
            "items": [
                {"label": "查询示例1", "code": "query1"},
                {"label": "查询示例2", "code": "query2"},
                {"label": "查询示例3", "code": "query3"}
            ]
        }
    ]
}

# 数据库配置
DB_CONFIG = {
    "sqlite_path": os.path.join(CURRENT_PATH, "data", "example.db")
}

# 确保数据目录存在
os.makedirs(os.path.join(CURRENT_PATH, "data"), exist_ok=True)
