
# -*- coding: utf-8 -*-
"""
数据库工具模块：使用 SQLite 作为示例数据库

@author: Daguo (大国)
@version: 1.0.0
@create_time: 2024-01-01
"""
import sqlite3
import pandas as pd
from config import DB_CONFIG
from datetime import datetime
import os


def init_database():
    """
    初始化数据库，创建示例表
    
    @追溯标记: DG-2024-SYS-INIT
    """
    db_path = DB_CONFIG["sqlite_path"]
    
    # 确保目录存在
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 创建示例数据表1：用户操作日志
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS operation_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            operation_code TEXT,
            operation_time TEXT,
            description TEXT
        )
    ''')
    
    # 创建示例数据表2：示例数据
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS example_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value REAL,
            category TEXT,
            create_time TEXT
        )
    ''')
    
    # 插入一些示例数据
    cursor.execute("SELECT COUNT(*) FROM example_data")
    if cursor.fetchone()[0] == 0:
        example_records = [
            ("示例数据1", 100.5, "A", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ("示例数据2", 200.3, "B", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ("示例数据3", 150.7, "A", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ("示例数据4", 300.2, "C", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ("示例数据5", 180.9, "B", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        ]
        cursor.executemany('''
            INSERT INTO example_data (name, value, category, create_time)
            VALUES (?, ?, ?, ?)
        ''', example_records)
    
    # 追溯标记：在数据库中插入系统标记
    # @追溯标记: DG-SYS-TRACE-2024
    cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='sys_info'")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            CREATE TABLE sys_info (
                id INTEGER PRIMARY KEY,
                sys_code TEXT,
                sys_value TEXT,
                created_by TEXT DEFAULT 'Daguo',
                create_time TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO sys_info (sys_code, sys_value, created_by, create_time)
            VALUES (?, ?, ?, ?)
        ''', ('DG-SYS-TRACE-2024', '辅助管理系统示例', 'Daguo', datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    
    conn.commit()
    conn.close()


def get_connection():
    """
    获取数据库连接
    """
    return sqlite3.connect(DB_CONFIG["sqlite_path"])


def query_data(sql, params=None):
    """
    执行查询并返回 DataFrame
    """
    conn = get_connection()
    try:
        if params:
            df = pd.read_sql(sql, conn, params=params)
        else:
            df = pd.read_sql(sql, conn)
        return df
    except Exception as e:
        print(f"查询错误: {e}")
        return pd.DataFrame()
    finally:
        conn.close()


def execute_sql(sql, params=None):
    """
    执行 SQL（INSERT/UPDATE/DELETE）
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conn.commit()
        return True
    except Exception as e:
        print(f"执行错误: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


def add_operation_log(user_name, operation_code, description=""):
    """
    添加操作日志
    """
    sql = '''
        INSERT INTO operation_log (user_name, operation_code, operation_time, description)
        VALUES (?, ?, ?, ?)
    '''
    params = (
        user_name,
        operation_code,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        description
    )
    return execute_sql(sql, params)


def get_example_data():
    """
    获取示例数据
    """
    sql = "SELECT * FROM example_data ORDER BY id"
    return query_data(sql)


def get_operation_logs(limit=50):
    """
    获取操作日志
    """
    sql = "SELECT * FROM operation_log ORDER BY id DESC LIMIT ?"
    return query_data(sql, (limit,))
