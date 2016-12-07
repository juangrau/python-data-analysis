#!/usr/bin/python
import csv
import sys


#MODO DE USO
#./analyzer.py <pattern file name> <data file name>

# first, we open the file with the text patterns and append them into a List
patterns = []
i=1
pattern_file = datafile = sys.argv[1]
f = open(pattern_file)
for line in f.readlines():
	line = line.strip()
	patterns.append(line)
	

# Now lets verify if each pattern could be a substring of another pattern
for line in patterns:
	text = line
	for line2 in patterns:
		text2 = line2
		if text in text2:
			if len(text) < len(text2):
				patterns.remove(text2)

# Finally lets eliminate the duplicates

final_patterns = []
for line in patterns:
	if line not in final_patterns:
		final_patterns.append(line)

# now double check patterns to see if there are duplicated patterns
print("Final Patterns\n")
print len(final_patterns)

# Now it is time to write results to text file:
f = open(datafile + ".out", 'w')
for pattern in final_patterns:
	f.write(pattern + "\n")