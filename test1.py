with open("myfile.csv","r") as f:
	for line in f:
		ab=line.split(",")
		for a in ab:
			if a!="0":
				print a,
		print ""
