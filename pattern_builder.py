#!/usr/bin/python

import csv
import sys

# MODO DE USO
# ./pattern_builder.py <data file name>


# Then the data file is loaded as the first parameter in the command line
datafile = sys.argv[1]
firsTime = True
words = []
tmp = []
all_texts = []



with open(datafile, 'r') as csvfile:
    filereader = csv.reader(csvfile, delimiter="|", quoting=csv.QUOTE_MINIMAL, quotechar='"')

    for row in filereader:

        if len(row) == 10:
            words = row[9].split()
            numWords = len(words)

            if firsTime:
                tmp = [1, row[9]]
                all_texts.append(tmp)
                firsTime = False
            else:
                # print(words[0])
                # print(numWords)
                tmp = [1, row[9]]
                                
                #print("row[9]: " + str(numWords) + " " + row[9]) 
                for element in all_texts:                    
                    match_words = 0
                    existing_pattern = False
                    element_words = element[1].split()
                    element_numWords = len(element_words)
                    #print("element: " + str(element_numWords) + " " + element[1])
                    if numWords > element_numWords:
                        max = element_numWords
                    else:
                        max = numWords
                    #print("Texto a analizar: " + str(row[9]))
                    #print("Texto para comparar: " + str(element))
                    for i in range(0, max-1):
                        if words[i] == element_words[i]:
                            match_words += 1
                    #print("Match words:" + str(match_words) + " Porcentaje:" + str(100 * (float(match_words)/float(max))))
                    if float(match_words) / float(max) > 0.5:
                        existing_pattern = True
                        element[0] += 1
                        break                    
                if not existing_pattern:
                    all_texts.append(tmp)
                    #print("Agregada\n\n")
                #else:
                    #print("Ya existe patron\n\n")


    print("\n\n*** Resultado ***\n\n")
    for element in all_texts:
        print(str(element[0]) + "|" + str(element[1]))