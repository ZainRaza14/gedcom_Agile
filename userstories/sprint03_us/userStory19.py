# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 02:20:40 2019

@author: NEIL
"""


from ParserModule import parse_main
from print_main import printTables


def us19_no_1st_cousin_marr(file):
    printTables(file)
    indDict,famDict,errorList = parse_main(file)
    error_list=list()
    for famID in famDict:
        fatherhusband=0;
        motherhusband=0;
        fatherwife=0;
        motherwife=0;
        famfatherhusband=0;
        fammotherhusband=0;
        famfatherwife=0;
        fammotherwife=0;
        grandmotherwife=0;
        grandmotherhusband=0;
        grandfatherwife=0;
        grandfatherhusband=0
        husband=famDict[famID].Husband
        wife=famDict[famID].Wife
        for iD in indDict:
            if indDict[iD].indID==husband:
                famhusband=indDict[iD].Child
               
            if indDict[iD].indID==wife:
                famwife=indDict[iD].Child
                
        for famID in famDict:
            if famhusband != 'NA' and famwife != 'NA':
                if famDict[famID].famID==famhusband:
                    fatherhusband=famDict[famID].Husband
                    
                    motherhusband=famDict[famID].Wife
                    
                if famDict[famID].famID==famwife:
                    fatherwife=famDict[famID].Husband
                    
                    motherwife=famDict[famID].Wife
                    
        for iD in indDict:
            
            if indDict[iD].indID==fatherhusband:
                famfatherhusband=indDict[iD].Child
                
            if indDict[iD].indID==motherhusband:
                fammotherhusband=indDict[iD].Child
                
            if indDict[iD].indID==fatherwife:
                famfatherwife=indDict[iD].Child
                
            if indDict[iD].indID==motherwife:
                fammotherwife=indDict[iD].Child
                
        for famID in famDict:
            if famfatherhusband is not None:
                if famDict[famID].famID==famfatherhusband:
                    grandfatherhusband=famDict[famID].Husband
                   
            if fammotherhusband is not None:        
                if famDict[famID].famID==fammotherhusband:
                    grandmotherhusband=famDict[famID].Wife
                    
            if famfatherwife is not None:    
                if famDict[famID].famID==famfatherwife:
                    grandfatherwife=famDict[famID].Husband
                    
            if fammotherwife is not None:        
                if famDict[famID].famID==fammotherwife:
                    grandmotherwife=famDict[famID].Wife
                    
        
        if grandmotherwife==grandmotherhusband!=0 or grandfatherhusband==grandfatherwife!=0:
            error_string = f"ERROR: FAMILY: US19: The two first cousins {husband} and {wife} cannot be married together"
            error_list.append(error_string)
                
    return error_list


def user_story19_main():
    error_list= us19_no_1st_cousin_marr("us19testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story19_main()