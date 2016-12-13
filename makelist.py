file = open('makelist.txt','w')
for n in range(10):
    file.write(str(n+1) + ". " + input("What would you like to add to the list?") + '\n')  
    
file.close()