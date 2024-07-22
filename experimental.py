

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
    

def calculatefe():

    global lp100k
    global mpg
    lcount = 0
    fensum = 0 
    pfensum = 0

    while int(lcount) < int(tc):
        
        pfensum = fensum

        fensum = int(fenList[lcount]) + int(pfensum)

        lcount += 1
    
    lp100k = int(fensum) // int(tc) 

    mpg = round(235.215 // lp100k)  


assignfens()
calculatefe()

print("Your fuel economy averages are...")
print(lp100k, "L/100km")
print(mpg, "mpg")




