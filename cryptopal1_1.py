string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

print string.decode("hex").encode("base64")
#Source: https://stackoverflow.com/questions/33704327/hex-to-base64-conversion-in-python
