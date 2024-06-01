from delphivcl import *
import os
import sys

# Current version
__version__ = "v1.0.2"

# Path of the main script
ScriptPath = os.path.realpath(__file__)

# Program directory
AppPath = os.path.dirname(__file__)  

class MainForm(Form):

    def __init__(self, owner):
        self.Caption = f"{Application.Title} - {__version__}"
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
            os.execl(sys.executable, os.path.join(AppPath,'..','lib/pythonw.exe'), os.path.join(AppPath,'update_check.pyw'), __version__, ScriptPath)

def main():
    Application.Initialize()
    Application.Title = "Sample App"
    Main = MainForm(Application)
    Main.Show()
    FreeConsole()
    Application.Run()
    Main.Destroy()

main()
