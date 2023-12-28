from PetHome import Cat

Cat1 = Cat("Барон", "male", 2)
Cat2 = Cat("Сэм", "male", 2)

print("Имя первого кота ", Cat1.name)
print("Пол первого кота: ", Cat1.gender)
print("Возраст первого кота: ", Cat1.age)
print("---")

print("Имя второго кота: ", Cat2.CatName())
print("Пол второго кота: ", Cat2.CatGender())
print("Возраст второго кота: ", Cat2.CatAge())
