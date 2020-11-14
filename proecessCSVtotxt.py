import csv
with open('file1.csv', 'r') as file:
    reader = csv.reader(file)
    cnt=0;
    with open('dangerData.txt', 'w') as writer:
        for row in reader:
            dangerFlag=0;
            # print(row)
            if row[1]!="temperature": 
                if float(row[1])>101 or (int(row[2])<60 or int(row[2])>120) and int(row[3])<90 and (int(row[4])<60 or int(row[4])>130):
                    print("in danger---- ",row[0] )
                    cnt+=1
                    dangerFlag=1
                writer.write(row[1]+","+row[2]+","+row[3]+","+row[4]+","+str(dangerFlag)+"\n")



    print(cnt)