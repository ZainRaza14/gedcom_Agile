from ParserModule import parse_main

from print_main import printTables


def us12_parents_not_too_old(file):
    error_list = list()
    #printTables(file)
    indDict,famDict,errorList = parse_main(file)
    
    for famID in famDict:
        if famDict[famID].multChild !=[]:
            mother=famDict[famID].Wife;
            father=famDict[famID].Husband;
            for iD in indDict:
                if indDict[iD].indID==mother:
                    age_moth=indDict[iD].Age
                if indDict[iD].indID==father:
                    age_fath=indDict[iD].Age
            for child in famDict[famID].multChild:
                for iD in indDict:
                    if indDict[iD].indID==child:
                        if age_moth-indDict[iD].Age>=60:
                            error_string = f"ERROR: INDIVIDUAL: US12: The age difference of child:{indDict[iD].indID} and mother:{mother} is greater than or equal to 60"
                            error_list.append(error_string)
                        if age_fath-indDict[iD].Age>=80:
                            error_string = f"ERROR: INDIVIDUAL: US12: The age difference of child:{indDict[iD].indID} and father:{father} is greater than or equal to 80"
                            error_list.append(error_string)
                            
    return error_list
    



def user_story12_main():
    list_errors =us12_parents_not_too_old("us12testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story12_main()