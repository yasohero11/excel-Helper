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


def insertRow(row, index, data):
        row.insert(index,data)
        

def getUserDescriptionLength(fileName , newFileName , columns , columnsNames):
        if(len(columns) != len(columnsNames)):
            print("please enter same number of values of columns and columns_Names")
            return
        with open(fileName +'.csv','rt')as read_obj, \
           open(newFileName + '.csv', 'a+', newline='') as write_obj:
            data = csv.reader(read_obj)
            csv_writer = csv.writer(write_obj)
            count = 0
            for row in data:
                rowLength =  len(row)
                if count != 0:
                    for i in range(len(columns)):                                                             
                         row.insert(rowLength+i,len(row[int(columns[i])].replace(" ", "")))

                    csv_writer.writerow(row)        
                else:
                    for i in range(len(columnsNames)):
                        row.insert(rowLength+i,columnsNames[i])

                    csv_writer.writerow(row)
                    count=1


                    

def roundColuemns(fileName , newFileName , columns , columnsNames):
        if(len(columns) != len(columnsNames)):
            print("please enter same number of values of columns and columns_Names")
            return
        with open(fileName +'.csv','rt')as read_obj, \
           open(newFileName + '.csv', 'a+', newline='') as write_obj:
            data = csv.reader(read_obj)
            csv_writer = csv.writer(write_obj)
            count = 0
            for row in data:
                rowLength = len(row)
                if count != 0:
                    
                    for i in range(len(columns)): 
                        try: 
                            cell = row[int(columns[i])]
                            
                            if(cell != "?"):        
                                
                                row.insert(rowLength+i,round(float(cell)))
                            else:
                                row.insert(rowLength+i,"?") 
                        except Exception:
                                print("error in 68")
                                                        
                    csv_writer.writerow(row)                          
                else:
                    for i in range(len(columnsNames)):
                        row.insert(rowLength+i,columnsNames[i])

                    csv_writer.writerow(row)
                    count=1


#                       6,7
def getRatio(fileName , newFileName , columns , columnsNames):
        
        with open(fileName +'.csv','rt')as read_obj, \
           open(newFileName + '.csv', 'a+', newline='') as write_obj:
            data = csv.reader(read_obj)
            csv_writer = csv.writer(write_obj)
            count = 0
            for row in data:
                rowLength =  len(row)
              
                if count != 0:
                    try:        
                        num1 = int(row[int(columns[0])])
                        num2 = int(row[int(columns[1])])                                                           
                        row.insert(rowLength+1,(num1/num2))
                    except Exception:
                            row.insert(rowLength+1,0)
                    csv_writer.writerow(row)        
                else:
                  
                    row.insert(rowLength+1,columnsNames)

                    csv_writer.writerow(row)
                    count=1

               

def main():
    #setdata(getavg(24))
    #getUserDescriptionLength("Testing" , "t2" , ["3","37"],["userDis","userScreenNameLe"]) 
    #roundColuemns("Testing" , "t1" , ["33","34","35"],["round1","round2","round2"])
    getRatio("Testing" , "t2" , ["6","7"],"raio")
    
   

if __name__== "__main__": main()