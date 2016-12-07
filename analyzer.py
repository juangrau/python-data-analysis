#!/usr/bin/python
import csv
import sys

#MODO DE USO
#./analyzer.py <pattern file name> <data file name>

# first, we open the file with the text patterns to search for
patterns = []
pattern_file = datafile = sys.argv[1]
f = open(pattern_file)
for line in f.readlines():
	line = line.strip()
	patterns.append(line)
#print patterns

# Now lets verify if each pattern could be a substring of another pattern
for line in patterns:
	text = line
	for line2 in patterns:
		text2 = line2
		if text in text2:
			if len(text) < len(text2):
				patterns.remove(text2)

# Finally lets eliminate the duplicates

depurated_patterns = []
for line in patterns:
	if line not in depurated_patterns:
		depurated_patterns.append(line)	

#print("*** DEPURATED PATTERNS ***")
#for line in depurated_patterns:
#	print(line)
#print("*** END OF DEPURATED PATTERNS ***")


# A dictionary is define to store the search results
pattern_count = {}
nopatter_found = []
nopatter_count = 0

# Then the big data file is loaded and a country search is performed to each line of csv data
datafile = sys.argv[2]
records=0
pattern_counter=0
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
					pattern_counter=pattern_counter+1
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
f.write("*** TOTAL RECORDS GROUPED IN PATTERNS:" + str(pattern_counter) + " ***\n")
for pattern in depurated_patterns:
	if pattern in pattern_count:
		f.write(pattern + "|" + str(pattern_count[pattern]) + "\n")
f.write("\n")			
f.write("*** THERE ARE " + str(nopatter_count) + " PATTERNS NOT FOUND ***\n")		
f.write("\nPATTERNS NOT GROUPED:\n\n")
for row in nopatter_found:
	f.write(row + "\n")
	
f.close()


#print pattern_count

