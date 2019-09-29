from ParserModule import parse_main

'''
US04	Marriage before divorce	sk
US04	Marriage before divorce	
Marriage should occur before divorce of spouses, and divorce can only occur after marriage
'''

def us04_marr_b4_divo(file):
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
    error_list= us04_marr_b4_divo("us04testdata.ged")
    for eacherror in error_list:
        print(eacherror)


if __name__ == "__main__":
    user_story04_main()