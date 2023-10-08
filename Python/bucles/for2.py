email = False
miEmail = input("Introduce tu dirección de e-mail: ")
for i in miEmail:
    if i == '@' and '.' in miEmail:

        email = True

if email == True:
    print("email correcto")
else:
    print("email incorrecto")
