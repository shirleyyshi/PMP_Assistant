

# PMP\_Assistant

帮助 PMP 考生复习和练习的智能辅助平台，包含知识点展示、题目练习、AI 答疑和学习情况梳理功能。

---

## 目录

* [项目介绍](#项目介绍)
* [技术栈](#技术栈)
* [功能模块](#功能模块)
* [环境搭建](#环境搭建)
* [运行项目](#运行项目)
* [分支说明](#分支说明)
* [项目结构](#项目结构)
* [贡献指南](#贡献指南)

---

## 项目介绍

PMP\_Assistant 是一个基于 Django 后端 + Vue3 前端的全栈项目，帮助 PMP 考生系统化学习和模拟考试。
支持用户注册登录，知识点浏览，组卷刷题，答题成绩记录，以及 AI 智能答疑。

---

## 技术栈

* **后端**: Python 3.10+，Django 5.2，Django REST Framework，MySQL 数据库
* **前端**: Vue 3，Vite，Vue Router，Axios
* **其他工具**: Git，Docker（可选）

---

## 功能模块

* 用户管理（注册、登录、权限管理）
* 知识点展示（按一级+二级分类）
* 题库管理（选择题、组卷、答题）
* 答题记录与成绩统计
* AI 答疑助教（基于后台接口）

---

## 环境搭建

### 1. 克隆代码

```bash
git clone -b frontend https://github.com/shirleyyshi/PMP_Assistant.git
cd PMP_Assistant
```

### 2. 配置 Python 虚拟环境及依赖（后端）

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

* 创建数据库（示例）：

```sql
CREATE DATABASE pmp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

* 修改 `backend/settings.py` 中数据库配置，填写你的数据库用户名密码
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

### 4. 迁移数据库

```bash
python manage.py migrate
```

### 5. 启动 Django 后端

```bash
python manage.py runserver
```

### 6. 安装并启动前端依赖

```bash
cd frontend
npm install
npm run dev
```

---

## 运行项目

* 后端服务默认运行在 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* 前端开发服务器默认运行在 [http://localhost:5173/](http://localhost:5173/) （端口可根据实际情况调整）

---

## 分支说明

* `main`：稳定主分支，保持后端和前端代码同步且稳定
* `frontend`：前端开发分支，前端人员主要在此分支进行开发和调试
* `backend`：后端开发分支（如有），后端人员独立开发

---

## 项目结构

```
PMP_Assistant/
├── backend/             # Django 后端项目文件夹
├── frontend/            # Vue3 前端项目文件夹
├── manage.py            # Django 管理脚本
├── requirements.txt     # Python 后端依赖
├── .gitignore
└── README.md
```

---

## 贡献指南

* 统一遵守代码规范，提交前请先拉取最新代码并测试
* 前端开发请切换到 `frontend` 分支进行
* 后端开发请切换到 `backend`分支
* 有任何问题或需求，请及时在项目 issue 中反馈

---

