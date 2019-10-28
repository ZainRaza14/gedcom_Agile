from ParserModule import parse_main
from utils import checkDiffInDays

from print_main import printTables




def us13_siblings_spacing(file):
    error_list = list()
    #printTables(file)
    indDict,famDict,errorList = parse_main(file)
    
    for famID in famDict:
        birthdays=[];
        if famDict[famID].multChild !=[]:
            for child in famDict[famID].multChild:
                for iD in indDict:
                    if indDict[iD].indID==child:
                        birthdays.append(indDict[iD].Birthday)
            
            cnt= len(birthdays)
            i=0;
            while i<=cnt-1:
                n=0;
                while n<=cnt-1:
                    diff=checkDiffInDays(birthdays[i],birthdays[n])
                    if diff>1 and diff<244:
                            error_string = f"ERROR: FAMILY: US13: The spacing between sibling1:{famDict[famID].multChild[i]} and sibling2:{famDict[famID].multChild[n]} of family:{famDict[famID].famID} is not valid"
                            error_list.append(error_string)
                    n=n+1;
                i=i+1;

                
    return error_list
    



def user_story13_main():
    list_errors =us13_siblings_spacing("us13testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story13_main()