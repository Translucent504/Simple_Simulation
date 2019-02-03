# TODO: need to add more to the person class
#  what things should they be able to do?
#  what are all of their characteristics?
import random, datetime
from pathlib import Path


class Person:
    def __init__(self, name=None, gender=None,adult_height=None, adult_weight=None, ethnicity=None, reproductive_age=None, age=0):
        possible_genders = ['Male',"Female"]
        possible_ethnicities = ["European", "African-American", "African", "Asian", "Latino", "Jewish", "Arab", "Indigenous"] #TODO: make ethnicities more abstract
        self.age = age
        if gender:
            self.gender = gender
        else:
            self.gender = random.choice(possible_genders)
        if reproductive_age:
            self.reproductive_age = reproductive_age
        else:
            if self.gender == "Male":
                self.reproductive_age = round(random.uniform(13,17), 1)
            elif self.gender == "Female":
                self.reproductive_age = round(random.uniform(11,16), 1)
        if name:
            self.name = name
        else:
            self.name = self.pickName(self.gender)
        if ethnicity:
            self.ethnicity = ethnicity
        else:
            self.ethnicity = random.choice(possible_ethnicities)
        if adult_height:
            self.adult_height = adult_height
        else:
            if self.gender == "Male":
                self.adult_height = round(random.uniform(1.6,2.1), 1) # Height is in Meters.
            elif self.gender == "Female":
                self.adult_height = round(random.uniform(1.5,1.9), 1) # Height is in Meters.
        if adult_weight:
            self.adult_weight = adult_weight
        else:
            if self.gender == "Male":
                self.adult_weight = round(random.uniform(50,110), 1) # Weight is in Kilograms
            elif self.gender == "Female":
                self.adult_weight = round(random.uniform(50,100), 1) # Weight is in Kilograms
        self.height = round(random.uniform(0.4, 0.6), 1) # Height is in Meters.    
        self.weight = round(random.uniform(2.5, 4.5), 1) # Weight is in Kilograms

    def pickName(self, gender):
        """
        Input: gender, one of : 'male' , 'female'
        Output: A random full name  (string)
        Example use:
        pickName('female') will return a female name as string.
        """
        def load_names(rel_path_name, filename):
            """
            Input: Name of file that contains a single name per line (string)
            Output: List of all the names in file with \n removed from the end (string list)
            """
            namelist = []
            script_location = Path(rel_path_name).absolute().parent
            # print(script_location)            print debugging for if weird path errors are thrown.
            file_location = script_location / filename
            # print(file_location)            print debugging for if weird path errors are thrown.
            with open(file_location, 'r') as f:
                for line in f:
                    namelist.append(line.strip('\n'))
            return namelist
            
        if gender.lower() == 'male':
            firstnames = load_names('.\\sim_objs\\person\\male_firstnames.txt', 'male_firstnames.txt')
        elif gender.lower() == 'female':
            firstnames = load_names('.\\sim_objs\\person\\female_firstnames.txt', 'female_firstnames.txt')
        else:
            return "NO GENDER"
        lastnames = load_names('.\\sim_objs\\person\\lastnames.txt', 'lastnames.txt')
        # Sizes of the firstnames and lastnames lists:
        first = random.choice(firstnames)
        last = random.choice(lastnames)
        fullname = ''.join((first,' ', last))
        return fullname

    def getInfo(self):
        print(f'{self.name} is {self.age} years old, is a {self.gender}, and is {self.ethnicity}. They are {self.height} meters tall, and {self.weight} kilograms. They will reach their reproductive age at {self.reproductive_age} years old.')

    def age_up(self):
        self.age = float(self.age)
        self.age += (1/365)
        if self.age < 1:
            print(f'{self.name} is {round(self.age * 365)} days old.')
        else:
            print(f'{self.name} is {round(self.age, 1)} years old.')

def breed(person1, person2):
    if person1.age >= person1.reproductive_age and person2.age >= person2.reproductive_age:
        if person1.gender != person2.gender:
            if person1.gender != "Male":
                person1, person2 = person2, person1
            ethnicity = random.choice((person1.ethnicity,person2.ethnicity)) #TODO: make ethnicities more abstract
            gender = random.choice(['Male',"Female"])
            if gender == "Male":
                adult_height = round((person1.adult_height + person2.adult_height+13)/2,1)
                adult_weight = round((person1.adult_weight+person2.adult_weight+13)/2,1)
                reproductive_age = round((person1.reproductive_age+person2.reproductive_age+3))
            elif gender == "Female":
                adult_height = round((person1.adult_height + person2.adult_height-13)/2,1)
                adult_weight = round((person1.adult_weight+person2.adult_weight-13)/2,1)
                reproductive_age = round((person1.reproductive_age+person2.reproductive_age-3))
            

            return Person(gender=gender, adult_height=adult_height,adult_weight=adult_weight, ethnicity=ethnicity, reproductive_age=reproductive_age)

'''     
Test1 = Person()
Test2 = Person()
Test3 = Person()

Test1.getInfo()
Test2.getInfo()
Test3.getInfo()

#Uncomment these lines to test Person Function.
'''