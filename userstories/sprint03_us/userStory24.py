from ParserModule import parse_main

from print_main import printTables


def us24_unique_fam_by_spouses(file):
    indDict, famDict, errorList = parse_main(file)
    
    error_list = list()
    
    mDate = []
    hName = []
    wName = []
    
    
    for fam in famDict:
        mDate.append(famDict[fam].Marriage)
        hName.append(famDict[fam].Husband)
        wName.append(famDict[fam].Wife)
        
    for fam in famDict:
        mDate1 = famDict[fam].Marriage
        hName1 = famDict[fam].Husband
        wName1 = famDict[fam].Wife
        
        if mDate1 in mDate:
            error_string = f"ERROR: US24 : {famDict[fam].famID} husband, wife names or marriage date is occurring twice in Gedcom "
            error_list.append(error_string)
            
        if hName1 in hName:
            error_string = f"ERROR: US24 : {famDict[fam].famID} husband, wife names or marriage date is occurring twice in Gedcom "
            error_list.append(error_string)
        
        if wName1 in wName1:
            error_string = f"ERROR: US24 : {famDict[fam].famID} husband, wife names or marriage date is occurring twice in Gedcom "
            error_list.append(error_string)                   
                         
    
    return error_list


def user_story24_main():
    error_list= us24_unique_fam_by_spouses("us24testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story24_main()