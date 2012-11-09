import csv
import re
from collections import defaultdict as ddict

jobDesc = set() # holds lines already seen

for line in open("jobTitles.txt", "r"):
    if line not in jobDesc: # not a duplicate
        jobDesc.add(line.rstrip())
        
jobDesc = list(jobDesc)


words = '|'.join(jobDesc)
print words


#combinedRegex = re.compile('|'.join('(?:{0})'.format(x) for x in jobDesc))
combinedRegex = re.compile(r'\b(?:%s)\b' % '|'.join(jobDesc))
'''
jobReq = {}

with open("/media/SHARE/NUS/JobRecoData/jobs1.tsv", "r") as infile:
	reader = csv.reader(infile, delimiter="\t", 	quoting=csv.QUOTE_NONE, quotechar="")
	# Skip the header line in the input file
	reader.next()

	# Write a new header to the output file
	#writer.writerow(("JobId", "WindowId", "Title","City", "Latitude", "Longitude", "StartDate", "EndDate"))
	
	for line in reader:
		(Jobid, WindowId, Title, Description, Requirements, City, State, Country, Zip5, StartDate, EndDate) = line
		jobReq[Jobid] = combinedRegex.findall(Description)
		print jobReq[Jobid]
		
'''
		
'''
		if City.lower() not in cityCode.keys():
			continue
		
		print Jobid, WindowId, Title.lower(), cityCode[City.lower()][0], cityCode[City.lower()][1], StartDate, EndDate
		writer.writerow( (Jobid, WindowId, Title.lower(), City.lower(), cityCode[City.lower()][0], cityCode[City.lower()][1], StartDate, EndDate))
		cityJobs[City.lower()] = cityJobs[City.lower()] + 1 # increment the number of jobs in the particular city
'''
		
