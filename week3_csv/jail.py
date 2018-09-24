import csv
# create data aggregation variables
totBlack = 0
totWhite = 0
# open jail census file
file = open('jail.csv', newline='')
reader = csv.DictReader(file)
	for rown in reader:
		print(row)
# read in fiel one line at a time
# retrieving each row as a dict
# examine a row based on values
# for race, increment aggregate counters
# display final values of aggregation vars
