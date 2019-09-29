from ParserModule import parse_main
from utils import compare_date_to_todays_date
from print_main import printTables
'''
US04	Marriage before divorce	sk
US04	Marriage before divorce	
Marriage should occur before divorce of spouses, and divorce can only occur after marriage
'''

def user_story04(file):
    error_list = list()
    #printTables(file)
    indDict,famDict = parse_main(file)
    for key,familyData in famDict.items():
        #print(f"key is {key} and data is {familyData}")
        if familyData.Divorce < familyData.Marriage:
            error_string = f"ERROR: FAMILY: US04: {familyData.famID}: Divorced {familyData.Divorce} before married {familyData.Marriage} "
            error_list.append(error_string)
    return error_list


def user_story04_main():
    error_list= user_story04("us04testdata.ged")
    for eacherror in error_list:
        print(eacherror)


if __name__ == "__main__":
    user_story04_main()