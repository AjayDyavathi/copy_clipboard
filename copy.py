import os
import sys
import datetime

try:
    import pyperclip
except:
    import subprocess
    print("trying to install pyperclip...")
    try:
        subprocess.call([sys.executable, "-m", "pip", "install", "pyperclip"])
    except:
        print("failed, please manually install 'pyperclip' and try again!")
        exit()
    import pyperclip
    print("successfully installed and imported")


def getDate():
    now = datetime.datetime.now()
    return str(now.date())


def getTime():
    now = datetime.datetime.now()
    return str(now.time())


dirName = 'CLIPBOARD'
cwd = os.getcwd()
oldCopy = ''
os.mkdir(dirName)
print("recording...")
while True:
    newCopy = pyperclip.paste()
    if newCopy != oldCopy:
        date = getDate()
        if not date+".txt" in os.listdir(dirName):
            with open(dirName+"/"+date+".txt", "w") as f:
                pass
            print("daily file created")
        with open(dirName+"/"+date+".txt", "a") as f:
            f.write("[{}]\t{}\n\n".format(getTime(), newCopy))
            print("[{}]: new copy recorded".format(getTime()))
    oldCopy = newCopy
