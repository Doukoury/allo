import csv
import statistics
from matplotlib import pyplot as plt
import math
#import numpy as np

def main():
	print('Select the file you want to analyze:\n1. Population Data\n2. Housing Data\n3. Exit the Program')
	sel = input()

	try: # check if user inputs an integer(valid input)
		sel = int(sel)
		
	except ValueError:
		print("Error: Invalid input. Please enter a valid input")
		main()


	if(sel!=1 and sel!=2 and sel!=3):
		print('Error: Invalid input. Please enter a valid input')
		main()

	elif(sel == 3):
		print('Thank you for using this app')
		return

	elif(sel==1):
		print('You have entered Population Data')
		analyzePopData()
		#populationData()
		main()

	else:
		print('You have entered Housing Data')
		analyzeHouseData()
		main()

def analyzePopData():
	print('Select the Column you want to analyze:\na. Pop Apr 1\nb. Pop Jul 1\nc. Change Pop\nd. Exit ')
	
	with open('PopChange.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		PopAprs = []
		PopJuls = []
		changes = []

		next(readCSV)
		for row in readCSV:
			PopApr = int(row[4])
			PopJul = int(row[5])
			change = int(row[6])
			PopAprs.append(PopApr)
			PopJuls.append(PopJul)
			changes.append(change)


	sel_ = input()

	if(sel_=='a'):
		printStats(PopAprs)
		analyzePopData()

	elif(sel_=='b'):
		printStats(PopJuls)
		analyzePopData()

	elif(sel_=='c'):
		printStats(changes)
		analyzePopData()

	elif(sel_=='d'):
		print('You selected to exit\n')
		return

	else:
		print('Error: Invalid input. Please enter a valid input')
		analyzePopData()



def analyzeHouseData():
	print('Select the Column you want to analyze:\na. Age\nb. Bedrooms\nc. Built\nd. Rooms\ne. Utility \nf. exit')
	
	with open('Housing.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		age = []
		bedrooms = []
		built = []
		rooms = []
		utility = []

		next(readCSV)
		for row in readCSV:
			a = int(row[0])
			if(a<0):
				a = 0 #to avoid negative age entries
			b = int(row[1])
			c = int(row[2])
			d = int(row[4])
			e = float(row[6])
			age.append(a)
			bedrooms.append(b)
			built.append(c)
			rooms.append(d)
			utility.append(e)


	sel_ = input()

	if(sel_=='a'):
		printStats(age)
		analyzeHouseData()

	elif(sel_=='b'):
		printStats(bedrooms)
		analyzeHouseData()

	elif(sel_=='c'):
		printStats(built)
		analyzeHouseData()

	elif(sel_=='d'):
		printStats(rooms)
		analyzeHouseData()

	elif(sel_=='e'):
		printStats(utility)
		analyzeHouseData()

	elif(sel_=='f'):
		print('You selected to exit\n')
		return

	else:
		print('Error: Invalid input. Please enter a valid input')
		analyzePopData()


def printStats(lst):
	print('The statistics of the column are:')
	print('Count = ',len(lst))
	print('Mean = ', statistics.mean(lst))
	print('Standard Deviation = ',statistics.stdev(lst))
	print('Min = ', min(lst))
	print('Max = ',max(lst))

	#bins = np.linspace(math.ceil(min(lst)),math.floor(max(lst)),20)

	#plt.xlim([min(lst)/10, max(lst)/10 +1])
	plt.hist(lst, bins='auto', alpha=0.5)
	plt.title('Histogram analysis')
	plt.xlabel('Data Bins')
	plt.ylabel('Count')
	#plt.show()
	plt.savefig("hist.jpg")

	print('\n\n')

print('*********** Welcome to the Python Data Analysis App********** ')
main()
