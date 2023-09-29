email = input("escribe un mail: ")

for i in email:
    if i == "@":
        arroba = True
        break

else:
    arroba = False
    
print(arroba)