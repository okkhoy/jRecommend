import csv
import sys
#from time import sleep
#from geopy import geocoders
from collections import defaultdict as ddict
from ahoCorasick import *

'''
Some GlobalVariables:
'''
cityCode = {}						# The dict contains latitude & longitude information for each city
cityUser = {}						# This dict contains the number of users in each city used later for probability calc
jobTitles = []

'''
This segment of code reads the zips.csv file which contains the latitude and longitude
information for each city in the USA.
The csv file has the following structure:
zipcode, state abbreviation, latitude, longitude, city, state
cityCode is a python dictionary.
at the end of this section, we get:
cityCode['city'][0] == latitude of the city and 
cityCode['city'][1] == longitude of the city and 
cityCode{} dictionary is used later in the file to map cities to the latitude and longitude.
'''

with open("/media/SHARE/NUS/JobRecoData_ForTesting/zips.csv", "r") as infile:
	reader = csv.reader(infile, delimiter=',', 	quoting=csv.QUOTE_NONE,  quotechar='"', skipinitialspace = True)
	
	# Skip the header line in the input file
	reader.next()
	
	for line in reader:
		(zipCode, stateAbbrv, latitude, longitude, city, state) = line
		latlong=[]
		#print zipCode, stateAbbrv, latitude, longitude, city, state, "\n"
		latlong.append(latitude)
		latlong.append(longitude)
		cityCode[city.lower()] = latlong
		cityUser[city.lower()] = 0					# initializing number of jobs in each city to zero


'''
The following section of the code reads the job titles from jobTitles.txt and stores the values in 
jobTitles list. 
The job_seen is declared as a set. This is to ensure there is no duplication.
'''
job_seen = set()
for line in open("/media/SHARE/NUS/JobRecoData_ForTesting/jobTitles.txt", "r"):
    if line not in job_seen: 														# not a duplicate
        job_seen.add(line)

'''
This super awesome line converts all spaces in the job titles read from the file into underscores.
first list(job_seen) converts the set job_seen to list. Then for... iterates the list. "_".join()
joins the words using the "_" character. w.split() splits each word on the boundary (demarcated 
by space)!
'''
jobTitles = ["_".join(w.split()) for w in list(job_seen)]


trainFile = open("/media/SHARE/NUS/JobRecoData_ForTesting/usersTrain_1.csv", 'wt')
testFile = open("/media/SHARE/NUS/JobRecoData_ForTesting/usersTest_1.csv", 'wt')
junkEntries = open("/media/SHARE/NUS/JobRecoData_ForTesting/usersTest_junkEntries.csv", 'wt')
trainWriter = csv.writer(trainFile)
testWriter = csv.writer(testFile)
junkWriter = csv.writer(junkEntries)

with open("/media/SHARE/NUS/JobRecoData_ForTesting/users.tsv", "r") as infile:
	reader = csv.reader(infile, delimiter="\t", quoting=csv.QUOTE_NONE, quotechar="") # delimiter="\t",

	# Skip the header line in the input file
	reader.next()
	# instantiate the ahoCorasick class. This is used to do the matching. Add all the job titles
	# to the trie
	kwMatch = ahoCorasick()
	kwMatch.addKeyword(jobTitles)
	
	kwMatch.setFailTransitions()
	
	# Write a new header to the output files one for training data, one for test
	trainWriter.writerow(("UserId", "WindowId", "Degree","Major","City", "Latitude", "Longitude", "Experience"))
	testWriter.writerow(("UserId", "WindowId", "Degree","Major","City", "Latitude", "Longitude", "Experience"))
	
	for line in reader:
		(UserId, WindowID, Split, City, State, Country, ZipCode, Degree, Major, GraduationDate, WorkHistoryCount, Experience, CurrentlyEmployed, ManagedOthers, ManagedHowMany) = line

		if City.lower() not in cityCode.keys():
			continue
	
		if WindowID is not  "1":
			print "End of window 1"
			break
			#sys.exit()
		
		#tempMajor = '_'.join(Major.split())
		#jobKeywords = kwMatch.findSubstrings(tempMajor)
		#print jobKeywords, '\n\n'
		#jobReqList = '|'.join(list(jobKeywords)).lower()
		#print Jobid, WindowId, Title.lower(), jobReqList, City.lower(), cityCode[City.lower()][0], cityCode[City.lower()][1], StartDate, EndDate
	
		if Split.strip().lower() == 'train':
			trainWriter.writerow((UserId,WindowID, Degree.lower(), Major.lower(), City.lower(), cityCode[City.lower()][0], cityCode[City.lower()][1], Experience))
		else:
			testWriter.writerow((UserId,WindowID, Degree.lower(), Major.lower(), City.lower(), cityCode[City.lower()][0], cityCode[City.lower()][1], Experience))

		cityUser[City.lower()] = cityUser[City.lower()] + 1 # increment the number of jobs in the particular city
		
'''
now record the city wise number of jobs
'''
print "\n \n Now recording per city users"
op = open("/media/SHARE/NUS/JobRecoData_ForTesting/users_1_perCity.csv", 'wt')
writer = csv.writer(op)
writer.writerow(("City", "NumberOfUsers"))
for key in cityUser.keys():
	writer.writerow( (key,cityUser[key]))



## 7616
