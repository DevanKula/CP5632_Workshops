class ProgrammingLanguage:
    def __init__(self, program = str, typing = str, reflection = bool, year = int):
        self.program = program
        self. typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        #return "{}, {} Typing, Reflection ={}, First appeared in {}".format(self.program,self.typing,self.reflection, self.year)
        return self.program
