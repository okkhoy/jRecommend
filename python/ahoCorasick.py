from collections import deque

class State:
	sid = None        ## store the id of state
	value = None      ## stores values of state
	tranList = None    ## used to store the list of next states for transition
	outputSet = None    ## it is set datastructure for storing the outputs at that state
	failState = None

	def __init__(self ,sid, val):
		self.sid = sid
		self.value = val
		self.tranList = []
		self.failState = 0
		self.outputSet = set()

	def getTransition(self, val):
		""" this function gets the next state on input val"""
		for node in self.tranList:
			if node.value == val:
			    return node
		return None


	def testTransition(self, val):
		""" This checks whether there is transition or not on input val"""
		""" for current state, the transition is always true on any input"""

		if self.sid == 0:     
		   return True
		else:
			for nd in self.tranList:
			    if nd.value == val:
			        return True
			return False
	
	def addOutput(self, key):
		"""This adds the key to the output in the state"""
		self.outputSet = self.outputSet ^ key
	
	  
##------------------------------------------------------------------------


class ahoCorasick:
	root = None
	newstate = None

	def __init__(self):
		self.root = State(0, '')
		self.newstate = 0

	def addKeyword(self, keywords):
		"""Adds the keyword in the tree"""

		#for key in keywords.split(' '):
		for key in keywords:
			
			j = 0
			state = 0
			current = self.root
			key = key.upper()

			while j < len(key):
			    ch = key[j]
			    j = j+ 1
			    child = current.getTransition(ch)
			    if child != None:
			        current = child
			    else:
			        self.newstate = self.newstate +1
			        nd = State(self.newstate, ch)
			        current.tranList.append(nd)
			        current = nd
			        while j < len(key):
			            self.newstate = self.newstate +1
			            nd2 = State(self.newstate, key[j])
			            current.tranList.append(nd2)
			            current = nd2
			            j = j+1
			        break
			current.outputSet.add(key)
	
##-------------------------------------------------------------------
	def setFailTransitions(self):
		"""Sets the fail transitions in tree"""
		queue = deque()
		current = self.root
		child = self.root

		for nd in self.root.tranList:
			queue.append(nd)
			nd.failState = self.root

		while len(queue) != 0:
			r = queue.popleft()
			for nd in r.tranList:
			    queue.append(nd)
			    state = r.failState
			    val = nd.value
			    current = state
			    while True:
			        if current.testTransition(val) == False:
			            current = current.failState
			        else:
			            break
			    child = current.getTransition(val)
			    if child == None:
			        nd.failState = current
			    else:
			        nd.failState = child
			nd.addOutput(nd.failState.outputSet)

##--------------------------------------------------------------------------------------------------
	def findSubstrings(self, findStr):
		keywords = set()
		""" Finds all substrings of input which are keywords in the tree"""
		#for string in findStr.split(' '):
		for string in findStr.split(' '):
			string = string.upper()
			#print "Finding substrings in ", string
			current = self.root
			j = 0
	
			while j < len(string):
			    while True:
			        if current.testTransition(string[j]) == False:
			            current = current.failState
			        else:
			            child = current.getTransition(string[j])
	##                      print "before break", child.sid
			            break
			    if child != None:
	##                  print "in none"
			        current = child
			        if len(child.outputSet) != 0:
			            #print j
			            itr = iter(child.outputSet)
			            for keyw in itr:
			            	keywords.add(keyw)
			    j = j + 1    	
		return keywords
			        

##---------------------------------------------------------
	def displayTree(self):
		""" It is used to display the tree of keywords. Prints ID of node and value of node"""
		queue = deque()
		for nd in self.root.tranList:
			queue.append(nd)

		while len(queue) !=0:
			node = queue.popleft()
			for nd in node.tranList:
			    queue.append(nd)
			print node.sid, node.value
	    
	        
	def displayOutput(self):
		""" This function displays the outputs at a state"""
		queue = deque()
		for nd in self.root.tranList:
			queue.append(nd)

		while len(queue) !=0:
			node = queue.popleft()
			for nd in node.tranList:
			    queue.append(nd)
			
			itr = iter(node.outputSet)
			if len(node.outputSet) !=0:
			    print node.sid
			for string in itr:
			    print string

if (__name__ == "__main__"):

	x = ahoCorasick()
	""" Usage: Create object of ahoCorasick
		to enter keywords use addKeyword("string of keywords")
		then call setFailTransitions (fail function)
		to find substrings of string use findSubstrings"""

	regexes = ["computer", "science", "human",  "resource", "security", "engineer"]
	combinedRegex = re.compile('|'.join('(?:{0})'.format(x) for x in regexes))
#	x.addKeyword("computer science")
#	x.addKeyword("human resource")
	x.addKeyword(keywords)
	
	x.setFailTransitions()
	kw = x.findSubstrings('_'.join('TMR, Inc. is an Equal Employment Opportunity Company</p>\r<p>For more job opportunities with TMR, visit our website <a href="http:// \
	 								www.tmrhq.com/">www.tmrhq.com</a></p>\r<p>Send Resumes to HR@tmrhq2.com</p>\r<p>&nbsp;</p>\r<p>JOB SUMMARY:</p>\r<p>&nbsp;</p>\r \
	 								<p>Leads the customer&rsquo;s overall Cyber Security strategy, formalizes service offerings consisted with ITIL best practices, and provides design \
	 								and architecture support.</p>\r<p>&nbsp;</p>\r<ul>\r    <li>Provide security design / architecture support for OJP&rsquo;s IT Security Division (ITSD) \
	 								 </li>\r    <li>Leads the SECOPS team in the day to day OJP Security Operations support&nbsp; </li>\r    <li>Provides direction when needed in a security\
	 								 incident or technical issues </li>\r    <li>Works in concert with network operations on design /integration for best security posture</li>\r    <li>Supports \
	 								 business development functions including Capture Management, Proposal Development and responses, and other initiatives to include conferences, trade \
	 								 shows, webinars, developing white papers and the like.</li>\r    <li>Identifies resources and mentors in-house talent to ensure TMR remains responsive to \
	 								 growing initiatives and contracts with qualified personnel.&nbsp;&nbsp; </li>\r</ul>\r<p>&nbsp;</p>\r<p><a href="https://www.tmrhq.com/ \
	 								 jobapplicationstep1.aspx"><span></span></a>&nbsp;</p>	<p>SKILL SET</p>\r<p>&nbsp;</p>\r<p>Network Security tools:</p>\r<p>&nbsp;</p>\r<p>\
	 								 Webdefend Web Application Firewall (WAF), Cisco Routers, Fortigate 3800 Firewall series, Palo Alto 4000 firewall series, Cisco ASA 5xx Firewall \
	 								 Platform, Cisco&nbsp; FWSM,&nbsp; SourceFire Defense Center, SourceFire IP Sensor Platform, BlueCoat SG Appliance, F5 BigIP(reverse proxy).</p>\
	 								 <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </p>\r<p>Web Application tools:&nbsp; </p>\r<p>&nbsp;</p>\r<p>AppDective, \
	 								 Fortify SCA, HP WebInspect, and the like.</p>\r<p>&nbsp;</p>\r<p>Network Vulnerability tools:&nbsp; </p>\r<p>&nbsp;</p>\r<p>Tenable Security Center, \
	 								 McAfee Foundstone scanner, Cain and Able, L0phtcrack - Password Cracker, Nessus Vulnerability Scanner, NMAP &ndash; Port Scanner, and other \
	 								 scanning and vulnerability mapping tools.&nbsp; </p>\r<p>&nbsp;</p>\r<p>&nbsp;</p>\r<p>DESIRABLE SKILLS:</p>\r<p>&nbsp;</p>\r<p>CISSP and/or \
	 								 related Certifications</p>\r<p>&nbsp;</p>\r<p>EDUCATION AND YEARS OF EXPERIENCE:</p>\r<p>&nbsp;</p>\r<p>BS Computer Science or related \
	 								 discipline; minimum of 8 years in IT Security; minimum 4 years in Senior/Lead position</p>\r<p>&nbsp;</p>\r<p><a href="https://www.tmrhq.com/\
	 								 jobapplicationstep1.aspx">'.split()))
	print kw
	
	kw = x.findSubstrings('_'.join('coordinate, prepare and facilitate requirements gathering sessions. </p>\r<p>Peer review team member requirements for completeness and accuracy. \
	      </p>\r<p>Facilitate requirements prioritization sessions. </p>\r<p>Obtain approval and business sign-off on requirements. </p>\r<p>Integrate with SAP \
	      Roll Out teams to provide Business and Customization Support for SAP warehouse applications and non SAP applications.</p>\r<p>&nbsp;</p>\r<p><b> \
	      What you will Gain:</b> </p>\r<p>Full-time employment <b>&ldquo;direct hire"</b> with a well-established company in a great location! Competitive salary, \
	      excellent benefits &hellip; PTO, insurance package, 401K etc. Relocation is provided. You will be working with a strong group of technical associates in an \
	      excellent work environment for a company that provides stable employment opportunities &hellip; working for one of the Charlotte, NC areas premier \
	      employers. Great Team and work environment!</p>	<p><b>WHAT YOU NEED: </b></p>\r<p>Four year college degree</p>\r<p>Minimum 5 to 8+ years of SAP \
	      experience</p>\r<p>3-5 years experience working with WM SAP module ... need strength in a manufacturing environment converting legacy systems to SAP, \
	      expertise with configurations, implementations, customization support and conditioning techniques.</p>\r<p>2 full life cycle implementations of SAP WM (new \
	      implementations or conversion from legacy applications preferred.</p>\r<p>Experience working in a manufacturing environment</p>\r<p>5 to 8 years of functional \
	      experience</p>\r<p>Strong Microsoft Office skills </p>\r<p>Ability to work with an appropriate sense of urgency and drive for results. </p>\r<p>Must be well \
	      organized with the ability to handle multiple assignments and prioritize appropriately. </p>\r<p><b><br />\r</b>&nbsp;</p>	Charlotte	NC	US	28217	2012-03-\
	      21 02:03:44.137	2012-04-20 23:59:59 7	1	P/T HUMAN RESOURCES ASSISTANT	<b>    <b> P/T HUMAN RESOURCES ASSISTANT')	 								 
