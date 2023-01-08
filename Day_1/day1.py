file = open("C:/Users/edgar/Documents/python/AdventOfCode22/Day_1/elfes_data.txt", "r")

lista = [0] * 3
cal = 0

for line in file:
    if line != "\n":
        cal += int(line)
    else:
        if lista[0] < cal:
            if lista[1] < cal:
                if lista[2] < cal:
                    lista[0] = lista[1]
                    lista[1]  = lista[2]
                    lista[2] = cal
                else:
                    lista[0] = lista[1]
                    lista[1] = cal
            else:
                lista[0] = cal
            
        cal = 0

print(lista)
