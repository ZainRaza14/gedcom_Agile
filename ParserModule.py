from collections import OrderedDict
from prettytable import PrettyTable
import datetime


from famClass import famClass
from indClass import indClass

def dateFormating(myDate):
    myMonths = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}
    myDate = myDate.split()
    if int(myDate[0]) in range(1,10):
        finalDay = '0' + myDate[0]
    else:
        finalDay = myDate[0]
    finalMonth = myMonths[myDate[1]]
    finalYear = myDate[2]
    return (finalYear + '-' + finalMonth + '-' + finalDay)



def addAges(indDict):
    for iD in indDict: 
        if indDict[iD].Birthday != 'NA':
            if indDict[iD].Death == 'NA':
                start = datetime.datetime.strptime(indDict[iD].Birthday, "%Y-%m-%d")
                #print(start)
                end = datetime.date.today()
                #print(end)
                finalAge = end.year - start.year - ((end.month, end.day) < (start.month, start.day))
                indDict[iD].ageSet(finalAge)
                #print(finalAge)
            else:
                start = datetime.datetime.strptime(indDict[iD].Birthday, "%Y-%m-%d")
                #print(start)
                end = datetime.datetime.strptime(indDict[iD].Death, "%Y-%m-%d")
                #print(end)
                finalAge = end.year - start.year - ((end.month, end.day) < (start.month, start.day))
                indDict[iD].ageSet(finalAge)
                #print(finalAge)

def addAlives(indDict):
    #alive = True
    for iD in indDict:
        if(indDict[iD].Death != 'NA'):
            indDict[iD].aliveSet(False)
        else:
            #alive
            indDict[iD].aliveSet(True)
    
 
def parse_main(fileName):
    myFile = open(fileName)
    indDict = OrderedDict()
    famDict = OrderedDict()
    myFlag = ''
    myFlag1 = ''
    myFlag2 = ''
    try:
        for line in myFile:
            lineData = line.strip().split(" ")
            if lineData[0]:
                myLevel = lineData[0]
                myTag = lineData[1]
                #print(f"check myTag {myTag}")
                myArg = lineData[2:]
                myArg1 = " ".join(myArg)
                if myArg1 == 'INDI' or myArg1 == 'FAM':
                    if myLevel == '0':
                        myFlag = myTag
                        if myArg1 == 'INDI':
                            indDict[myFlag] = indClass(myTag)
                        elif myArg1 == 'FAM':
                            famDict[myFlag] = famClass(myTag)
                if myLevel == '1':
                    #print(myTag)
                    if (myTag == 'NAME'):
                        #print(myArg1)
                        indDict[myFlag].nameSet(myArg1)
                    elif (myTag == 'SEX'):
                            indDict[myFlag].sexSet(myArg1)
                    elif (myTag == 'BIRT'):
                            myFlag1 = 'Birthday'
                    elif (myTag == 'DEAT'):
                            myFlag1 = 'Death'
                    elif (myTag == 'FAMC'):
                            indDict[myFlag].childSet(myArg1)
                    elif (myTag == 'FAMS'):
                            indDict[myFlag].spouseSet(myArg1)
                    elif (myTag == 'HUSB'):
                            famDict[myFlag].husbandSet(myArg1)
                    elif (myTag == 'WIFE'):
                            famDict[myFlag].wifeSet(myArg1)
                    elif (myTag == 'CHIL'):
                            famDict[myFlag].multChildSet(myArg1)
                    elif (myTag == 'MARR'):
                            myFlag1 = 'Marriage'
                    elif (myTag == 'DIV'):
                            myFlag1 = 'Divorce'
                elif myLevel == '2':
                    if myTag == 'DATE':
                        if (myFlag1 == 'Birthday'):
                            indDict[myFlag].birthdaySet(myArg1)
                        elif (myFlag1 == 'Death'):
                            indDict[myFlag].deathSet(myArg1)
                        elif (myFlag1 == 'Marriage'):
                            myHusb = famDict[myFlag].husbandGet()
                            myWif = famDict[myFlag].wifeGet()
                            if(myHusb !="NA"):
                                indDict[myHusb].marriageSet(myArg1)
                            if(myWif !="NA"):
                                indDict[myWif].marriageSet(myArg1)
                            famDict[myFlag].marriageSet(myArg1)
                        elif (myFlag1 == 'Divorce'):
                            myHusb = famDict[myFlag].husbandGet()
                            myWif = famDict[myFlag].wifeGet()
                            if myHusb != "NA":
                                indDict[myHusb].divorceSet(myArg1)
                            if myWif != "NA":
                                indDict[myWif].divorceSet(myArg1)
                            if myFlag != "NA":
                                famDict[myFlag].divorceSet(myArg1)
        addAges(indDict)
        addAlives(indDict)
    finally:
        myFile.close()
    return indDict, famDict

