from ParserModule import parse_main
from prettytable import PrettyTable

def printTables(fileName):
    indDict, famDict = parse_main(fileName);
    indTable = PrettyTable()
    famTable = PrettyTable()
    
    indTable.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    #print(famDict)
    
    for iD in indDict:
        ind = indDict[iD]
        indTable.add_row(ind.details())
    
    #print(famDict)
    #print(famDict)
    print('\n\nIndividuals Information----------------------->\n')
    
    print (indTable)

    famTable.field_names = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
    #print(famDict)
    
    for famID in famDict:
        famObj= famDict[famID]
        childrenarr=[];
        for lin in famObj.multChild:
            childrenarr.append(lin.strip("@"))
        famObj.multChild=childrenarr
        famTable.add_row(famObj.details(indDict))
    
    #print(famDict)
    #print(famDict)
    print('\n\nFamily Information----------------------->\n')
    print (famTable)
    return indTable,famTable

if __name__ == "__main__":
    printTables("gedfilestest/sprint01-testdata_1.ged")