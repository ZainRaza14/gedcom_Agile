from ParserModule import parse_main
from utils import compare_date_to_todays_date
'''
US 07
Death should be less than 150 years after birth for dead people, and current date should be less than 
150 years after birth for all living people
Birth => Individual 
Death => Individual
'''
def us07_less_than_150years(file):
    indDict,famDict,errorList = parse_main(file)
    error_list = list()
    for iD in indDict:
        if indDict[iD].Age > 150:
            if indDict[iD].Alive == True:       
                error_string = f"ERROR: INDIVIDUAL: US07: {indDict[iD].indID}: Birth Date OF Individual:{indDict[iD].Birthday} Age is more than 150 years"
                error_list.append(error_string)
            
            if indDict[iD].Alive == False:
                error_string = f"ERROR: INDIVIDUAL: US07: {indDict[iD].indID}: Birth Date OF Deceased Individual:{indDict[iD].Birthday} and Death Date OF Deceased Individual:{indDict[iD].Death} Age is more than 150 years"
                error_list.append(error_string)
                    
    return error_list            
                         
def user_story07_main():
    error_list= us07_less_than_150years("us07testdata.ged")
    for eacherror in error_list:
        print(eacherror)
        
if __name__ == "__main__":
   user_story07_main()