

tcA = input("input number of trips: ")


def assignfens():

    global fenList
    c = 0
    fenList = []
    
    while int(c) < int(tcA):
        
        fenList.extend([c,])
        fenList[c] = input("Input fuel economy number: ")
        c += 1 
    
    

assignfens()

print(fenList)

