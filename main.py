import csv
import re
import insults

myData =  []


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




def getUserDescriptionLength(columns , columnsNames):

            count = 0
            for row in myData:
                if count != 0:
                    for i in range(len(columns)):                                                             
                        row[columnsNames[i]] = len(row[columns[i]].replace(" ", ""))
                       
                     
                else:
                    for i in range(len(columnsNames)):
                        row[columnsNames[i]] =columnsNames[i]
                    count=1

                 

                    

def roundColuemns(columns):

            count = 0
            for row in myData:
                
                # if count != 0:
                    
                    for i in range(len(columns)): 
                        
                        try: 
                            cell = row[columns[i]]
                            
                            if(cell != "?"):        
                                
                                row[columns[i]] = round(float(cell))

                            else:
                                row[columns[i]] = 1000 
                        except Exception:
                                print("error in 68")
                                                        
                                            
                # else:
                #     for i in range(len(columnsNames)):
                #         row[columnsNames[i]] = columnsNames[i]
                
                #     count=1
            

def getRatio(columns , columnsNames):
            
            if(len(columns) > 2):
                print("you can't enter more or less than two columens")
                return

            count = 0
            for row in myData:
                      
                if count != 0:
                    try:
                        
                         num1 = int(row[columns[0]])
                         num2 = int(row[columns[1]])                                                                         
                         row[columnsNames[0]] = round(num1/num2)
                         
                    except Exception as e:
                           row[columnsNames[0]] = 0                 
                else:                  
                    row[columnsNames[0]] = columnsNames[0] 
                    count=1



def getinsults(columns , columnsNames):
     
        
        insult = insults.insults()
        for col in range(len(columns)):
            tweetinsults = ""
            count = 0
            for row in myData:      
                if count != 0:
                    try:
                        tweet = row[columns[col]]
                        for ins in range(len(insult)) :
                            if (tweet.find(insult[ins]) != -1): 
                                tweetinsults = tweetinsults + insult[ins] + "  "
                               
                                                                        
                        row[columnsNames[col]] = tweetinsults
                        tweetinsults = ""   
                        
                    except Exception as e:
                            row[columnsNames[col]] = 0
                            
                                
                else:                  
                    row[columnsNames[col]] = columnsNames[col]
                    count=1


def checkColuemns(coluemn1 , coluemn2):
    if(len(coluemn1) ==  len(coluemn2)) :
         return True 
    else: 
         return False

def isColuemn(coluemns):
    for coluemn in coluemns:
        if(coluemn not in myData[0]):
            return coluemn
    return True

def isNotColuemn(coluemns):
        for coluemn in coluemns:
            if(coluemn  in myData[0]):
                return coluemn
        return True

def checkColuemns(coluemn1 , coluemn2):
    if(len(coluemn1) ==  len(coluemn2)) :
         return True 
    else: 
         return False

def getAnswer():
   while True: 
    columens =  setColumens()
    columenNames =  setColumensNames()
    if(checkColuemns(columens , columenNames)):
        return columens , columenNames
    else:
        print("columens count and new columen names count are not equal please try again \n")
     
       

def setColumens():
     
     while True:
        columns = (input("\n enter columns names with sperated ',' : ")).replace(" " , "").split(",") 
        if(columns[0] == "0") : exit()
        column = isColuemn(columns)
        if(column == True): 
            return columns 
        else: print(column + " is not a column, please try again \n")    


def setColumensNames():
    while True:
        columnNames = (input("\nenter new columns names with sperated ',' : ")).replace(" " , "").split(",") 
        if(columnNames[0] == "0") : exit()
        column = isNotColuemn(columnNames)
        if(column == True): 
            return columnNames 
        else: print(column + " is already created, please try again\n") 







        

        



def readData(filePath):
    try:
        with open(filePath,'rt')as read_obj:
                data = csv.DictReader(read_obj)                        
                for row in data:                    
                    myData.append(row)
        print("Data is been loaded successfully \n")  
        return True                  
    except Exception as e:
        print("There is a problem on reading the file\n")
        return False
        
    
        


       

def writeData(filePath):
    try:
        with open( filePath, 'w', newline='') as write_obj:
                    csv_writer = csv.writer(write_obj)  
                    count = 0
                    
                    for row in myData:
                        if count != 0:                        
                            csv_writer.writerow(row.values())            
                        else:
                            csv_writer.writerow(row.keys())  
                            count = 1      

                    
    except Exception as e:
        print(e)
               

def main():
        
  
    #  readData(filePath)
    #  roundColuemns(["FollowersToAccountAge" , "StatusesCountToAccountAge"])
    #  getUserDescriptionLength(["User.Screen_name" , "User.Description"],["User.Screen_Count", "User.Description_Count"])
    #  getRatio(["User.Followers_count","User.Friends_count"],"ratio")
    #  getinsults("Text","Insults")
    #  writeData(newFilePath)
     
       
        while True:
            fileName =  input("please enter the file path here : ")
            newFile = input("do you want the results in other file? if yes please enter the path and the new file name with .csv at the end if no just press enter : ")
            if(newFile == ""):
                newFile  = fileName
            if(readData(fileName)):
                break
            

        
        while True:
            answer = input("please enter your requiest : \n 1. for avrage  \n 2. for charcters count  \n 3. for round columens \n 4. for insultes  \n 5. for ratio of 2 columens \n 0. for exit \n\n  answer : ")
            if(len(answer) == 1):
                if(re.findall("0|1|2|3|4|5", answer)):
                    if(answer == "2"):
                        columns , columnsNames = getAnswer()
                        getUserDescriptionLength(columns , columnsNames)
                    elif(answer == "3"):
                        roundColuemns(setColumens())
                    elif(answer == "4"):
                        columns , columnsNames = getAnswer()
                        getinsults(columns,columnsNames)
                    elif(answer == "5"):
                        columns= setColumens()
                        columnsNames = None
                        x = 0
                        while x == 0:
                            columnsNames = setColumensNames()
                            if(len(columnsNames) == 1):
                                x = 1
                            else:    
                                print("you can't enter more than one value for ratio value")

                        getRatio(columns , columnsNames)
                    else: break       
                else: print("please enter a on of the following numbers")           

                    
        writeData(newFile)
        

          

    
if __name__== "__main__": main()