def lineCount(file):
    lineCount = 0
    for i in file:
        lineCount += 1
    return lineCount

def readCoords(file) :

    a = file.read(1)
    
    while a != "<" :
        a = file.read(1)

    s = ""
    b = file.read(1)
    while b != ">" :
        s = s + b
        b = file.read(1)

    return s

def checkNewline(name) :
    iFile = open(name,"r")
    lines = iFile.readlines()
    if (lines[-1] == "\n"):
        iFile.close()
        iFile = open(name,"w")
        for line in lines[0:-1]:
            iFile.write(line)
        iFile.close()


fileName = input("Enter a file name :")
checkNewline(fileName)
print(fileName)
iFile = open(fileName,"r")
num = lineCount(iFile)
iFile.close()
iFile = open(fileName,"r")
array = [[],[],[],[],[],[],[],[]]

for i in range(0,num*8):
    array[i%8].append(readCoords(iFile))
iFile.close()
oFile = open(fileName + ".svg", "w")
oFile.write("<svg\n")
oFile.write('\t viewBox="0 0 1000 1000"  >\n')
for i in range(0,num):
    s = ""
    s += "M"
    for j in range(0,8):
        if j==2:
            s+= "C"
        s += array[j][i] + " "
    s += " "
    d = 'd=' + '"' + s + '"'
    oFile.write('\t <path style="fill:#ffffff;stroke:#000000;"' + " " + d + ' />\n')
    
oFile.write("</svg>")
oFile.close()
print("The .svg file is created successfully.")

   





