from ParserModule import parse_main
from utils import checkDiffInDays, date_Check

from print_main import printTables




def us11_no_bigamy(file):
    error_list = list()
    #printTables(file)
    indDict,famDict = parse_main(file)
    totalSpouses = []
    numSpouse = 0
    
    for iD in indDict:
        an_Indi = indDict[iD]
        
        if an_Indi.Spouse == 'NA':
            continue
        else:
            for famID in famDict:
                id_Fam = famDict[famID]
                
                if (famID != an_Indi.Spouse and ((id_Fam.Husband and an_Indi.indID == id_Fam.Husband) 
                   or (id_Fam.Wife and an_Indi.indID == id_Fam.Wife))):
                    
                    if (famDict[an_Indi.Spouse].Marriage and id_Fam.Marriage):

                        if date_Check(famDict[an_Indi.Spouse].Marriage, id_Fam.Marriage):
                            marriage1 = famDict[an_Indi.Spouse]
                            marriage2 = id_Fam
                        else:
                            marriage1 = id_Fam
                            marriage2 = famDict[an_Indi.Spouse]


                        if(an_Indi.indID == marriage1.Husband):
                            id_Spouse = marriage1.Wife
                        else:
                            id_Spouse = marriage1.Husband

                        


                        if (marriage1.Divorce == 'NA'):                                         
                                                       

                            if(indDict[id_Spouse].Death == 'NA'):
                                error_string = f"ERROR: INDIVIDUAL: US11: {an_Indi.indID}:Married2 {marriage1.famID} & {marriage2.famID}"
                                error_list.append(error_string)                                    
                            
                            else:
                                if (date_Check(marriage2.Marriage, indDict[id_Spouse].Death)):
                                    error_string =f"ERROR: INDIVIDUAL: US11: {an_Indi.indID}:Married2 {marriage1.famID} & {marriage2.famID}"
                                    error_list.append(error_string)
                        else:
                            
                            if (date_Check(marriage2.Marriage, marriage1.Divorce)):
                                error_string = f"ERROR: INDIVIDUAL: US11: {an_Indi.indID}:Married2 {marriage1.famID} & {marriage2.famID}"
                                error_list.append(error_string)
            
            
                
    return error_list
    



def user_story11_main():
    list_errors =us11_no_bigamy("us11testdata.ged")
    for eacherror in list_errors:
        print(eacherror)

if __name__ == "__main__":
    user_story11_main()