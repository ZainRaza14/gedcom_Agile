from ParserModule import parse_main
from utils import checkDiffInDays
from print_main import printTables
from datetime import datetime

def us31_list_living_single(file):
    indDict,famDict,errorList = parse_main(file)
    #printTables(file)
    error_list = list()
    
    for iD in indDict:
        if indDict[iD].Age > 30 and indDict[iD].Spouse == 'NA':
            error_string = f"ERROR: INDIVIDUAL: US31: The individual {indDict[iD].indID} is single and above 30" 
            error_list.append(error_string)
            
    return error_list
    
def user_story31_main():
    error_list= us31_list_living_single("us31testdata.ged")
    for eacherror in error_list:
        print(eacherror)
        
if __name__ == "__main__":
   user_story31_main()