

class Student:

    def __init__(self, studID, name, date_of_birth, classification, register):
        self.__StudentID = studID
        self.__Name = name 
        self.__dob = date_of_birth
        self.__Classification = classification
        self.__register = None
        self.__age = 0

    def get_age(self, dob):
        self.dob = '10/11/2001'
        self.dob = dob.split('/')
        dob_year = dob[2]
        self.get_age = year - dob_year

    
    def age(self, get_age):
        return self.__age


    def classification(self, Classification, register):
        self.Classification = [F, S, Jr, Sr]
        if self.Classification == F:
            self.register = '4/10 thru 4/12'
        if self.Classification == S:
            self.register = '4/7 thru 4/9'
        if self.Classification == Jr:
            self.register = '4/4 thru 4/6'
        if self.Classification == Sr:
            self.register = '4/1 thru 4/3'

    def return_age()

              

        
