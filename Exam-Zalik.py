file = open("poem.txt", "r", encoding="utf-8")
word = input("Введіть слово для пошуку:")
s = " "
count = 1

L = file.readlines()

for i in L:
    L2 = i.split()
    if word in L2:
        print("Номер абзацу", count, ":", i)
    
    count+=1