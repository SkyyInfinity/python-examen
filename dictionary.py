import json

# --------------------------
# A class to get informations about a person.
# --------------------------
class Dictionary:
    # Properties
    firstName = ""
    lastName = ""
    genre = 0
    age = 0
    isMajor = False

    # --------------------------
    # Constructor
    # --------------------------
    def __init__(
        self, 
        firstName = "John", 
        lastName = "Doe", 
        genre = 0, # 0 = Male / 1 = Female
        age = 32,
    ):
        self.firstName = firstName
        self.lastName = lastName
        self.genre = genre
        self.age = age
        self.isMajor = True if self.age >= 18 else False

        print(self.show_dictionary(firstName = self.firstName, lastName = self.lastName, genre = self.genre, age = self.age, isMajor = self.isMajor))

    # --------------------------
    # Show dictionary from a person
    #
    # :param firstName string
    # :param lastName string
    # :param genre int
    # :param age int
    # :param isMajor bool
    # :return string 
    # --------------------------
    def show_dictionary(self, firstName, lastName, genre, age, isMajor):
        toJson = {
            "firstName": firstName,
            "lastName": lastName,
            "genre": "Male" if genre == 0 else "Female",
            "age": age,
            "isMajor": "Yes" if isMajor == True else "No"
        }

        return json.dumps(toJson, indent = 4)

Dictionary(firstName="Jane", genre=1, age=17)
