

class Student:

    def __init__(self, studID, name, date_of_birth, classification, register):
        self.__StudentID = studID
        self.__Name = name 
        self.__dob = date_of_birth
        self.__Classification = classification
        self.__register = None
        self.__stu_age = 0

    def get_age(self, dob, stu_age):
        self.__dob = '10/11/2001'
        self.__dob = dob.split('/')
        self.__dob_year = dob[2]
        self.__stu_age = year - dob_year


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

    
    def age(self):
        return self.__stu_age
    
    def registration_date(self):
        return self.__register
              

        
