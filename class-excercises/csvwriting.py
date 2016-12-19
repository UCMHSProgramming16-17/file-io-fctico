#csvwriting.py

# import csv
import csv
import math


#open csv file
csvfile = open('triangles.csv', 'w')

#create csv writer
csvwriter = csv.writer(csvfile, delimiter = ',')
#write to file

#a, b, hypotenuse
csvwriter.writerow(['a', 'b', 'hypotenuse'])


#write numbers 1-100 into the first cell
for a in range(1,101):
    #get each possible value of b
    for b in range(a,101):
        #calculate hypotenuse
        hypotenuse = math.sqrt(a**2 + b**2)
        #write a row containing a + b
        csvwriter.writerow([a,b, hypotenuse])
        
        
    #hypotenuse = (1 + (x)**2)**.5
    #csvwriter.writerow([x, ".", 1,x,hypotenuse])




#close file
csvfile.close()