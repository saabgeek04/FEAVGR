

tc = input("input number of trips: ")


def assignfens():
    global fencount
    global fenList
    fencount = 0
    fenList = []
    
    while int(fencount) < int(tc):
        
        fenList.extend([fencount,])
        fenList[fencount] = input("Input fuel economy number " + str(fencount+1) + ": ")
        fencount += 1 
    


assignfens()

print(fenList)

def calculatefe():

    global lp100k
    lcount = 0
    fensum = 0 
    pfensum = 0

    while int(lcount) < int(tc):
        
        pfensum = fensum

        fensum = fenList[lcount] +  

        print("pfensum: ", pfensum)
        print("fensum: ", fensum)

        lcount += 1 

calculatefe()
    




