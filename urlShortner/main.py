import shortlink
from remi import start,App,gui
class main (App):
    def __init__(self,*args):
        super(main,self).__init__(*args)
    def main(self):
        layout=gui.Container()
        self.URL=gui.TextInput(True,"long link")
        layout.append(self.URL)
        self.short=gui.Button("short")
        self.short.onclick.do(self.on_short)
        layout.append(self.short)
        self.result=gui.Label("result")
        layout.append(self.result)
        return layout
    def on_short(self,event):
        URL=shortlink.short(self.URL.get_value())
        self.result.set_text(URL)
start(main,title="url shortner")