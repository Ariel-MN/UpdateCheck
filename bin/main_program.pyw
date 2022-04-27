from delphivcl import *
import os
import sys

# Current version
__version__ = "v.1.0.0"

class MainForm(Form):

    def __init__(self, owner):
        self.Caption = "Main Form"
        self.SetBounds(10, 10, 300, 300)
        self.Position = "poScreenCenter"

        self.btnUpdate = Button(self)
        self.btnUpdate.SetProps(Parent=self, 
            Caption="Check for updates")
        self.btnUpdate.SetBounds(70, 100, 150, 24)
        self.btnUpdate.OnClick = self.__check_for_updates

        self.OnClose = self.__on_form_close

    def __on_form_close(self, sender, action):
        action.Value = caFree
    
    def __check_for_updates(self, sender):
        try:
            # Flush buffer
            sys.stdout.flush()
        finally:
            # Kill process and start update
            os.execl(sys.executable, "../lib/pythonw.exe", "update_check.pyw", __version__)

def main():
    Application.Initialize()
    Application.Title = "Main program"
    Main = MainForm(Application)
    Main.Show()
    FreeConsole()
    Application.Run()
    Main.Destroy()

main()