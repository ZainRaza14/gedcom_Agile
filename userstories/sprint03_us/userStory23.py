from ParserModule import parse_main
from utils import checkDiffInDays
from print_main import printTables
from datetime import datetime

def us23_unique_name_and_birth(file):

    indDict, famDict, errorList = parse_main(file)
    error_list = list()
    indNames = []
    indBirthdates = []
    
    for iD in indDict:
        indNames.append(indDict[iD].Name)
        indBirthdates.append(indDict[iD].Birthday)
 
    if len(indNames) != len(set(indNames)):
        error_string = f"ERROR: INDIVIDUAL: US23: No more than one individual with the same name and birth date should appear in GEDCOM file"
        error_list.append(error_string)
    
    if len(indBirthdates) != len(set(indBirthdates)):
        error_string = f"ERROR: INDIVIDUAL: US23: No more than one individual with the same name and birth date should appear in GEDCOM file"
        error_list.append(error_string)
      
    return error_list

def user_story23_main():
    list_errors = us23_unique_name_and_birth("us23testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story23_main()