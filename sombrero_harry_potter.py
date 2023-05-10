import random

# gryffindor : valor
# hufflepuff : lealtad
# ravenclaw : sabiduria
# slytherin : ambicion

class HatQuestion:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
def get_answer():
    answer = input("Reponde 1, 2, 3 o 4: ")
    if answer == "1" or answer == "2" or answer == "3" or answer == "4":
        return int(answer)    
    else:
        return get_answer()

hat_question = HatQuestion("Como te definirias?", 
                           [("1. Valiente"),
                            ("2. Leal"),
                            ("3. Sabio"), 
                            ("4. Ambicioso")]),
HatQuestion("Cual es tu clase favorita?", 
                            [("1. Vuelo", "gryffindor"),
                            ("2. Pociones", "ravenclaw"),
                            ("3. Defensa contra las artes oscuras", "slytherin"),
                            ("4. Anumales fantasticos", "hufflepuff")])
houses = {"gryffindor" : 0,
          "hufflepuff" : 0,
          "ravenclaw" : 0,
          "slytherin" : 0}


for hat_question in hat_question:
    
    print(hat_question.question)
    for answer in hat_question.answer:
        print(hat_question.answer[0])
    
    house = hat_question.answer[get_answer() - 1][1]
    house[house] += 1
    
    print()
    
print(houses)

selecte_house = ""

max_points = 0

for house, points in houses.items():
    if points > max_points:
        selecte_house.clear()
        selecte_house.append(house)
        max_points = points
    elif points == max_points:
        selecte_house.append(house)
        max_points = points
        

if len (selecte_house) == 1:
    print(f"Lo tengo claro ... !{selecte_house[0].capitalize()}!")
else:
    print(f"Ha esatdo complicado ... !{random.choice.capitalize()}!")