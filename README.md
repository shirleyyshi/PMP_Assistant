# PMP\_Assistant

帮助 PMP 考生复习和练习的智能辅助平台，包含知识点展示、题目练习、AI 答疑和学习情况梳理功能。

---

## 目录

* 项目介绍
* 技术栈
* 功能模块
* 环境搭建
* 运行项目
* 分支说明
* 项目结构
* 前端协作指南
* 贡献指南

---

## 项目介绍

PMP\_Assistant 是一个基于 Django 后端 + Vue3 前端的全栈项目，帮助 PMP 考生系统化学习和模拟考试。
系统支持用户注册登录、知识点展示、组卷刷题、成绩记录，以及 AI 智能问答功能。

---

## 技术栈

* 后端：Python 3.10+，Django 5.2，Django REST Framework，MySQL
* 前端：Vue 3、Vite、Vue Router、Axios
* 工具：Git、Node.js、npm、Docker（可选）

---

## 功能模块

* 用户管理：注册、登录、权限控制
* 知识点管理：按一级分类 + 二级子分类展示内容
* 题库系统：选择题管理，按知识点组卷随机抽题
* 答题记录：每道题、每次考试的答题情况和分数统计
* AI 助教：基于后端接口的问答系统（可接入大语言模型）

---

## 环境搭建（后端 + 前端开发通用）

### 1. 克隆代码并切换分支

```bash
git clone https://github.com/shirleyyshi/PMP_Assistant.git
cd PMP_Assistant
git checkout frontend
```

### 2. 设置 Python 虚拟环境并安装依赖

```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

### 3. 配置 MySQL 数据库

确保你本地已安装 MySQL，并新建一个数据库，例如：

```sql
CREATE DATABASE pmp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

然后在 `backend/settings.py` 中配置数据库连接：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pmp_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

### 4. 初始化数据库迁移

```bash
python manage.py migrate
```

### 5. 启动 Django 后端服务

```bash
python manage.py runserver
```

---

## 运行项目

* 后端运行地址：[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* 前端运行地址：[http://localhost:5173/](http://localhost:5173/)（默认端口）

---

## 分支说明

* `main`：主分支，后端更新会定期合并到此分支
* `frontend`：前端开发分支，仅包含前端开发需要的文件
* `backend`：后端开发专用分支

---

## 项目结构

```
PMP_Assistant/
├── backend/               # Django 后端
├── frontend/              # Vue3 前端
├── users/                # 用户模块（后端 App）
├── quizzes/              # 题库模块（后端 App）
├── knowledges/           # 知识点模块（后端 App）
├── assistants/           # AI 助教模块（后端 App）
├── manage.py
├── requirements.txt
└── README.md
```

---

## 前端协作指南（适用于前端开发人员）

1. **确保已安装环境**：

   * Node.js 18+
   * npm 9+ （`node -v` / `npm -v` 可查看版本）

2. **克隆项目并切换到 `frontend` 分支**：

```bash
git clone https://github.com/shirleyyshi/PMP_Assistant.git
cd PMP_Assistant
git checkout frontend
```

3. **后端准备**（前端人员不需要改动代码，但需要能正常跑起来）：

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

4. **安装前端依赖并启动**：

```bash
cd frontend
npm install
npm run dev
```

5. **开发建议**：

* 所有前端修改请基于 `frontend` 分支完成，改动后记得 `git add . && git commit && git push`
* 对于需要与后端联调的接口，使用 Axios 调用后端 API（接口文档可查看 Swagger 或直接询问开发）

---

## 贡献指南

* 所有开发需基于对应分支：`frontend` 或 `backend`
* 开发前请先 `git pull` 获取最新代码，开发后请 `commit` 清晰注明修改点
* 请不要直接提交 main 分支，需通过合并
* 如有问题建议统一使用 issue 或微信群沟通

---
