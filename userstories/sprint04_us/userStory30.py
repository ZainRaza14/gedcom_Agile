from ParserModule import parse_main
from utils import compare_date_to_todays_date,checkDiffInMonths
from print_main import printTables_indData
from print_main import printTables
import operator
import collections

'''
US30 List all living married people in a GEDCOM file
'''

def us30_list_living_married(file):
    error_list = list()
    printTables(file)
    indDict,famDict,errorList = parse_main(file)
    newindDict = dict()
    for key,indData in indDict.items():
        indId= key;
        if indData.Alive == True and indData.Spouse!='NA':
            newindDict[key]= indData
    print('\n\nAfter filtering Individuals Information with condition living married people ----------------------->\n')
    printTables_indData(newindDict);
    return newindDict
    


def user_story30_main():
    newindDict= us30_list_living_married("us30testdata.ged")


if __name__ == "__main__":
    user_story30_main()