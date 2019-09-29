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

class indClass(object):
    def __init__(self, indID = 'NA', Name = 'NA', Marriage = 'NA', Divorce = 'NA', Sex = 'NA', Alive = 'NA', Death = 'NA', Age = '0', Child = 'NA', Spouse = 'NA', Birthday = 'NA'):
        self.indID =  indID
        self.Name = Name
        self.Marriage = Marriage
        self.Divorce = Divorce
        self.Sex = Sex
        self.Alive = Alive
        self.Death = Death
        self.Age = Age
        self.Child = Child
        self.Spouse = Spouse
        self.Birthday = Birthday
        
    def nameSet(self, Name):
        self.Name = Name 
        
    def marriageSet(self, Marriage):
        Marriage = dateFormating(Marriage)
        self.Marriage = Marriage
        
    def divorceSet(self, Divorce):
        Divorce = dateFormating(Divorce)
        self.Divorce = Divorce
        
    def sexSet(self, Sex):
        self.Sex = Sex
        
    def deathSet(self, Death):
        Death=dateFormating(Death)
        self.Death = Death
        
    def ageSet(self, Age):
        self.Age = Age
        
    def childSet(self, Child):
        self.Child = Child
        
    def spouseSet(self, Spouse):
        self.Spouse = Spouse
        
    def birthdaySet(self, Birthday):
        Birthday = dateFormating(Birthday)
        self.Birthday = Birthday
        
    def aliveSet(self, Alive):
        self.Alive = Alive
        
    def nameGet(self):
        return self.Name
        
    def marriageGet(self):
        return self.Marriage
        
    def divorceGet(self):
        return self.Divorce
        
    def sexGet(self):
        return self.Sex
        
    def deathGet(self):
        return self.Death
    
    def aliveGet(self):
        return self.Alive
        
    def ageGet(self):
        return self.Age
        
    def childGet(self):
        return self.Child
        
    def spouseGet(self):
        return self.Spouse
        
    def birthdayGet(self):
        return self.Birthday
    
    def details(self):
        return [self.indID, self.Name, self.Sex, self.Birthday, self.Age, self.Alive, self.Death, self.Child.strip('@'), self.Spouse.strip('@')]
    



