from programminglanguage import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1995)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print("The dynamically typed languages are:")
    for language in [python,ruby,vb]:
        if language.is_dynamic():
            print(language)

main()