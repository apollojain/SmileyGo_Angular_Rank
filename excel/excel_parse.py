import xlrd
import re
from math import *
def is_yes(res):
	if res=='Y' or res=='y' or res =='Yes' or res == 'yes':
		return 1
	else:
		return 0

def image_find(brand):
	keyword = brand.replace(' ', '-').lower()
	return 'http://cf.juggle-images.com/matte/white/280x280/' + keyword + '-logo-primary.jpg'

non_decimal = re.compile(r'[^\d.]+')
file_location = "SmileyGo_Rankings.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
total = '[\n \n'
for row in range(1, sheet.nrows):
	counter = 1
	if(str(sheet.cell_value(row, 5)) != 'unknown'):
		total += '{'
		total = total + "name: '" + str(sheet.cell_value(row, 0)) + "', \n"
		total = total + "revenue: '$" + str(int(sheet.cell_value(row, 3))) + ".00', \n"
		total = total + "social_spending: '$" + str(int(sheet.cell_value(row, 4))) + ".00', \n"
		total = total + "url: '" + image_find(str(sheet.cell_value(row, 0))) + "', \n"
		charity_types = is_yes(sheet.cell_value(row, 7)) + is_yes(sheet.cell_value(row, 8)) + is_yes(sheet.cell_value(row, 9)) + is_yes(sheet.cell_value(row, 10)) + is_yes(sheet.cell_value(row, 11)) + is_yes(sheet.cell_value(row, 12))
		# my_score = str(float(log(float(non_decimal.sub('', sheet.cell_value(row, 3))), 10)/log(10))*float(1000*float(sheet.cell_value(row, 5)))*charity_types)
		# a1 = log(sheet.cell_value(row, 3)[1:])/log(10))
		a1 = float(log(int(sheet.cell_value(row, 3)))/log(10))
		a2 = 1000*float(sheet.cell_value(row, 5))
		my_score = str(int(a1 + a2 + charity_types) + 1)
		if(row == sheet.nrows - 2):
			total = total + "score: " + str(my_score) + "} \n \n"
		else:
			total = total + "score: " + str(my_score) + "} , \n \n"
		counter+=1
		if(counter == 26):
			break
total = total + ']'
text_file = open("results.txt", "w")
text_file.write(total)
text_file.close()


