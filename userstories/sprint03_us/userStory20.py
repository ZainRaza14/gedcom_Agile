from ParserModule import parse_main

from print_main import printTables


def us20_aunts_and_uncles(file):
    indDict, famDict, errorList = parse_main(file)
    
    error_list = list()
    
    mFlag = False
    
    fFlag = False
    
    for fam in famDict:
        if(famDict[fam].multChild):
            for chil in famDict[fam].multChild:
                if chil in indDict:
                    mFlag = False
                    fFlag = False
                    if indDict[chil].Spouse:
                        if indDict[chil].Sex == 'M':
                            mFlag = True
                        else:
                            fFlag = True
                        
                        if mFlag == True:
                            spouseFam = indDict[chil].Spouse
                            spouseId = famDict[spouseFam].Wife
                            chilFather = famDict[fam].Husband
                            chilMother = famDict[fam].Wife
                            chilFatFam = indDict[chilFather].Child
                            chilMotFam = indDict[chilMother].Child
                            spouseParentFam = indDict[spouseId].Child
                            if chilFatFam == spouseParentFam or chilMotFam == spouseParentFam:
                                error_string = f"ERROR: US20 : {spouseId} is married to their nephew or niece"
                                error_list.append(error_string)
                            
                            
                        if fFlag == True:
                            spouseFam = indDict[chil].Spouse
                            spouseId = famDict[spouseFam].Husband
                            chilFather = famDict[fam].Husband
                            chilMother = famDict[fam].Wife
                            chilFatFam = indDict[chilFather].Child
                            chilMotFam = indDict[chilMother].Child
                            spouseParentFam = indDict[spouseId].Child
                            if chilFatFam == spouseParentFam or chilMotFam == spouseParentFam:
                                error_string = f"ERROR: US20 : {spouseId} is married to their nephew or niece"
                                error_list.append(error_string)
                        
                         
    
    return error_list


def user_story20_main():
    error_list= us20_aunts_and_uncles("us20testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story20_main()