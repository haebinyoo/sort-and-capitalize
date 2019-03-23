f = raw_input('Which file do you want?')
file = open(f,'r')
##print file.readlines()
list1 = []
list1 = file.readlines()
print list1
##file = open(f,'w')
##print("1. Sort alphabetically by first name")
##print("2. Sort alphabetically by last name")
##inp = int(input("What would you like to do?"))
##if inp==1:
##        print file.sort()
##        
##elif inp==2:
##        inp = file.write("bob")
##else:
##        print file.write("Invalid")
##               
##file.close()
