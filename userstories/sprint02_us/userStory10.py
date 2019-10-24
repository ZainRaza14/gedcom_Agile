from ParserModule import parse_main
from utils import checkDiffInDays

from print_main import printTables
from datetime import datetime

#Get Age
def getAgeAt(born, given):
    born = datetime.strptime(born, "%Y-%m-%d")
    given = datetime.strptime(given, "%Y-%m-%d")
    return given.year - born.year - ((given.month, given.day) < (born.month, born.day))

def us10_marr_after_14(file):
    indDict,famDict = parse_main(file)
    error_list = list()
    
    for famID in famDict:
            if famDict[famID].Husband != 'NA': #check husb age
                
                husband = famDict[famID].Husband
                if(husband in indDict):
                    age = 0
                    if(famDict[famID].Marriage != 'NA'):
                        age = getAgeAt(indDict[husband].Birthday, famDict[famID].Marriage)
                    if(age <=14):
                        error_string = f"ERROR: US10 - The individual {husband} was married before 14, this is not valid"
                        error_list.append(error_string)
        
            if famDict[famID].Wife != 'NA': #check wife age
                wife = famDict[famID].Wife
                if(wife in indDict):
                    age = 0
                    if(famDict[famID].Marriage != 'NA'):
                        age = getAgeAt(indDict[wife].Birthday, famDict[famID].Marriage)
                    if(age <=14):
                        error_string = f"ERROR: US10 - The individual {wife} was married before 14, this is not valid"
                        error_list.append(error_string)    

    return error_list
    
def user_story10_main():
    list_errors = us10_marr_after_14("us10testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story10_main()