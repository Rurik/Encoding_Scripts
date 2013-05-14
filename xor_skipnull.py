import sys

def xor_skipnull(data, xor):
    result = ""
    for i in range(0,len(data)):
        char = data[i]
        if char != "\x00" and char != xor: 
            char = chr(ord(char) ^ ord(xor))
        result += char
    return result

if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print "XOR Skip Null. Version 1.1 - @bbaskin"
        print "Usage: xor_skipnull.py <file> <hex key>"
        print "Input : Raw Data File, hex value"
        print "Output: Data file with each byte XOR'd by key, skipping nulls"
        quit()

    filename = sys.argv[1]
    xor = chr(int(sys.argv[2],16))
    print "Using XOR 0x%s" % xor.encode("hex")
    if len(xor) != 1: 
        print "Invalid XOR key"
        quit()

    data = open(filename, "rb").read()
    print "%d bytes read" % len(data)
    out = open(filename+".dec", "wb")
    newdata = xor_skipnull(data, xor)
    out.write(newdata)
    out.close()
