import os
import json
BASE_DIRECTORY = 'data/'
dicsturt = {}
def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE_DIRECTORY+ archivo))):
        with open(BASE_DIRECTORY + archivo ,"w") as bw:
            json.dump(data,bw,indent=4)

def CreateFile(filename,data):
    with open (BASE_DIRECTORY+filename,'w') as f:
        json.dump(data,f,indent=4)

def ReadFile(file):
    with open(BASE_DIRECTORY+file,'r') as fr:
        return json.load(fr)

def UpdateFile(archivo,data):
    with open(BASE_DIRECTORY+ archivo,'w') as fw:
        json.dump(data,fw,indent=4)
