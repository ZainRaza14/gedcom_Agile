from ParserModule import parse_main
from utils import compare_date_to_todays_date

'''
US 02 
Birth should occur before marriage of an individual
Birth=> Individual 
Marriage => Family
'''
def us02_birth_b4_marr(file):
    indDict,famDict,errorList = parse_main(file)
    error_list = list()
    for famID in famDict :
        if famDict[famID].Marriage != "NA" and famDict[famID].Marriage != "":
            # Search through individuals to get husband and wife
            husband = None
            wife = None
            for iD in indDict:
                if indDict[iD].indID == famDict[famID].Husband:
                    husband = indDict[iD]
                
                if indDict[iD].indID == famDict[famID].Wife:
                    wife = indDict[iD]

            if wife.Birthday is not None and wife.Birthday > famDict[famID].Marriage:
                error_string = f"ERROR: INDIVIDUAL: US02: {wife.indID}: Birth Date OF Wife:{wife.Birthday} is after Marriage Date:{famDict[famID].Marriage}"
                error_list.append(error_string)
                
            if husband.Birthday is not None and husband.Birthday > famDict[famID].Marriage:
                error_string = f"ERROR: INDIVIDUAL: US02: {husband.indID}: Birth Date OF Husband:{husband.Birthday} is after Marriage Date:{famDict[famID].Marriage}"
                error_list.append(error_string)
    return error_list       

def user_story02_main():
    error_list= us02_birth_b4_marr("us02testdata.ged")
    for eacherror in error_list:
        print(eacherror)
        
if __name__ == "__main__":
   user_story02_main()