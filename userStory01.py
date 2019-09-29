from ParserModule import parse_main
from utils import compare_date_to_todays_date

def us01_dates_b4_curr_date(file):
    indDict,famDict = parse_main(file)
    error_list = list()
    for iD in indDict:
        if indDict[iD].Birthday != "NA" and indDict[iD].Birthday != "":
            if compare_date_to_todays_date(indDict[iD].Birthday)==1:
                error_string = f"ERROR: INDIVIDUAL: US01: {indDict[iD].indID}: Birthday {indDict[iD].Birthday} is after todays date"
                error_list.append(error_string)

        if indDict[iD].Death != "NA" and indDict[iD].Death!="":
            if compare_date_to_todays_date(indDict[iD].Death)==1:
                error_string = f"ERROR: INDIVIDUAL: US01: {indDict[iD].indID}: Death Date {indDict[iD].Death} is after todays date"
                error_list.append(error_string)

    for famID in famDict:
        if famDict[famID].Marriage != "NA" and famDict[famID].Marriage != "":
            if compare_date_to_todays_date(famDict[famID].Marriage)==1:
                error_string = f"ERROR: FAMILY: US01: {famDict[famID].famID}: Marriage Date {famDict[famID].Marriage}  is after todays date"
                error_list.append(error_string)
                
        if famDict[famID].Divorce != "NA" and famDict[famID].Divorce != "":
            if compare_date_to_todays_date(famDict[famID].Divorce)==1:
                error_string = f"ERROR: FAMILY: US01: {famDict[famID].famID}: Divorce Date {famDict[famID].Divorce}  is after todays date"
                error_list.append(error_string)
    return error_list
        #return list 

def user_story01_main():
    error_list= us01_dates_b4_curr_date("us01testdata.ged")
    for eacherror in error_list:
        print(eacherror)
if __name__ == "__main__":
   user_story01_main()