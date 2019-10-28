from ParserModule import parse_main
from utils import checkDiffInDays
from print_main import printTables
from datetime import datetime

def us15_fewer_than_15_siblings(file):

    indDict,famDict,errorList = parse_main(file)
    error_list = list()
    for famID in famDict:

        if famDict[famID].multChild != 'NA':
            if len(famDict[famID].multChild) > 15:
                error_string = f"ERROR: FAMILY: US15: Family has more than 15 siblings {famDict[famID].famID}"
                error_list.append(error_string)
    return error_list
    
def user_story15_main():
    list_errors = us15_fewer_than_15_siblings("us15testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story15_main()
