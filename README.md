
# 🚀 Streamlit Kit

&gt; 作者：**Daguo（大国）**  
&gt; 版本：**1.0.0**  
&gt; 创建时间：**2024-01-01**

---

## 📌 项目简介

这是一个基于 **Streamlit** 单页面架构搭建的**极简授权访问页面系统**，旨在为数据分析师、建模工程师等提供最快捷、最低成本的数据展示和分享方案。

---

## ✨ 核心特点

### 1️⃣ 单页面授权访问系统

- 采用 Streamlit 单页面架构，学习成本低
- 增加了授权码访问功能，便于内部小范围授权访问
- 支持多角色权限管理（管理员、用户等）
- 完美适用于数据分析、数据共享、建模展示等场景

### 2️⃣ 极简克制的设计理念

- 极少的外部依赖库（仅需 3 个核心库）
- 代码结构清晰，易于理解和修改
- 对新手极其友好，学习曲线平缓
- SQLite 数据库，无需配置 MySQL 等复杂数据库

### 3️⃣ 专注数据分析与展示

- 让数据分析师专注于数据分析与处理
- 不必花费太多精力关注页面展示和权限控制
- 菜单配置化，通过 `config.py` 即可完成菜单布局
- 提供标准的页面结构和交互逻辑

### 4️⃣ 极佳的学习项目

- 适合作为 Streamlit 入门学习项目
- 代码规范，注释清晰
- 展示了 Streamlit 完整的应用架构
- 包含了侧边栏菜单、状态管理、功能路由等核心功能

---

## 🛠️ 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| **Python** | 3.8+ | 核心编程语言 |
| **Streamlit** | ≥1.28.0 | Web 应用框架 |
| **Pandas** | ≥2.0.0 | 数据处理 |
| **SQLite** | 内置 | 数据存储 |
| **openpyxl** | ≥3.1.0 | Excel 支持（可选） |

---

## 📁 项目结构

```
streamlit-kit/
├── .streamlit/
│   └── secrets.toml          # 授权码配置（可选）
├── pages/
│   └── subpages.py           # 所有子页面函数
├── static/                   # 静态资源目录
├── data/                     # 数据目录（自动生成）
├── app.py                    # 主程序入口
├── config.py                 # 配置文件（菜单、授权码等）
├── db_utils.py               # SQLite 数据库工具
├── requirements.txt          # 依赖库
└── README.md                 # 本文件
```

---

## 🚀 快速开始

### 1. 环境要求

- Python 3.8 或更高版本
- pip 包管理器

### 2. 安装步骤

1. **克隆或下载项目**

   ```bash
   # 如果使用 git
   git clone &lt;项目地址&gt;
   cd streamlit-kit
   ```

2. **创建虚拟环境（推荐）**

   ```bash
   python -m venv .venv
   ```

3. **激活虚拟环境**
   - Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - Linux/Mac:

     ```bash
     source .venv/bin/activate
     ```

4. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

5. **运行项目**

   ```bash
   streamlit run app.py
   ```

浏览器会自动打开 `http://localhost:8501`，您就可以看到应用了！

---

## 🔑 测试授权码

项目预置了几个测试授权码，便于您快速体验：

| 角色 | 授权码 | 说明 |
|------|--------|------|
| **管理员** | `admin` | 可访问所有菜单 |
| **功能角色1** | `user1` | 可访问部分功能 |
| **功能角色2** | `user2` | 可访问查询类功能 |

---

## 📖 使用指南

### 配置菜单

在 [`config.py`](file:///e:/Codes/Apps/CabinApp/streamlit-kit/config.py) 中的 `MENU_CONFIG` 配置：

```python
MENU_CONFIG = {
    "admin": [
        {
            "name": "数据管理",
            "icon": "🔢",
            "expanded": True,
            "items": [
                {"label": "数据更新", "code": "data_update"},
                {"label": "数据查询", "code": "data_query"},
            ]
        }
    ]
}
```

### 添加新页面

1. 在 [`pages/subpages.py`](file:///e:/Codes/Apps/CabinApp/streamlit-kit/pages/subpages.py) 中添加新的页面函数：

   ```python
   def my_new_page():
       st.subheader(":rainbow[我的新页面]", divider='rainbow')
       st.caption("页面功能说明")
       st.write("这里是页面内容")
   ```

2. 在 [`config.py`](file:///e:/Codes/Apps/CabinApp/streamlit-kit/config.py) 中添加菜单项

3. 在 [`app.py`](file:///e:/Codes/Apps/CabinApp/streamlit-kit/app.py) 的 `main()` 函数中添加路由逻辑

### 页面函数生成提示词

如需快速生成页面函数代码，可以使用以下提示词模板向AI助手描述需求：

```plaintext
请帮我创建一个Streamlit页面函数，需求如下：

【页面需求】
<请在此描述页面功能需求>

【技术要求】
1. 使用 Streamlit 框架
2. 不要使用 st.sidebar 功能
3. 输出为单个页面函数，函数名格式为 def page_xxx():
4. 必须以 st.subheader 定义页面标题，st.caption 定义页面说明
5. 可以使用 Streamlit 的各种组件（st.button, st.selectbox, st.dataframe 等）

【输出格式】
```python
def page_xxx():
    st.subheader(":rainbow[页面标题]", divider='rainbow')
    st.caption("页面说明")
    
    # 页面内容
    # ...
```

```

**示例输入**：
```plaintext
请帮我创建一个Streamlit页面函数，需求如下：

【页面需求】
创建一个用户管理页面，包含用户列表展示、添加用户表单、搜索功能

【技术要求】
1. 使用 Streamlit 框架
2. 不要使用 st.sidebar 功能
3. 输出为单个页面函数，函数名格式为 def page_xxx():
4. 必须以 st.subheader 定义页面标题，st.caption 定义页面说明
5. 可以使用 Streamlit 的各种组件（st.button, st.selectbox, st.dataframe 等）

【输出格式】
```python
def page_xxx():
    st.subheader(":rainbow[页面标题]", divider='rainbow')
    st.caption("页面说明")
    
    # 页面内容
    # ...
```

```

### 修改授权码

编辑 [`config.py`](file:///e:/Codes/Apps/CabinApp/streamlit-kit/config.py) 中的 `ACCESS_CODE_CONFIG`：

```python
ACCESS_CODE_CONFIG = {
    "my_role": {
        "name": "我的角色",
        "code": "my_password",  # 这里使用明码
        "menu": "admin"
    }
}
```

---

## 🎯 适合人群

✅ **数据分析师** - 快速搭建数据展示页面  
✅ **建模工程师** - 展示机器学习模型和分析结果  
✅ **团队内部协作** - 小范围内按需授权访问数据  
✅ **Streamlit 学习者** - 学习完整的 Streamlit 应用架构  
✅ **Python 新手** - 学习成本低，代码清晰

---

## 📊 原项目特点保留

- ✅ 侧边栏菜单导航
- ✅ 授权码验证机制
- ✅ 相同的页面布局和样式
- ✅ 功能代码路由方式
- ✅ session_state 状态管理

---

## 🔍 追溯标记说明

本项目在代码中包含了多处追溯标记，用于识别代码来源：

### 代码追溯标记

- **DG-PROJECT-SIGNATURE** - 项目签名（app.py 末尾）
- **DG-MAIN-EXEC** - 主程序执行标记
- **DG-HOME-RENDER** - 首页渲染标记
- **DG-2024-SYS-INIT** - 系统初始化标记

### 数据库追溯标记

- **DG-SYS-TRACE-2024** - 系统追溯表（自动创建于 SQLite 数据库）
- **sys_info** - 系统信息表，包含创建者和创建时间

### CSS/HTML 追溯标记

- **DG-CSS-HIDE-MENU** - 样式隐藏菜单标记
- **DG-CSS-STYLE** - 样式配置标记
- **DG-HTML-COMMENT** - HTML 注释标记

### 查找方法

1. 在代码中搜索 `@追溯标记`
2. 在数据库中查询 `sys_info` 表
3. 在浏览器开发者工具中查看页面源码

---

## 📝 开发建议

1. **保持极简** - 只添加必要的功能
2. **配置优先** - 尽量通过 `config.py` 配置，减少硬编码
3. **注释清晰** - 关键代码添加详细注释
4. **测试充分** - 确保在不同环境下能正常运行

---

## 📄 许可证

示例项目，作者：**Daguo（大国）**  
Copyright 2024-2026 Daguo. All rights reserved.

---

## 🙏 致谢

感谢 Streamlit 团队提供了这么优秀的框架，让数据分析变得更加简单和有趣！

---

## 💬 联系方式

如有问题或建议，欢迎交流！

---

&gt; 本项目是一个开源示例，旨在帮助大家更好地学习和使用 Streamlit。希望这个项目能对您有所帮助！💪
