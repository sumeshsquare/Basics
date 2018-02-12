class Person:

    def setFullName(chef, firstName, lastName):
        chef.firstName = firstName
        chef.lastName = lastName

    def prinFullName(chef):
        print(chef.firstName, chef.lastName)


personName = Person()
personName.setFullName("Sumesh", "S")
personName.prinFullName()
