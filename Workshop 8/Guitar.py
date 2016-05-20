class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{:>15} ({}) worth $ {:10,.2f} {}".format(self.name,self.year,float(self.cost),self.is_vintage())

    def get_age(self):
        age = 2015 - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return "(is vintage)"
        else:
            return ""



