from random import randint, choice

No = 1
languages = ["Python", "C++", "C#", "Java"]
sorted_students = {}

with open("data.csv", "w") as datafile:
    datafile.write("No, Student, Age, Grade, Sex, Prog. Language\n")
    while No < 201:
        string = f"{No}, student{No}, "
        age = randint(13, 16)
        if age == 13:
            grade = randint(8, 9)
        elif age == 14:
            grade = randint(9, 10)
        elif age == 15:
            grade = randint(10, 11)
        else:
            grade = 11
        sex = choice(["m", "fm"])
        language = choice(languages)
        string += f"{age}, {grade}, {sex}, {language}\n"
        datafile.write(string)
        No += 1

with open("data.csv", "r") as datafile:
    next(datafile)
    for line in datafile:
        text = line.split(", ")
        text[5] = text[5][:-1]
        if text[3] not in sorted_students:
            sorted_students[text[3]] = {}
        if text[3] in sorted_students:
            if text[5] not in sorted_students[text[3]]:
                sorted_students[text[3]][text[5]] = []
            sorted_students[text[3]][text[5]].append(text)
    sorted_students = dict(sorted(sorted_students.items(), key = lambda item: int(item[0])))
for key in sorted_students:
    print(f"{key} :")
    for key1 in sorted_students[key]:
        print(f"    {key1} :")
        for student in sorted_students[key][key1]:
            print(f"        {student}")