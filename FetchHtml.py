import bs4 as bs
import urllib.request
import pandas as pd

collegecode = test
# collegecode = input()
# collegecode = input("COLLEGE EXAM ID : ") # 7117CSE3A020321
# source = urllib.request.urlopen(
# 	'https://ramkumarmrj.github.io/ExamModule/data/{}.html'.format(collegecode)
# 	).read()
source = urllib.request.urlopen(
	'https://ramkumarmrj.github.io/ExamModule/{}.html'.format(collegecode)
	).read()


soup = bs.BeautifulSoup(source, features='lxml')
table = soup.find('table', attrs={'class':'dataframe'})
table_rows = table.find_all('tr')


StudentData = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    # print(row)
    StudentData.append(row)
    pd.DataFrame(StudentData, columns=[])
print(StudentData)


register = input("Enter Register Number : ")
DOB = input("Enter Date of Birth : ")
StartTime = "10:00:00"
EndTime = "11:00:00"
ExamDate = "2021-03-12"
inStudentList = [register, DOB, StartTime, EndTime, ExamDate]
currentTime = "10:30:00"
currentDate = "2021-03-12"

if inStudentList in StudentData:
	return "Found"
	print("datefound")
	# # print(StudentData[0])
	# if (currentDate == ExamDate) and (currentTime <= StartTime and EndTime >= currentTime):
	# 	print("Eligible candidate")
	# 	for getLink in StudentData[:-1]:
	# 		print(getLink[0])
else:
	print("no")
	return "no"
