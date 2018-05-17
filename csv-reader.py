import csv
with open('C:\Users\chmamai\Documents\logging-example\my.csv', 'r+', newline='') as csv_file:
	reader = csv.reader(csv_file)
	for row in reader:
		print(str(row))
