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
    h1, h2 {
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

  <h2><strong>📦 Installation</strong></h2>

  <h3><strong>1. Install Python:</strong></h3>
  <ul>
    <li>Install <code>python-3.7.2</code> and <code>pip</code>.</li>
    <li>Follow the steps from the reference below based on your OS:<br>
      <a href="https://docs.python-guide.org/starting/installation/" target="_blank">
        https://docs.python-guide.org/starting/installation/
      </a>
    </li>
  </ul>

  <h3><strong>2. Set Up Virtual Environment:</strong></h3>

  <p><strong>Creating virtual environment:</strong></p>
  <pre><code id="code1">python -m venv &lt;name of the environment&gt;
# Example:
python -m venv .venv</code><button class="copy-btn" onclick="copyCode('code1')"></button></pre>

  <p><strong>Activating virtual environment (for Windows):</strong></p>
  <pre><code id="code2">&lt;env name&gt;\Scripts\activate
# Example:
.venv\Scripts\activate</code><button class="copy-btn" onclick="copyCode('code2')">Copy</button></pre>

  <p><strong>If activation fails, authorize script execution:</strong></p>
  <pre><code id="code3"># Open PowerShell as Administrator, then run:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned</code><button class="copy-btn" onclick="copyCode('code3')">Copy</button></pre>

  <h3><strong>3. Install Django:</strong></h3>
  <pre><code id="code4">py -m pip install Django</code><button class="copy-btn" onclick="copyCode('code4')">Copy</button></pre>

  <h2><strong>⚙️ Starting the Project</strong></h2>

  <p><strong>Create your Django project:</strong></p>
  <pre><code id="code5">django-admin startproject &lt;project_name&gt;
# Example:
django-admin startproject myfirstdjango</code><button class="copy-btn" onclick="copyCode('code5')">Copy</button></pre>

  <p><strong>Navigate into your project directory:</strong></p>
  <pre><code id="code6">cd &lt;project_name&gt;
# Example:
cd myfirstdjango</code><button class="copy-btn" onclick="copyCode('code6')">Copy</button></pre>

  <p><strong>Run the development server:</strong></p>
  <pre><code id="code7">python manage.py runserver</code><button class="copy-btn" onclick="copyCode('code7')">Copy</button></pre>

  <script>
    function copyCode(id) {
      const code = document.getElementById(id).innerText;
      navigator.clipboard.writeText(code);
      alert("Copied to clipboard!");
    }
  </script>

</body>
</html>
