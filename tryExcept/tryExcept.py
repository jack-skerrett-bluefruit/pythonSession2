import sys

reference = open(sys.argv[1], "r")
log = open(sys.argv[2], "r")
output = open("output.txt", "w+")
i = 0 
x = 0

referenceList = reference.read().split("</CD>")
logList = log.read().split("</CD>")

for CD in referenceList:
    referenceListProperties = referenceList[i].split("</")
    logListProperties = logList[i].split("</")
    for item in referenceListProperties:
        if referenceListProperties[x] != logListProperties[x]:
            output.write("Entry " + str(i) + " - Section " + str(x) + ": " + logListProperties[x].split(">")[2] + " should be " + referenceListProperties[x].split(">")[2] + "\n")
        x += 1
    i += 1    
    x = 0

reference.close()
log.close()
output.close()
