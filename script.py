interestingindex =[]
f = open('example.csv', 'r')
res = open('res.csv','w')
line = f.readline()
print "res:" +line
line = line.split(";")
interestingindex.append(line.index("data"));
interestingindex.append(line.index("country"));
#print str(interestingindex);
print "====\n";
for lines in f:
	#print lines,
	lines = lines.split(";")
	for a in interestingindex:
		print str(lines[a])+";",
	print "\n"
print "====\n";


