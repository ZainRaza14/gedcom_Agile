from ParserModule import parse_main
from utils import checkDiffInDaysCompTodays
from print_main import printTables
from datetime import date
from datetime import datetime

'''
US35 list recent births
'''

def us35_list_recent_births(file):
    error_list = list()
    #printTables(file)
    indDict,famDict,errorList = parse_main(file)
    for iD in indDict:
         if indDict[iD].Birthday != 'NA':
                indBirthday = indDict[iD].Birthday
                
                todaysDate = date.today().strftime("%Y-%m-%d")
                
                indBCheck = datetime.strptime(indBirthday, "%Y-%m-%d")
                
                todaysCheck = datetime.strptime(todaysDate, "%Y-%m-%d")
                
                if (todaysCheck - indBCheck).days < 30:
                    error_string = f"ERROR: INDIVIDUAL: US35: The individual {indDict[iD].indID} was born within the last 30 days"
                    error_list.append(error_string)
    
    return error_list
    


def user_story35_main():
    error_list= us35_list_recent_births("us35testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story35_main()