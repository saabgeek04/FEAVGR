




def assignfens():

    global unittpye
    unittype = 0

    print("[1] L/100km")
    print("[2] km/L")
    print("[3] mpg (UK)")
    print("[4] mpg (US)")

    fentype = input("Select the number corresponding to the unit you would like: ")

    while unittype == 0:

        if fentype == "1":
            print("You have Selected L/100km")
            unittype = 1 

        elif fentype == "2":
            print("You have selected km/L")
            unittype = 2 

        elif fentype == "3":
            print("You have selected mpg (UK)")
            unittpye = 3

        elif fentype == "4":
            print("You have selected mpg (US)")
            unittpye = 4 

        else:
            print("Invalid Input, Try again")
            assignfens()

        


    global tc
    tc = input("input number of trips: ")

    
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


# Next step: compare multiple groups of fuel economy data to each other

# end goal: have a flexible amount of groups and items, maybe web server?
