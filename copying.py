import datetime,os,pyperclip

def getDate():
    now = datetime.datetime.now()
    return str(now.date())

def getTime():
    now = datetime.datetime.now()
    return str(now.time())

dirName = '__has_been_copied__'
cwd = os.getcwd()
oldCopy = ''
while True:
    newCopy = pyperclip.paste()
    if newCopy != oldCopy:
        if not dirName in os.listdir():
            os.mkdir(dirName)
        os.chdir(cwd+'/'+dirName)
        if not getDate() in os.listdir():
            os.mkdir(getDate())
        os.chdir(cwd+'/'+dirName+'/'+getDate())
        file = open('copy data.txt','a')
        file.write('\n\n')
        file.write(getTime())
        file.write('\n\n-------------------------\n\n')
        file.write(newCopy)
        file.write('\n\n')
        file.write('!@'*10)
        file.write('\n\n')
        file.close()
    os.chdir(cwd)
    oldCopy = newCopy
