from ParserModule import parse_main
from utils import compare_date_to_todays_date,checkDiffInMonths
from print_main import printTables
'''
US09    Birth before death of parents	
Child should be born before death of mother and before 9 months after death of father

'''
def us09_birth_b4_parents_death(file):
    error_list = list()
    #printTables(file)
    indDict,famDict = parse_main(file)
    '''
    loop over family records
    for each family
        a) get the husband death and wife death from individuals
           for each children 
                => check if child is born before (wife death) 
                    a) if yes add to error_list
                =>  difference of (death of father - birth of child) < 9 
                    a) if yes add to error_list
    '''
    for key,familyData in famDict.items():
        #print(f"key is {key} and data is {familyData}")
        husband_death_date = indDict[familyData.Husband].Death
        wife_death_date = indDict[familyData.Wife].Death
        wife_name = indDict[familyData.Wife].Name; 
        husband_name = indDict[familyData.Husband].Name; 
        for eachchild in familyData.multChild:
            child_birth_date = indDict[eachchild].Birthday
            child_full_name= indDict[eachchild].Name
            if child_birth_date > wife_death_date:
                error_string= f"ERROR: FAMILY: US09 : Individual {eachchild} Name: {child_full_name} born after death of mother {familyData.Wife} {wife_name}"
                error_list.append(error_string);
            if child_birth_date > husband_death_date and not (checkDiffInMonths(child_birth_date,husband_death_date) < 9):
                error_string= f"ERROR: FAMILY: US09 : Individual {eachchild} Name: {child_full_name} born 9 months after death of father {familyData.Husband} {husband_name}"
                error_list.append(error_string);
    return error_list


def user_story09_main():
    error_list= us09_birth_b4_parents_death("us09testdata.ged")
    for eacherror in error_list:
        print(eacherror)


if __name__ == "__main__":
    user_story09_main()