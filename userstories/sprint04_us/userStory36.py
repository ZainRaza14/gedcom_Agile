from ParserModule import parse_main
from utils import checkDiffInDaysCompTodays
from print_main import printTables

'''
US36 List all recent deaths
'''

def us36_list_recent_deaths(file):
    error_list = list()
    printTables(file)
    indDict,famDict,errorList = parse_main(file)
    for iD in indDict:
         if indDict[iD].Death != 'NA':
             diff=checkDiffInDaysCompTodays(indDict[iD].Death)
             if diff>=0 and diff<31:
                 error_string = f"ERROR: INDIVIDUAL: US36: The individual {indDict[iD].indID} died recently on {indDict[iD].Death}"
                 error_list.append(error_string)
    
    return error_list

    


def user_story36_main():
    error_list= us36_list_recent_deaths("us36testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story36_main()