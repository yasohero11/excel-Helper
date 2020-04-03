import csv
def getavg(cnum) :
    sum = 0
    count = 0
    with open('c.csv','rt')as file:
        data = csv.reader(file)
        for row in data:
            if row[cnum].isdigit() :
                sum+=int(row[cnum])
                count+=1
    return sum/count
def setdata(tweetlenth) :
    with open('c.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["null", "null", "null","null","null","null", "null", "null","null","null","null", "null", "null","null","null","null", "null", "null","null","null","null", "null", "null","null","AVG = "+str(tweetlenth),"null", "null", "null","null","null","null", "null", "null","null","null","null", "null", "null","null","null","null", "null", "null","null","null"])

def main():
    setdata(getavg(24))
  
if __name__== "__main__": main()