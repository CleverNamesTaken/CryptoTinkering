#string = bytearray(raw_input('Input the hex string you want converted. \n>>>'))

string = '1c0111001f010100061a024b53535009181c'

#Change the string into binary
binary1 = bin(int(string,16))

#string2 = bytearray(raw_input('And what will we add to that string? \n>>>'))
string2 = '686974207468652062756c6c277320657965'

#change the string into binary
binary2 = bin(int(string2,16))

#XOR the two strings (after converting them into binary again).
answer = hex(int(binary1,2) ^ int(binary2,2))
print(answer)