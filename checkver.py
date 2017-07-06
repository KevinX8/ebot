oldver = float(sys.argv[1])
newver = float(sys.argv[2])

def checkver():
	global oldver, newver
	
	if newver > oldver:
		return True
		
if checkver() == True:
	isnew = open("isnew", "w")
	
	isnew.write("True")
	
	isnew.close()
