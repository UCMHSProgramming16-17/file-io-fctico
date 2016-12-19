file = open('makelist.txt','w') #creates file makelist.txt to write in
for n in range(10): #creates for loop
    file.write(str(n+1) + ". " + input("What would you like to add to the list?") + '\n')  #allows the user to input 10 things, each on new lines with a numbered list
    
file.close() #closes the file