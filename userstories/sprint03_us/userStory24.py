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
        hName.append(indDict[famDict[fam].Husband].Name)
        wName.append(indDict[famDict[fam].Wife].Name)
       
    
    if len(mDate) != len(set(mDate)):
        error_string = f"ERROR: US24 : husband, wife names or marriage date is occurring twice in Gedcom "
        error_list.append(error_string)
    
    if len(hName) != len(set(hName)):
        error_string = f"ERROR: US24 : husband, wife names or marriage date is occurring twice in Gedcom "
        error_list.append(error_string)                  
      
    if len(wName) != len(set(wName)):
        error_string = f"ERROR: US24 : husband, wife names or marriage date is occurring twice in Gedcom "
        error_list.append(error_string)  
    
    return error_list


def user_story24_main():
    error_list= us24_unique_fam_by_spouses("us24testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story24_main()