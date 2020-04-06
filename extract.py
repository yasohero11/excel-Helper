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
                                row[columns[i]] = "?" 
                        except Exception:
                                print("error in 68")
                                                        
                                            
                # else:
                #     for i in range(len(columnsNames)):
                #         row[columnsNames[i]] = columnsNames[i]
                
                #     count=1
            

def getRatio(columns , columnsNames):
        
            if(len(columns) > 2):
                print("you can't enter more than two columens")
                return

            count = 0
            for row in myData:
                      
                if count != 0:
                    try:
                        
                         num1 = int(row[columns[0]])
                         num2 = int(row[columns[1]])                                                                         
                         row[columnsNames] = num1/num2
                         
                    except Exception as e:
                           row[columnsNames] = 0                 
                else:                  
                    row[columnsNames] = columnsNames 
                    count=1
def getinsults(columns , columnsNames):
        tweetinsults = ""
        insult = insults.insults()
        count = 0
        for row in myData:      
            if count != 0:
                try:
                    tweet = row[columns]
                    for ins in range(len(insult)) :
                        if (tweet.find(insult[ins]) != -1): 
                            tweetinsults = tweetinsults + insult[ins] + "  "
                                                                     
                    row[columnsNames] = tweetinsults
                    tweetinsults = ""   
                except Exception as e:
                        row[columnsNames] = 0                 
            else:                  
                row[columnsNames] = columnsNames 
                count=1

def checkColuemns(coluemn1 , coluemn2):
    if(len(coluemn1) ==  len(coluemn2)) :
         return True 
    else: 
         return False
              


        

        



def readData(filePath):
    try:
        with open(filePath,'rt')as read_obj:
                data = csv.DictReader(read_obj)                        
                for row in data:                    
                    myData.append(row)
    except Exception as e:
        print(e)

       

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

     filePath = input("enter file path here : ")
     newFilePath = input("new file path : ")
     if(newFilePath == ""):
         newFilePath = filePath

     readData(filePath)
     roundColuemns(["FollowersToAccountAge" , "StatusesCountToAccountAge"])
     getUserDescriptionLength(["User.Screen_name" , "User.Description"],["User.Screen_Count", "User.Description_Count"])
     getRatio(["User.Followers_count","User.Friends_count"],"ratio")
     getinsults("Text","Insults")
     writeData(newFilePath)
     
    # getinsults("Text","Insults")
    # writeData("x.csv")

    #setdata(getavg(24))
    #getUserDescriptionLength("Testing" , "t2" , ["3","37"],["userDis","userScreenNameLe"]) 
    #roundColuemns("Testing" , "t1" , ["33","34","35"],["round1","round2","round2"])
    #getRatio("Testing" , ["User.Followers_count","User.Friends_count"],"raio")

    #   with open("Testing" +'.csv','rt')as read_obj:
          
    #         data = csv.DictReader(read_obj)
    #         try:
    #             for row in data:
    #                 print(str(row["raio"]))
    #         except Exception:
    #             print("any")    
    
        # fileName =  input("please enter the file path here : ")
        # readData(fileName)
        # newFile = input("do you want the results in other file? if yes please enter the path and the new file name with .csv at the end in no just press enter : ")
        # if(newFile == ""):
        #     newFile  = fileName


        # answer = input("please enter your requiest : \n 1. for avrage enter 'a' \n 2. for charcters count enter 'c' \n 3. for round columens enter 'r' \n answer : ")
        # if(len(answer) == 1):
        #     if(re.findall("a|c|r", answer)):

        #         if(answer == "c"):
        #             columns = (input("enter columns names with sperated ',' : ")).replace(" " , "").split(",") 
        #             columnsNames = (input("enter new columns names with sperated ',' : ")).replace(" " , "").split(",") 
        #             if(checkColuemns(columns , columnsNames)):
        #                 getUserDescriptionLength(fileName , columns , columnsNames)    

                    
        #             #print("the columens names not equal to new columens names, try agaien")
      
        # else:
        #     print("you enterd a word not a charter, please try ")
        
        # writeData(newFile) 

        # input("exit")     

        #readData(fileName)
        
        #getUserDescriptionLength("training2" , ["User.Screen_name" , "User.Description"],["count_user", "dis_count"]) 
        #getRatio("Testing" , ["User.Followers_count","User.Friends_count"],"raio")
        #roundColuemns("Testing (1)" ,["FollowersToAccountAge" , "StatusesCountToAccountAge" , "raio"] , ["ratio raio" , "raio1", "rasio2"] )

        #writeData(newFile)   
    #getRatio("Testing" , ["User.Followers_count","User.Friends_count"],"raio")
    
    
   

if __name__== "__main__": main()