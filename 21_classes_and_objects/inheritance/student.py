from person import Person

class Student(Person):
    # Inheritance
    
    def __init__(
        self,
        firstname="Mike",
        lastname="Simpson",
        age=25,
        country="UK",
        city="London",
        gender="male"
    ):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = "He" if self.gender == "male" else "She"
        return f"{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}."


s1 = Student("Chad", "Smith", 25, "USA", "New York", "male")
print(s1.person_info())
s1.add_skill("JavaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)

s2 = Student("Lidiya", "Teklemariam", 28, "Finland", "Espoo", "female")
print(s2.person_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Marketing")
print(s2.skills)
