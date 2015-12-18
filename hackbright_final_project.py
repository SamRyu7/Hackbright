import csv
import matplotlib.pyplot as plt
import pandas as pd  


list1 = []
with open('/users/samantharyu/Desktop/bag_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            list1.append(row) 

bags = pd.DataFrame(list1)

bags = bags.rename(columns = {'TIME bag received Month': 'Bag Received Month', 'TIME bag received Date': 'Bag Received Date', 'BAG id': 'Bag ID', 'Users ID': 'User ID'})

bags['Bag Received Date'] = pd.to_datetime(bags['Bag Received Date'])

bags['Bag Received Month'] = bags['Bag Received Month'].str.replace('-','')

bags1 = bags.sort_values(['Bag Received Month', 'Bag Received Date'], ascending=[1,1])

bags1['Bag Rank'] = bags1.groupby('User ID')['Bag Received Date'].rank(method='first')

# print(bags1.head())            

# get rid of User ID = 1

# print(bags1.dtypes)

bags2 = bags1[bags1['User ID'] != "1"]

# print(bags2.head())

# putting into groups like in Cameran's graph

list2 = []

for row in bags2['Bag Rank']:
	if row == 1:
		list2.append("1st")
	elif row == 2:
		list2.append("2nd")
	elif (row == 3 or row == 4):
		list2.append("3rd/4th")
	elif (row == 5 or row == 6):
		list2.append("5th/6th")
	else:
		list2.append("7th+")		

bags2['Bag Number'] = list2
# print(bags2)

# creating a date range so the graph shows only last 12 complete months

bags3 = bags2[bags2['Bag Received Date'] > '2014-11-01']

bags4 = bags3.groupby(['Bag Received Month','Bag Number'])

bags4.size().unstack().plot(kind='bar', stacked=True)

plt.show()
