interestingindex =[]
f = open('example.csv', 'r')
res = open('res.csv','w')
line = f.readline()

tmp=line.split(";")
print "res:" +line
line = line.split(";")
interestingindex.append(line.index("data"));
interestingindex.append(line.index("country"));

#First line case, the header
for a in interestingindex:
	if tmp[a] == 'data':
		print "OMGOMG"
		if a != interestingindex[-1]:
			result="datav2"+";"
		else:
			result="datav2"
	elif tmp[a] == 'country':
		if a != interestingindex[-1]:
			result="countryv2"+";"
		else:
			result="countryv2"
	else:
		if a != interestingindex[-1]:
			result=tmp[a]+";"
		else:
			result=tmp[a]
	res.write(result)
res.write("\n")
print "====\n";

#The other lines, the data, not the header
for lines in f:
	#print lines,
	lines = lines.split(";")
	for a in interestingindex:
		if a != interestingindex[-1]:
			temp = lines[a]+";"
		else:
			temp = lines[a]
		res.write(temp)
		print str(lines[a])+";",
	res.write("\n");
	print "\n"
print "====\n";


