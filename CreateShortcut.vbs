Set objshell = WScript.CreateObject("WScript.Shell")
CurDir = objshell.CurrentDirectory
Quote = """"
Set Link = objshell.CreateShortcut(".\UpgradeManager.lnk")
    Link.TargetPath = CurDir+".\lib\pythonw.exe"
    Link.Arguments = Quote+CurDir+"\bin\main_program.pyw"+Quote
    Link.IconLocation = CurDir+"\etc\multi-res.ico"
    Link.Description = "Upgrade Manager"
    Link.WorkingDirectory = CurDir+"\bin\"
    Link.Save