import tkinter
from tkinter import filedialog
import os
import subprocess

root = tkinter.Tk()
root.withdraw() 

currdir = os.getcwd()
path = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Browse the evtx file')

print(path)
def run(cmd):
    result = subprocess.run(["powershell","-Command",cmd])
    return result

dest = os.path.dirname(path)

cmd1 = r"Get-WinEvent -Path "+path +r"| Export-Csv "+ dest + "/evtxtocsv.csv" 

csvcreation = run(cmd1)
if csvcreation.returncode == 0:
    print("Done!")
else:
    print('error')