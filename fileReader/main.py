def readFile(fileSrc):
    f = open(fileSrc, 'r')

    lines = f.readlines()
    for line in lines:
        line = line.strip()
    
    f.close()

    return line