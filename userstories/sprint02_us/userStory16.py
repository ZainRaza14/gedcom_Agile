from ParserModule import parse_main
from utils import compare_date_to_todays_date,get_first_name
from print_main import printTables
'''
US16	Male last names	All male members of a family should have the same last name
'''

def us16_male_last_names(file):
    error_list = list()
    #printTables(file)
    '''
    loop over family records
    for each family
        a) get the husband first name 
           1. see wife name and if wife first name and husband name is not same
              a) add that individual Id error to wife Name 
           2. for each children 
              a) get ind formation and see if the first name of ind is matching with husband firstname
              b) if does not match 
                  if yes add to error_list
    '''
    indDict,famDict = parse_main(file)
    for key,familyData in famDict.items():
        husband_first_name = get_first_name(indDict[familyData.Husband].Name)
        for eachchild in familyData.multChild:
            child_full_name= indDict[eachchild].Name
            child_first_name= get_first_name(child_full_name)
            if child_first_name != husband_first_name:
                error_string= f"ERROR: FAMILY: US16: Individual {eachchild} Name: {child_full_name} not matched with family first name: {husband_first_name}"
                error_list.append(error_string);
    return error_list


def user_story16_main():
    error_list= us16_male_last_names("us16testdata.ged")
    for eacherror in error_list:
        print(eacherror)


if __name__ == "__main__":
    user_story16_main()