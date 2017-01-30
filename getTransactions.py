#!/usr/bin/python
import csv
import sys



# Then the big data file is loaded and a country search is performed to each line of csv data
datafile = sys.argv[2]
records=0
with open(datafile, 'rb') as csvfile:
	filereader = csv.reader(csvfile, delimiter="|", quoting=csv.QUOTE_MINIMAL, quotechar='"')
	for row in filereader:
		if len(row) == 10:
			#print(row[9])
			foundit = 0
			#for pattern in patterns:
			for pattern in depurated_patterns:
				#print row[9].strip().find(test_string_to_find)
				#print("Pattern: " + pattern.strip() + " ORIGINAL ROW: " + row[9].strip())
				if pattern.strip() in row[9].strip() and foundit==0:
					#print("Pattern: " + pattern + " ORIGINAL ROW: " + row[9])
					foundit=1
					if pattern.strip() not in pattern_count:
						pattern_count[pattern] = 1
					else:
						pattern_count[pattern] = pattern_count[pattern] + 1
			if foundit == 0:
				nopatter_found.append(row[9])
				nopatter_count = nopatter_count + 1
			foundit = 0
		records = records +1

# Now it is time to write results to text file:
f = open(datafile + ".out", 'w')
f.write("*** ANALYSIS RESULTS ***\n")
f.write("*** TOTAL RECORDS:" + str(records) + " ***\n")
for pattern in patterns:
	if pattern in pattern_count:
		f.write(pattern + "|" + str(pattern_count[pattern]) + "\n")
f.write("\n")			
f.write("*** THERE ARE " + str(nopatter_count) + " PATTERNS NOT FOUND ***\n")		
f.write("\nPATTERNS NOT GROUPED:\n\n")
for row in nopatter_found:
	f.write(row + "\n")
	
f.close()