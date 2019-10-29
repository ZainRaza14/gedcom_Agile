from ParserModule import parse_main
from utils import checkDiffInDays
from print_main import printTables
from datetime import datetime

def us17_no_marr_2_children(file):

    indDict, famDict, errorList = parse_main(file)
    error_list = list()
    
    for famID in famDict:
        totalChild = famDict[famID].multChild
        
        for child in totalChild:
            if indDict[child].Spouse:
                spouseFam = indDict[child].Spouse
                if indDict[child].Sex == 'M':
                    spouseID = famDict[spouseFam].Wife
                    childMother = famDict[famID].Wife
                    if spouseID == childMother:
                        error_string = f"ERROR: FAMILY: US17: {famDict[famID].famID} Parents should not marry their descendants"
                        error_list.append(error_string)
                                    
                else:
                    spouseID = famDict[spouseFam].Husband
                    childFather = famDict[famID].Husband
                    if spouseID == childFather:
                        error_string = f"ERROR: FAMILY: US17: {famDict[famID].famID} Parents should not marry their descendants"
                        error_list.append(error_string)
                
    return error_list

def user_story17_main():
    list_errors = us17_no_marr_2_children("us17testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story17_main()