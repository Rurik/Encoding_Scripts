import win32clipboard as w
import tempfile, os

def ReadClipboard():
    w.OpenClipboard()
    result = w.GetClipboardData(w.CF_TEXT)
    w.CloseClipboard()
    return result

def ParseData(data, type):
    result = ""
    for line in data.split("\n"):
        try:
            if len(line.split("  ")[0]) != 8: continue
        except:
            raise
        if line.startswith("Offset"): continue
        items = line.split("   ")
        print items
        if type == 1:
            result += (items[type].strip() + " ").replace("  ", " ")
        else:
            newresult = ""
            newresult += (items[type].strip()).replace("  ", " ")
            if newresult: 
                result += newresult
            else:
                result += (items[-1].strip()).replace("  ", " ")
    return result

print "Winhex to ASCII v1.0 - @bbaskin"
print "Copy Winhex 'Editor Display' output to clipboard and run"
print "Result will be just the hex and just the ASCII portions"
print "If there's an error, then you copied the wrong data"
print "\n\n"
    
data = ReadClipboard()   
hex = ParseData(data, 1)
ascii = ParseData(data, 2)
print hex
print ascii

(tempfd, temppath) = tempfile.mkstemp()
temphandle = os.fdopen(tempfd, 'w')
temphandle.write("ASCII:\n")
temphandle.write(ascii)
temphandle.write("\n\n\nHex:\n")
temphandle.write(hex)
print "*** Writing data to %s" % temppath
temphandle.close()
os.system("write.exe \"%s\"" % temppath)

