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
      position: relative;
      overflow-x: auto;
    }
    button.copy-btn {
      position: absolute;
      top: 5px;
      right: 5px;
      background: #007acc;
      color: white;
      border: none;
      padding: 4px 8px;
      cursor: pointer;
      font-size: 0.8em;
      border-radius: 3px;
    }
    strong {
      font-size: 1.1em;
    }
  </style>
</head>
<body>

  <h1><strong>🚀 Django Project Setup Guide</strong></h1>

  <h2><strong>🗂️ Project Architecture</strong></h2>
  <pre><code id="code-arch">Myfirstdjango/
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
└── README.md</code><button class="copy-btn" onclick="copyCode('code-arch')">Copy</button></pre>

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
  <pre><code id="code1">python -m venv &lt;env_name&gt;
# Example:
python -m venv .venv</code><button class="copy-btn" onclick="copyCode('code1')">Copy</button></pre>

  <pre><code id="code2">.venv\Scripts\activate</code><button class="copy-btn" onclick="copyCode('code2')">Copy</button></pre>

  <pre><code id="code3">Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned</code><button class="copy-btn" onclick="copyCode('code3')">Copy</button></pre>

  <h3><strong>3. Install Django:</strong></h3>
  <pre><code id="code4">py -m pip install Django</code><button class="copy-btn" onclick="copyCode('code4')">Copy</button></pre>

  <h2><strong>⚙️ Starting the Project</strong></h2>
  <pre><code id="code5">django-admin startproject myfirstdjango
cd myfirstdjango
python manage.py runserver</code><button class="copy-btn" onclick="copyCode('code5')">Copy</button></pre>

  <script>
    function copyCode(id) {
      const code = document.getElementById(id).innerText;
      navigator.clipboard.writeText(code);
      alert("Copied to clipboard!");
    }
  </script>

</body>
</html>
