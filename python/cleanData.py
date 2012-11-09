import csv
#from time import sleep
#from geopy import geocoders
from collections import defaultdict as ddict


'''
Some GlobalVariables:
'''
cityCode = {}						# The dict contains latitude & longitude information for each city
cityJobs = {}						# This dict contains the number of jobs in each city used later for probability calc

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
		cityJobs[city.lower()] = 0					# initializing number of jobs in each city to zero



op = open("/media/SHARE/NUS/JobRecoData_ForTesting/jobs_1.csv", 'wt')
writer = csv.writer(op)

with open("/media/SHARE/NUS/JobRecoData/jobs1.tsv", "r") as infile:
	reader = csv.reader(infile, delimiter="\t", 	quoting=csv.QUOTE_NONE, quotechar="")
	# Skip the header line in the input file
	reader.next()

	# Write a new header to the output file
	writer.writerow(("JobId", "WindowId", "Title","City", "Latitude", "Longitude", "StartDate", "EndDate"))
	
	for line in reader:
		(Jobid, WindowId, Title, Description, Requirements, City, State, Country, Zip5, StartDate, EndDate) = line
		if City.lower() not in cityCode.keys():
			continue
		#print Jobid, WindowId, Title.lower(), cityCode[City.lower()][0], cityCode[City.lower()][1], StartDate, EndDate
		#writer.writerow( (Jobid, WindowId, Title.lower(), City.lower(), cityCode[City.lower()][0], cityCode[City.lower()][1], StartDate, EndDate))
		cityJobs[City.lower()] = cityJobs[City.lower()] + 1 # increment the number of jobs in the particular city
		
		
		
'''
now record the city wise number of jobs
'''

op = open("/media/SHARE/NUS/JobRecoData_ForTesting/jobs_1_perCity.csv", 'wt')
writer = csv.writer(op)
writer.writerow(("City", "NumberOfJobs"))
for key in sort(cityJobs.keys()):
	writer.writerow( (key,cityJobs[key]))


#-------------------------------------------


'''		
op = open("/media/SHARE/NUS/JobRecoData_ForTesting/jobs_4.csv", 'wt')
writer = csv.writer(op)

with open("/media/SHARE/NUS/JobRecoData/jobs4.tsv", "r") as infile:
	reader = csv.reader(infile, delimiter="\t", 	quoting=csv.QUOTE_NONE, quotechar="")
	#reader.next() 

	for line in reader:
		(Jobid, WindowId, Title, Description, Requirements, City, State, Country, Zip5, StartDate, EndDate) = line
		print Jobid, WindowId, Title.lower(), City.lower(), State.lower(), Country.lower(), Zip5, StartDate, EndDate
		writer.writerow( (Jobid, WindowId, Title.lower(), City.lower(), State.lower(), Country.lower(), Zip5, StartDate, EndDate))
		
#--------------------------------------------

op = open("/media/SHARE/NUS/JobRecoData_ForTesting/jobs_5.csv", 'wt')
writer = csv.writer(op)

with open("/media/SHARE/NUS/JobRecoData/jobs5.tsv", "r") as infile:
	reader = csv.reader(infile, delimiter="\t", 	quoting=csv.QUOTE_NONE, quotechar="")
	#reader.next() 

	for line in reader:
		(Jobid, WindowId, Title, Description, Requirements, City, State, Country, Zip5, StartDate, EndDate) = line
		print Jobid, WindowId, Title.lower(), City.lower(), State.lower(), Country.lower(), Zip5, StartDate, EndDate
		writer.writerow( (Jobid, WindowId, Title.lower(), City.lower(), State.lower(), Country.lower(), Zip5, StartDate, EndDate))
		
#----------------------------------------------

op = open("/media/SHARE/NUS/JobRecoData_ForTesting/jobs_6.csv", 'wt')
writer = csv.writer(op)

with open("/media/SHARE/NUS/JobRecoData/jobs6.tsv", "r") as infile:
	reader = csv.reader(infile, delimiter="\t", 	quoting=csv.QUOTE_NONE, quotechar="")
	#reader.next() 

	for line in reader:
		(Jobid, WindowId, Title, Description, Requirements, City, State, Country, Zip5, StartDate, EndDate) = line
		print Jobid, WindowId, Title.lower(), City.lower(), State.lower(), Country.lower(), Zip5, StartDate, EndDate
		writer.writerow( (Jobid, WindowId, Title.lower(), City.lower(), State.lower(), Country.lower(), Zip5, StartDate, EndDate))
		
#-------------------------------------------------

op = open("/media/SHARE/NUS/JobRecoData_ForTesting/jobs_7.csv", 'wt')
writer = csv.writer(op)

with open("/media/SHARE/NUS/JobRecoData/jobs7.tsv", "r") as infile:
	reader = csv.reader(infile, delimiter="\t", 	quoting=csv.QUOTE_NONE, quotechar="")
	#reader.next() 

	for line in reader:
		(Jobid, WindowId, Title, Description, Requirements, City, State, Country, Zip5, StartDate, EndDate) = line
		print Jobid, WindowId, Title.lower(), City.lower(), State.lower(), Country.lower(), Zip5, StartDate, EndDate
		writer.writerow( (Jobid, WindowId, Title.lower(), City.lower(), State.lower(), Country.lower(), Zip5, StartDate, EndDate))
		
#------------------------------------------------

with open("jobs1.tsv", "r") as infile:
	reader = csv.reader(infile, delimiter="\t", 	quoting=csv.QUOTE_NONE, quotechar="")
	reader.next() 
	geoCoder = geocoders.GeoNames()
	
	for line in reader:
		(Jobid, WindowId, Title, Description, Requirements, City, State, Country, Zip5, StartDate, EndDate) = line
		print Jobid, City,State, 
		if Zip5 == '':
			print  " not lat", "no long!"
		else:
			pl = City + ' ' + State + ' ' + Zip5
			place, (latitude,longitude) = geoCoder.geocode(pl)
			print latitude, longitude
'''					
