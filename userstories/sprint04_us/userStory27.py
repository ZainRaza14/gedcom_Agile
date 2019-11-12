from ParserModule import parse_main
from print_main import printTables

'''
US27 List ages for individuals
'''

def us27_individual_ages(file):
    error_list = list()
    #printTables(file)
    indDict,famDict,errorList = parse_main(file)
    agedict={};
    for iD in indDict:
         if indDict[iD].Age != 'NA':
            agedict[indDict[iD].indID]=indDict[iD].Age
    error_string = f"US27: The list of individuals along with their ages are:{agedict}"
    error_list.append(error_string)
    
    return error_list

    


def user_story27_main():
    error_list= us27_individual_ages("us27testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story27_main()