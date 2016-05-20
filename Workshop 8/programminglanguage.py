class ProgrammingLanguage:
    def __init__(self, program, typing, reflection, year):
        self.program = program
        self. typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):

        return "{}".format(self.program)
        #return "{}, {} Typing, Reflection ={}, First appeared in {}".format(self.program,self.typing,self.reflection, self.year)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False


