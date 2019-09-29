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

class famClass(object):
    
    def __init__(self, famID = 'NA', Divorce = 'NA', Husband = 'NA', Marriage = 'NA', Wife = 'NA' ):
        self.famID = famID
        self.Divorce = Divorce
        self.Husband = Husband
        self.multChild = []
        self.Marriage = Marriage
        self.Wife = Wife
        
    def divorceSet(self, Divorce):
        Divorce = dateFormating(Divorce)
        self.Divorce = Divorce
        
    def husbandSet(self, Husband):
        self.Husband = Husband
        
    def marriageSet(self, Marriage):
        Marriage = dateFormating(Marriage)
        self.Marriage = Marriage
        
    def multChildSet(self, multChild):
        self.multChild.append(multChild)
        
    def wifeSet(self, Wife):
        self.Wife = Wife
        
    def divorceGet(self):
        return self.Divorce
        
    def husbandGet(self):
        return self.Husband
        
    def marriageGet(self):
        return self.Marriage
        
    def wifeGet(self):
        return self.Wife

    def details(self,indDict):
        return [self.famID, self.Marriage, self.Divorce, self.Husband, indDict[self.Husband].Name, self.Wife, indDict[self.Wife].Name,self.multChild]
    
    def __str__(self):
        return f"famID: {self.famID} Marriage: {self.Marriage} Divorce:{self.Divorce} Husband ID: {self.Husband} Wife ID: {self.Wife}"
    