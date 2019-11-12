from ParserModule import parse_main
from utils import compare_date_to_todays_date,checkDiffInMonths
from print_main import printTables_custom
import operator
import collections

'''
US28 Siblings should not marry one another
'''
def us28_order_sibilings_by_age(file):
    error_list = list()
    indDict,famDict,errorList = parse_main(file)
    for key,familyData in famDict.items():
        children = familyData.multChild
        id_age_dict = dict();
        for eachchild in children:
            child_id = eachchild
            age = indDict[child_id].Age
            id_age_dict[child_id] = age; 
        sorted_x = sorted(id_age_dict.items(), key=operator.itemgetter(1),reverse=True)
        keys= collections.OrderedDict(sorted_x).keys();
        familyData.multChild= keys
    famData= list(famDict.values())[0]
    multiChild= famData.multChild
    error_string= f"US28: The list of sibilings in sorting order according to their age are {list(multiChild)}"
    error_list.append(error_string)
    #print('\n\n After sorting sibilings in Descending order\n')
    #printTables_custom(indDict,famDict)
    return error_list

        
def user_story28_main():
    famDict= us28_order_sibilings_by_age("us28testdata.ged")


if __name__ == "__main__":
    user_story28_main()