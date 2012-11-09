import csv
#from time import sleep
#from geopy import geocoders
from collections import defaultdict as ddict

'''
reader = csv.DictReader(open("/media/SHARE/NUS/JobRecoData_ForTesting/zips.csv", "rb"), skipinitialspace=True)

for row in reader:
	print row

'''
cityCode = {}
with open("/media/SHARE/NUS/JobRecoData_ForTesting/zips.csv", "r") as infile:
	reader = csv.reader(infile, delimiter=',', 	quoting=csv.QUOTE_NONE,  quotechar='"', skipinitialspace = True)
	
	for line in reader:
		(zipCode, stateAbbrv, latitude, longitude, city, state) = line
		latlong=[]
		#print zipCode, stateAbbrv, latitude, longitude, city, state, "\n"
		latlong.append(latitude)
		latlong.append(longitude)
		cityCode[city.lower()]= latlong
	


	

