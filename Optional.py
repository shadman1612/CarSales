import csv   
import matplotlib.pyplot as plt

with open('data.csv', mode = 'r') as fileCSV: # Opening the data.csv file
    fCSV = csv.reader(fileCSV)                  # Reading the csv file
    for line in fCSV:
        print(line)                     # Printing file content line by line

f = open(r'C:\Users\User\Desktop\ITM 200\Optional\.vs\stats.txt', 'x')
totalSales = []
f.write("{0}".format(fileCSV.readline().split()))
  
for x in fileCSV:
        x = x.split()
        f.write("{0} = {1}".format(x[0],sum(map(int, x[2:]))))
        totalSales.append(sum(map(int, x[1:])))

fileC = csv.reader(fileCSV, delimiter=',')
sumF21 = sum(map(int, 11[1:6]))
sumF22 = sum(map(int, 12[1:6]))
fileC.close()
salesGrow = (sumF22 - sumF21)/sumF22
f.write(salesGrow)
x = ['Jan', 'Feb', 'Mar', 'Apr', 'item5']
y = totalSales

plt.figure(1)
plt.bar(x,y)

plt.title("Total Sales for each year") # Writing plot title
plt.xlabel("Year")      # Writing x-axis label
plt.ylabel("Total sales")  # Writing y-axis label

plt.show()
f.close()