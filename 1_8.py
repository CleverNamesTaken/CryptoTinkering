import requests,base64,codecs
from Crypto.Cipher import AES
#Pull down the list
r = requests.get('https://cryptopals.com/static/challenge-data/8.txt')
#Convert it from a byte array to ascii
hexString = bytearray(r.content).decode('ascii')
#Make it a list by splitting
hexList = hexString.split('\n')
#Decode each component of the list and make a new list
encryptedList = []
for element in hexList:
  encryptedList.append(codecs.decode(element,"hex"))

#Go through each element of the list
matches = {}
for element in encryptedList:
  #Grab every consecutive bytes and look for another two that are similar
  for i in range(len(element)):
    searchString=element[i:i+1]
    #If the particular string is found more than 4 times, add it to the list of possible candidates
    if element.count(searchString) > 4:
      if encryptedList.index(element) not in matches.keys():
        matches[encryptedList.index(element)]=1
      else:
        matches[encryptedList.index(element)]=matches[encryptedList.index(element)]+1
#Print out the line with the most matches 
print ("Most matches found on line {}".format(max(matches,key=matches.get)))
