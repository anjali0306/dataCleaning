def cleaningFile(t):
    with open(t,'r') as file:
        a=[]
        for line in file:
            if not line.isspace():
                a.append(line)
    return(a)

filewriting=cleaningFile("/home/anjali/pythonpractice/datacleaning/text.txt")
print (filewriting)
filewritinginside=', '.join(filewriting)


file=open("/home/anjali/pythonpractice/datacleaning/InsideFileNew.txt","w")
file.write(filewritinginside)
file.close
