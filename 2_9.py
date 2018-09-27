string="YELLOW SUBMARINE"
paddingLen = 20

while len(string) < paddingLen:
  string += '\x04'

print (len(string))
