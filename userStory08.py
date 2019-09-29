from ParserModule import parse_main
from utils import compare_date_to_todays_date,checkDiffInMonths

from print_main import printTables
'''
US08    Birth before marriage of parents	sk
US08	Birth before marriage of parents	
Children should be born after marriage of parents (and not more than 9 months after their divorce)
'''

def user_story08(file):
    error_list = list()
    #printTables(file)
    indDict,famDict = parse_main(file)
    
    for famId, famObject in famDict.items():
        marriedDate= famObject.Marriage
        divorcedDate= famObject.Divorce
        if famObject.multChild != "NA":
            for eachchild in famObject.multChild:
                indObj=indDict[eachchild]
                birthday = indObj.Birthday
                #print(f"{birthday} > {marriedDate} is {birthday > marriedDate} ")
                if birthday < marriedDate:
                    error_list.append(f"ANOMALY: FAMILY: US08: {indObj.indID}: born {indObj.Birthday} before marriage on {marriedDate}")
                if birthday > divorcedDate:
                    if checkDiffInMonths(birthday,divorcedDate) > 9:
                        error_list.append(f"ANOMALY: FAMILY: US08: {indObj.indID}: born {indObj.Birthday} after divorce on {marriedDate}")
                '''
                elif birthday < divorcedDate and checkDiffInMonths(birthday,divorcedDate) < 9 :
                    error_list.append(f"ANOMALY: FAMILY: US08: {indObj.indID}: born {indObj.Birthday} after divorce on {marriedDate}")
                '''
    return error_list
    


    '''
    first iterate over families
       for each of families, track MarriedDate and DivorcedDate
        check if children is not 'NA'
        then get the childrens=> 
             for each children
                 a) check the individual birthday 
                     =>    compare birthday to marriage day .
                     =>    if it is before => add the error
                           if it is not
                              => then check if his birthday and marriage day is crossing 9 months 
                              => if yes 
                                    a) add the error
    '''

    
    #return list 


def user_story08_main():
    list_errors =user_story08("us08testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story08_main()