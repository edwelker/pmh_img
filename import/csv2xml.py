import csv

names = ['NIA', 'NIAMS', 'NIDDK', 'NHGRI', 'NIGMS']

for name in names:
    csvFile = 'csv/' + name + '.csv'
    xmlFile = name + '.xml'

    csvData = csv.reader(open(csvFile))
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    xmlData.write('<' + name + '>' + "\n")

    rowNum = 0

    for row in csvData:
        if rowNum == 0:
            tags = row
    # replace spaces w/ underscores in tag names
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
        else: 
            xmlData.write('<row>' + "\n")
            for i in range(len(tags)):
                xmlData.write('    ' + '<' + tags[i] + '>' \
                                + row[i].encode("UTF-8") + '</' + tags[i] + '>' + "\n")
            xmlData.write('</row>' + "\n")

        rowNum +=1

    xmlData.write('</' + name + '>' + "\n")
    xmlData.close()
