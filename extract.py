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



def getUserDescriptionLength():
        with open('Testing (1).csv','rt')as read_obj, \
           open('Testing (2).csv', 'a+', newline='') as write_obj:
            data = csv.reader(read_obj)
            csv_writer = csv.writer(write_obj)
            count = 0
            for row in data:
                if count != 0:
                    words = row[6].split()                                   
                    row.append(len(words))
                    csv_writer.writerow(row)        
                else:
                     row.append("DescriptionLength")
                     csv_writer.writerow(row)
                     count=1

# def getUserDescriptionLength():
#         with open('Testing (1).csv','rt')as read_obj:
           
#             data = csv.reader(read_obj)
#             with open('Testing (1).csv', 'a+', newline='') as write_obj:
#                 csv_writer = csv.writer(write_obj)
#                 count = 0
#                 for row in data:
#                     if count != 0:
#                         words = row[6].split()                                   
#                         row.append(len(words))
#                         csv_writer.writerow(row)        
#                     else:
#                         row.append("DescriptionLength")
#                         csv_writer.writerow(row)
#                         count=1                     

# def getUserDescription():
#         with open('Testing (1).csv','rt')as read_obj:
#              data = csv.reader(read_obj)
             

#         return data

# def getUserDescriptionLength(userDescription):
        
#         with open('Testing (1).csv', 'a+', newline='') as write_obj:
#             csv_writer = csv.writer(write_obj)
#             count = 0
#             for row in userDescription:
#                     if count != 0:
#                         words = row[6].split()                                   
#                         row.append(len(words))
#                         csv_writer.writerow(row)        
#                     else:
#                         row.append("DescriptionLength")
#                         csv_writer.writerow(row)
#                         count=1



               

def main():
    #setdata(getavg(24))
    getUserDescriptionLength() 
if __name__== "__main__": main()