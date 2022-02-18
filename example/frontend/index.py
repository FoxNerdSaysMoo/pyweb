
class Index:
    def __init__(self, js):
        self.js = js
        self.onload()

    def onload(self):
        self.js.window.document.body.innerHTML = '<h1>Hello World!</h1>'
