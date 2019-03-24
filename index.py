f = raw_input('Which file do you want?')
file = open(f,'r')
list1 = []
list1 = file.readlines()
list1 = [x.strip() for x in list1]
list1 = [x.title() for x in list1]
print list1
file = open(f,'w')
print("1. Sort alphabetically by first name")
print("2. Sort alphabetically by last name")
print("3. Sort by the total lenght")
print("4. Reverse the list")
print("5. Capitalize the list")

inp = int(input("What would you like to do?"))
if inp==1:
        list1.sort()
        print list1
        [file.write(x + '\n') for x in list1]
elif inp==2:
        list1.sort(key=lambda x: x.split(" ")[-1].lower()) 
        [file.write(x + '\n') for x in list1]
##elif inp==3:
##        [file.write(x + '\n') for x in list1]
##elif inp==4:
##        [file.write(x + '\n') for x in list1]
##elif inp==5:
##        [file.write(x + '\n') for x in list1]
        
else:
        print file.write("Invalid Request Enter 1-5")
               
file.close()
