import requests, base64,string
def hammingDistance(x,y):
  distance = 0
  for i in range(len(x)):
    bin_c1=ord(x[i])
    bin_c2=ord(y[i])
    xor=bin(bin_c1^bin_c2)
    distance += xor.count('1')
  return (float(distance))

def keySizer(string):
  KEYS={}
  KEYSIZE_Range = range(2,40)
  LikelyKeySize=[]
  # Go through the different key sizes
#  print (string[8:10])
  for KEYSIZE in KEYSIZE_Range:
    dist=[]
    #Get the largest sampling possible
    for i in range(40):
#    for i in range(len(string)//KEYSIZE-9):
      cut1=string[i*KEYSIZE:KEYSIZE*(i+1)]
      cut2=string[KEYSIZE*(i+1):KEYSIZE*(i+2)]
      dist.append(hammingDistance(cut1,cut2)/KEYSIZE)
    distance_average = sum(dist)/len(dist)
    KEYS[KEYSIZE]=distance_average
  # Grab the top 3
  for i in range(3):
    LikelyKeySize.append(min(KEYS,key=KEYS.get))
    KEYS.pop(LikelyKeySize[i])
  print ("Top three most likely key sizes are: {}".format(LikelyKeySize))
  return(LikelyKeySize)

def Blocks(string,listOfSizes):
  KeyDict = {}
  for keySize in listOfSizes:
    key = ''
    #Break the string into blocks of the key length size
#    blocks = [string[i:i+keySize] for i in range(0,len(string)-keySize,keySize)]
#    transposeBlocks(blocks,keySize)
    blocks = [0] * keySize
    for i in range(keySize):
      blocks[i]=string[i::keySize] 
      keyBit=XOR_brute(blocks[i])
      key += keyBit
    KeyDict[keySize]=key
  return(KeyDict)
def XOR_brute(block):
  allChars = string.printable
  highScore = 0
  keyCandidate = ''
  testing = {}
  # Go through each block
  for candidate in allChars:
    XOR_String = ''
    for char in block:
        XOR_String += chr(ord(char)^ord(candidate))
    score=scoreString(XOR_String)
#    print ("Candidate:{} \n String:\n {}".format(candidate,XOR_String))
    testing[candidate]=score
    if score > highScore:
      highScore = score
      keyCandidate = candidate
  return (keyCandidate)

def scoreString(XOR_String):
  common = 'ETASOIN etasoin'
  punctuation= string.punctuation+'\n\t\r'+'\x08\x06\x0c\x1d\x16\x7f\x02\x11\x1f'
  uncommon = "qQZzjJXx"
  score = 0
  for plus in common:
    score += XOR_String.count(plus)*4
  for minus in punctuation:
    score -= XOR_String.count(minus)*3
  for minus in uncommon:
    score -= XOR_String.count(minus)*2

  return (score)
#string1='this is a test'
#string2='wokka wokka!!!'
#print (hammingDistance(string1,string2))
def decodeString(KeyDict,string): 
  highScore= 0
  for keyLength in KeyDict:
    key = KeyDict[keyLength]
    while len(key) < len(string):
      key += key
    decoded = ''
    for i in range(len(string)):
      decodedChar = chr(ord(string[i]) ^ ord(key[i]))
      decoded += decodedChar
    score = scoreString(decoded)
    if score > highScore:
      highScore = score
      decodedMessage = decoded
      solution = KeyDict[keyLength]
  print("The message has been cracked with a keylength of {} as '{}'.  The message is as follows:\n{}".format(len(solution),solution,decodedMessage))


r=requests.get('https://cryptopals.com/static/challenge-data/6.txt')
base64_encoded=r.content
encoded_string_bytes = base64.b64decode(base64_encoded)
encoded_string =bytearray(encoded_string_bytes).decode('utf-8')
KeySizes = keySizer(encoded_string)
KeyDict=Blocks(encoded_string,KeySizes)
decodedMessage=decodeString(KeyDict,encoded_string)
