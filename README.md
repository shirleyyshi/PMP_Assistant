

# PMP\_Assistant

���� PMP ������ϰ����ϰ�����ܸ���ƽ̨������֪ʶ��չʾ����Ŀ��ϰ��AI ���ɺ�ѧϰ��������ܡ�

---

## Ŀ¼

* [��Ŀ����](#��Ŀ����)
* [����ջ](#����ջ)
* [����ģ��](#����ģ��)
* [�����](#�����)
* [������Ŀ](#������Ŀ)
* [��֧˵��](#��֧˵��)
* [��Ŀ�ṹ](#��Ŀ�ṹ)
* [����ָ��](#����ָ��)

---

## ��Ŀ����

PMP\_Assistant ��һ������ Django ��� + Vue3 ǰ�˵�ȫջ��Ŀ������ PMP ����ϵͳ��ѧϰ��ģ�⿼�ԡ�
֧���û�ע���¼��֪ʶ����������ˢ�⣬����ɼ���¼���Լ� AI ���ܴ��ɡ�

---

## ����ջ

* **���**: Python 3.10+��Django 5.2��Django REST Framework��MySQL ���ݿ�
* **ǰ��**: Vue 3��Vite��Vue Router��Axios
* **��������**: Git��Docker����ѡ��

---

## ����ģ��

* �û�����ע�ᡢ��¼��Ȩ�޹���
* ֪ʶ��չʾ����һ��+�������ࣩ
* ������ѡ���⡢������⣩
* �����¼��ɼ�ͳ��
* AI �������̣����ں�̨�ӿڣ�

---

## �����

### 1. ��¡����

```bash
git clone -b frontend https://github.com/shirleyyshi/PMP_Assistant.git
cd PMP_Assistant
```

### 2. ���� Python ���⻷������������ˣ�

```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. ���� MySQL ���ݿ�

* �������ݿ⣨ʾ������

```sql
CREATE DATABASE pmp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

* �޸� `backend/settings.py` �����ݿ����ã���д������ݿ��û�������
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

### 4. Ǩ�����ݿ�

```bash
python manage.py migrate
```

### 5. ���� Django ���

```bash
python manage.py runserver
```

### 6. ��װ������ǰ������

```bash
cd frontend
npm install
npm run dev
```

---

## ������Ŀ

* ��˷���Ĭ�������� [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* ǰ�˿���������Ĭ�������� [http://localhost:5173/](http://localhost:5173/) ���˿ڿɸ���ʵ�����������

---

## ��֧˵��

* `main`���ȶ�����֧�����ֺ�˺�ǰ�˴���ͬ�����ȶ�
* `frontend`��ǰ�˿�����֧��ǰ����Ա��Ҫ�ڴ˷�֧���п����͵���
* `backend`����˿�����֧�����У��������Ա��������

---

## ��Ŀ�ṹ

```
PMP_Assistant/
������ backend/             # Django �����Ŀ�ļ���
������ frontend/            # Vue3 ǰ����Ŀ�ļ���
������ manage.py            # Django ����ű�
������ requirements.txt     # Python �������
������ .gitignore
������ README.md
```

---

## ����ָ��

* ͳһ���ش���淶���ύǰ������ȡ���´��벢����
* ǰ�˿������л��� `frontend` ��֧����
* ��˿������л��� `backend`��֧
* ���κ�����������뼰ʱ����Ŀ issue �з���

---

