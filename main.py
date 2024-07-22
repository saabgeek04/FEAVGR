print("Welcome, please input numbers only")
rfenA = input("input number a: ")
rfenB = input("input number b: ")
rfenC = input("input number c: ")

fenA = int(rfenA)
fenB = int(rfenB)
fenC = int(rfenC)

AVGfen = (fenA + fenB + fenC) // 3

print(str(AVGfen) + str("L/100Km"))

# Convert to MPG

AVGmpg = round(235.215 // AVGfen)


print(str(AVGmpg) + str("mpg"))

# Next step: compare multiple groups of fuel economy data to each other

# end goal: have a flexible amount of groups and items, maybe web server?
