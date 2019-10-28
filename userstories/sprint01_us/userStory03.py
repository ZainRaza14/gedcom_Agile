from ParserModule import parse_main

from utils import date_Check

from print_main import printTables


def us03_birth_b4_death(file):
    error_list = list()
    #printTables(file)
    indDict,famDict,errorList = parse_main(file)
    
    for iD in indDict:
        an_Indi = indDict[iD]
        if an_Indi.Death == 'NA' and an_Indi.Birthday != 'NA':
            continue 
    
        if an_Indi.Birthday == 'NA':
            error_string = f"ANOMALY: INDIVIDUAL: US03: {an_Indi.indID}: Birthdate not Found "
            error_list.append(error_string)
            
    
        else:
            finalOutput = date_Check(an_Indi.Birthday, an_Indi.Death)
            if finalOutput == False:
                error_string = f"ERROR: INDIVIDUAL: US03: {an_Indi.indID} : Died {an_Indi.Death} before born {an_Indi.Birthday} "
                error_list.append(error_string)
    
    
    return error_list


def user_story03_main():
    error_list= us03_birth_b4_death("us03testdata.ged")
    for eacherror in error_list:
        print(eacherror)


if __name__ == "__main__":
    user_story03_main()