import  matplotlib.pyplot as plt
import csv
x = []
y = []
with open('weatherdata.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(row[1])
plt.xticks(rotation=25)
plt.plot(x, y,color='r', marker='o', linestyle='dashed')
plt.xlabel("Date")
plt.ylabel("Temparature")
plt.title("Weather data")
plt.grid()
plt.show()


