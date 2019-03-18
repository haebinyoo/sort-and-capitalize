f = raw_input('Which file do you want?')
file = open(f,'r')

print file.read()


d1a = input ("What do you want to do?:\n\
    1)Sort alphabetically by first name\n\
    2)Sort alphabetically by last name\n\
    3)Sort by total length\n\
    4)Reverse the list\n\
    5)Correctly capitalize the list\n\
    [1/2/3/4/5]: ")
if d1a == "1":
    lines = file.readlines()
    lines.sort()
elif d1a == "2":
    print ("You approach the stables.")
elif d1a == "3":
    print ("You approach the stables.")
elif d1a == "4":
    print ("You approach the stables.")
elif d1a == "5":
    print ("You approach the stables.")

        

file.close()

