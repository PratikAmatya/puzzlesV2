numberOfRows=0
file=open('csv-sample.csv')
 
for row in file:
    numberOfRows+=1

print(numberOfRows)
