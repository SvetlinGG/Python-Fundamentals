import webbrowser
import os

html_content = """
<!DOCTYPE html>
<html lang="bg">
<head>
    <meta charset="UTF-8">
    <title>Python + HTML</title>
    <style>
        body { font-family: Arial; background: #f0f0f0; padding: 20px; }
        h1 { color: green; }
    </style>
</head>
<body>
    <h1>Това е HTML, генериран от Python!</h1>
    <p>Поздрави от Python скрипта 🚀</p>
</body>
</html>
"""

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Автоматично отваряне в браузър:
webbrowser.open('file://' + os.path.realpath("output.html"))

