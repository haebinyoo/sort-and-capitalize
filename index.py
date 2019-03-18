f = raw_input('Which file do you want?')
file = open(f,'r')

print file.read()

options = input ("What do you want to do?:\n\
    1)Sort alphabetically by first name\n\
    2)Sort alphabetically by last name\n\
    3)Sort by the total length\n\
    4)Reverse the list\n\
    5)Correctly capitalize the list\n\
    [1/2/3/4/5]: ")
if options == "1":
    for line in f:
        line = line.sort()
        print(f)
elif options == "2":
    print ("You approach the stables.")
elif options == "3":
    print ("You approach the stables.")
elif options == "4":
    print ("You approach the stables.")
elif options == "5":
    print ("You approach the stables.")


file.close()

 


