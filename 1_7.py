import requests,base64
from Crypto.Cipher import AES
r = requests.get('https://cryptopals.com/static/challenge-data/7.txt')
encrypted=base64.b64decode(bytearray(r.content).decode('utf-8'))

key='YELLOW SUBMARINE'

decipher = AES.new(key, AES.MODE_ECB)
decrypted = decipher.decrypt(encrypted)
decoded = bytearray(decrypted).decode('utf-8')
print (decoded)
