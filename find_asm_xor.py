import sys

try:
    fname = sys.argv[1]
except:
    print "Find ASM XORs v1.0 - bbaskin"
    print "Usage : %s <filename>.asm" % sys.argv[0]
    print "Input : .ASM file (from IDA Pro or similar)"
    print "Output: Location of XOR commands in file"
    quit()


data = open(fname, 'r').readlines()
currentsub = ""

for line in data:
	if line.startswith("sub_") or line.startswith("loc_"): currentsub = line
	if "xor" in line:
		items = line.split()
		if items[1].strip(",") != items[2]:
			print currentsub.split()[0] + "\t\t" + line.strip()