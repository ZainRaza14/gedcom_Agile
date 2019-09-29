from ParserModule import parse_main

def us05_marr_b4_death(file):
    indDict,famDict = parse_main(file)
    error_list = list()
    for famID in famDict:
        if famDict[famID].Marriage != "NA" and famDict[famID].Marriage != "":
        # Search through individuals to get husband and wife
            husband = None
            wife = None
            for iD in indDict:
                if indDict[iD].indID == famDict[famID].Husband:
                    husband = indDict[iD]
                    #print(husband)
                if indDict[iD].indID == famDict[famID].Wife:
                    wife = indDict[iD]
                    #print(wife)
            if wife.Death is not None and famDict[famID].Marriage > wife.Death:
                error_string = f"ERROR: FAMILY: US05: {famDict[famID].famID} : Marriage of wife:{wife.indID} occurs after death"
                error_list.append(error_string)
            if husband.Death is not None and famDict[famID].Marriage > husband.Death:
                error_string = f"ERROR: FAMILY: US05: {famDict[famID].famID} : Marriage of husband:{husband.indID} occurs after death"
                error_list.append(error_string)

                
    return error_list
        #return list 

def user_story05_main():
    error_list= us05_marr_b4_death("us05testdata.ged")
    for eacherror in error_list:
        print(eacherror)
if __name__ == "__main__":
   user_story05_main()