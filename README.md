# pyweb
### I really didn't know a better name :/
## A library to help package python modules into web applications.

```py
from pyweb import build_js

with open("test.html", "w") as f:
    f.write("""
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    {}
    </body>
    </html>""".format(build_js({"example.frontend.index": ["example.frontend.index.Index"]})))
```

Then open `test.html` in your browser.
