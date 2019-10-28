# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:24:33 2019

@author: NEIL
"""

from ParserModule import parse_main
from print_main import printTables


def us22_unique_IDs(file):
    printTables(file)
    indDict,famDict,errorList = parse_main(file)
    error_list=list()
    errorList=list(errorList)
    if errorList:
        error_string=f"ERROR: US22 : The ids:{errorList} are repeated"
        error_list.append(error_string)
    return error_list


def user_story22_main():
    error_list= us22_unique_IDs("us22testdata.ged")
    for eacherror in error_list:
        print(eacherror)

if __name__ == "__main__":
    user_story22_main()