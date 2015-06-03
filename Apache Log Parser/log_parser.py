import re

fp = open("weblog.txt")
j = []

for i in fp:
	exp = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+ *\d+)* "(.*?)" "(.*?)"'
	s = re.match(exp,i)
	if s == None:
		exp = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+ *\d+)* - "(.*?)" "(.*?)"'
		s = re.match(exp,i)
	
	print "\n"
	print "IP 	\t:" + s.group(1)
	print "Timestamp\t:" + s.group(2)

	k = s.group(3)
	j = k.split()

	print "Method	\t:" + j[0]
	print "URL	\t:" + j[1]
	print "Version	\t:" + j[2]

	k = s.group(4)
	j = k.split()

	if len(j) == 2:
		print "Status Code\t:" + j[0]
		print "Object Size\t:" + j[1]
	else:
		print "Status Code\t:" + j[0]

	print "Referer	\t:" + s.group(5)
	print "User-agent\t:" + s.group(6)