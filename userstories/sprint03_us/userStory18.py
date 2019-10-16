from ParserModule import parse_main
from utils import compare_date_to_todays_date,checkDiffInMonths
from print_main import printTables
'''
US18 Siblings should not marry one another
'''
def us18_sibilings_no_marriage(file):
    error_list = list()
    printTables(file)
    indDict,famDict = parse_main(file)
    '''
    loop over family records
    a) for each of the family record, get all the children 
       => for each children, get the individual record's spouse
            => for each record get column Spouse and store it in variable
    '''
    for key,familyData in famDict.items():
        children = familyData.multChild
        for eachchild in children:
            child_id = eachchild
            spouse_id = indDict[child_id].Spouse
            siblings= children[children.index(child_id)+1:]
            for eachsibiling in siblings:
                if (spouse_id!="NA" and indDict[eachsibiling].Spouse!="NA") and spouse_id==indDict[eachsibiling].Spouse:
                    error_string= f"ERROR: FAMILY: US18 : Sibiings Id:{indDict[eachsibiling].indID},name:{indDict[eachsibiling].Name} and  Id:{indDict[child_id].indID},name:{indDict[child_id].Name} are married"
                    error_list.append(error_string);
    return error_list

        
def user_story18_main():
    error_list= us18_sibilings_no_marriage("us18testdata.ged")
    for eacherror in error_list:
        print(eacherror)


if __name__ == "__main__":
    user_story18_main()