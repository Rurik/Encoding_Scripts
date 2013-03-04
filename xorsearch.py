import binascii
import sys

def XORdata (filename, xor):
    file = open (filename, "rb")
    byte = file.read(1)
    newdata = ""
    while byte != "":
        newdata += chr(ord(byte) ^ xor)
        if option == "-a":
                if ((ord(byte) ^ xor) > 127) or ((ord(byte) ^ xor < 32)):
                    return null
        byte = file.read(1)
    file.close()
    return newdata



try:
    fn = sys.argv[1]
except:
    print "Simple XOR key search v1.0 - @bbaskin"
    print "Specify file with binary data to XOR"
    print sys.argv[0] + " <filename> [-a]"
    print "-a will avoid printing unprintable characters"
    quit()

try:
    option = sys.argv[2]
except:
    option = "z"

for xor in range (1,255,1):
    result = XORdata(fn, xor)
    if result:
        print "%s : %s" % (hex(xor), result)
            
