from ParserModule import parse_main
from utils import compare_date_to_todays_date,get_first_name
from print_main import printTables
'''
US21 Husband in family should be male and wife in family should be female
'''

def us21_husb_male_wife_female(file):
    error_list = list()
    #printTables(file)
    indDict,famDict,errorList = parse_main(file)
    
    for key,familyData in famDict.items():
        husband_gender = indDict[familyData.Husband].Sex
        husband_name = indDict[familyData.Husband].Name
        wife_gender = indDict[familyData.Wife].Sex
        wife_name = indDict[familyData.Wife].Name
        if husband_gender != "M":
            error_string= f"ERROR: FAMILY: US21 : Husband Id:{familyData.Husband},name:{husband_name} is not male"
            error_list.append(error_string)
        if wife_gender !="F":
            error_string= f"ERROR: FAMILY: US21 : Wife Id:{familyData.Wife},name:{wife_name} is not female"
            error_list.append(error_string)
    return error_list


def user_story21_main():
    error_list= us21_husb_male_wife_female("us16testdata.ged")
    for eacherror in error_list:
        print(eacherror)


if __name__ == "__main__":
    user_story21_main()