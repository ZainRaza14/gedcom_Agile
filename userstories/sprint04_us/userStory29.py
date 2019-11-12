from ParserModule import parse_main
from utils import checkDiffInDays
from print_main import printTables
from datetime import datetime

def us29_list_deceased(file):
    indDict,famDict,errorList = parse_main(file)
    
    error_list = list()

    for iD in indDict:
        if indDict[iD].Death != 'NA':
            error_string = f"US29: The individual {indDict[iD].indID} is dead"
            error_list.append(error_string)
    
    return error_list
    
def user_story29_main():
    error_list= us29_list_deceased("us29testdata.ged")
    for eacherror in error_list:
        print(eacherror)
        
if __name__ == "__main__":
   user_story29_main()