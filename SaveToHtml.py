import pandas as pd


def create():
	docName = "CS8551U1"
	# docName = input(
	# 	'''ENTER EXAM ID \n 
	# 	[College Code + Dept + Year(Batch) 
	# 	+ Section + Day + Month + Year] \n 
	# 	Ex : 7117CSE3A020321 \n'''
	# 	)

	ExcelName = "Student_Data" # College Code + Exam Name
	# ExcelName = input(
	# 	'''Enter College Code + 
	# 	Exam Name + Subject Short Form \n 
	# 	Ex : 7117IA01AI \n'''
	# 	)

	wb = pd.read_excel('list/{}.xlsx'.format(ExcelName), engine='openpyxl')
	wb.to_html('data/7117/{}.html'.format(docName))
	return docName


print(create())