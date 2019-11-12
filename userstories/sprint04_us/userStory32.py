from ParserModule import parse_main
from utils import checkDiffInDaysCompTodays
from print_main import printTables

'''
US32 List multiple births
'''

def us32_list_multiple_births(file):
    error_list = list()
    #printTables(file)
    indDict,famDict,errorList = parse_main(file)
    
    birthList = []
    
    for iD in indDict:
         if indDict[iD].Birthday != 'NA':
                for indID in indDict:
                    checkBirth = indDict[indID].Birthday
                    if iD != indID:
                        if indDict[iD].Birthday == checkBirth:
                            error_string = f"ERROR: INDIVIDUAL: US32: The individual {indDict[iD].indID} has multiple births"
                            error_list.append(error_string)
    
    return error_list

def user_story32_main():
    error_list= us32_list_multiple_births("us32testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story32_main()
