from ParserModule import parse_main
from utils import checkDiffInDays, date_Check

from print_main import printTables




def us14_multiple_births(file):
    error_list = list()
    #printTables(file)
    indDict,famDict = parse_main(file)
    
    totalSpouses = []
    
    numSpouse = 0
    
    countSameSiblings = 1
    
    listChild = [] 
    
    lenChild = 0
    
    for famId in famDict:
        if(famDict[famId].multChild):
            lenChild = len(famDict[famId].multChild)
            if lenChild > 5:
                listChild = famDict[famId].multChild
                birthCheck = indDict[listChild[0]].Birthday
                #print(birthCheck)
                #print(indDict[listChild[i]].Birthday)
                for i in range(1,lenChild):
                    #print(indDict[listChild[i]].Birthday)
                    if indDict[listChild[i]].Birthday == birthCheck:
                        countSameSiblings +=1
                        
                if countSameSiblings > 5:
                    #print(countSameSiblings)
                    error_string = f"ERROR: FAMILY: US14 Family {famDict[famId].famID} has more than 5 siblings born at the same time"
                    error_list.append(error_string)
               
                
        
        
            
            
                
    return error_list
    



def user_story14_main():
    list_errors =us14_multiple_births("us14testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story11_main()