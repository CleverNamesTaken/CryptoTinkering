import requests,base64
from Crypto.Cipher import AES
def XOR_chunk(string,key):
  assert len(string) == len(key)
  cipherText = ''
  for i in range(len(string)):
    XOR = chr(ord(string[i]) ^ ord(key[i]))
    cipherText += XOR
  return (cipherText)
r = requests.get('https://cryptopals.com/static/challenge-data/10.txt')
encrypted=bytearray(r.content).decode('utf-8')
#Create the initialization vector with 16 null bytes
iv='\x00'*16
key = 'YELLOW SUBMARINE'
#Divide the text into the blocks it will use
cipher = AES.new(key, AES.MODE_CBC, iv)
print (cipher.decrypt(encrypted).hex())
blocks = [encrypted[i:i+16] for i in range(0,len(encrypted),16)]

'''
for i in range(len(blocks)):
  if i == 0:
    key = IV
  else:
    key = cipherText 
  XOR_block=XOR_chunk(blocks[i],key)
  cipher = AES.new(key, AES.MODE_ECB)
  cipherText = cipher.decrypt(blocks[i])
  cipher = AES.new(key, AES.MODE_CBC, iv)
  lastBlock = XOR_block 
  print (cipherText.hex())
'''
