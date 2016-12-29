import sys
file_grammer = sys.argv[1]
file_sent = sys.argv[2]

#======================================READ=========================================
with open(file_grammer) as document:
    first=[]
    maingram = {}
    for line in document:
        line = line.split()
        del line[1]
        first.append(line[1:])
        second=line[0]
        if second in maingram:
            maingram[second].append(line[1:])
        else:
            maingram[second]=[line[1:]]

#=================================READ SENTENCES================================
test_sent = []
with open(file_sent) as my_file:
    for line in my_file:
        #line=line.lower()
        line = line.split()
        test_sent.append(line)
"""for i in test_sent:
    print (i)"""

#===================================FUNCTION====================================

for sentence in test_sent:
    final_chart=[]
    chart=[[[] for j in range(len(sentence))] for k in range(len(sentence))]
    #print len(chart[0])
    #print len(chart[0])
    for c in range(len(sentence)):
        for k in maingram:
            if [sentence[c]] in maingram[k]:
                chart[c][c].append(k)
        #print chart[c][c]
        row=c-1
        while(row>-1):
            for s in range(row+1,c+1):
                #print s,row,c
                B=chart[row][s-1]
                C=chart[s][c]
                #print B,"_________"
                #print C,"_________@@"
                mapper=[[item,val] for item in B for val in C]
                #print mapper
                for k in maingram:
                    for item in mapper:
                        if item in maingram[k]:
                            chart[row][c].append(k)
                #print chart,"@@@@@@@@@"
        
            row-=1
    #print chart
    #final_chart.append(chart)
    
    print "PARSING SENTENCE:",' '.join(sentence)
    print "NUMBER OF PARSINGS FOUND",chart[0][-1].count("S")
    #print "Chart:",chart
    for i in range(len(chart)):
        for j in range(len(chart[0])):
            print "chart[%d][%d]:"%(i,j),chart[i][j]
