<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Django Project Setup</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background: #fdfdfd;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    pre {
      background: #f4f4f4;
      padding: 10px;
      border-left: 4px solid #007acc;
      overflow-x: auto;
    }
    strong {
      font-size: 1.1em;
    }
  </style>
</head>
<body>

  <h1><strong>🚀 Django Project Setup Guide</strong></h1>

  <h2><strong>🗂️ Project Architecture</strong></h2>
  <pre>
Myfirstdjango/
│
├── Media/
│   ├── Ss1/
│   └── Ss2/
│
├── Myfirstdjango/  ← Django main project folder
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── Second/  ← Your app
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   └── tests.py
│
├── static/
│   └── style.css
│
├── Templates/
│   └── theme/
│
├── db.sqlite3
├── manage.py
└── README.md
  </pre>

  <h2><strong>📦 Installation</strong></h2>

  <h3><strong>1. Install Python:</strong></h3>
  <ul>
    <li>Install <code>python-3.7.2</code> and <code>pip</code>.</li>
    <li>Reference:
      <a href="https://docs.python-guide.org/starting/installation/" target="_blank">
        https://docs.python-guide.org/starting/installation/
      </a>
    </li>
  </ul>

  <h3><strong>2. Set Up Virtual Environment:</strong></h3>
  <pre>
python -m venv <env_name>
# Example:
python -m venv .venv
  </pre>

  <pre>
.venv\Scripts\activate
  </pre>

  <pre>
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  </pre>

  <h3><strong>3. Install Django:</strong></h3>
  <pre>
py -m pip install Django
  </pre>

  <h2><strong>⚙️ Starting the Project</strong></h2>
  <pre>
django-admin startproject myfirstdjango
cd myfirstdjango
python manage.py runserver
  </pre>

</body>
</html>
