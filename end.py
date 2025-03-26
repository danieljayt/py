
nome= input("come ti chiami?")
print("ciao", nome)

eta= int(input("quanti anni hai?"))

invito= input("hai l'invito?")
if invito == "si":
    invito = True
else:
    invito = False
    
if eta >= 18 and invito:
    print("caio", nome, "benvenuto al club dei programmatori.")
    
elif eta < 18 and invito:
        print("Mi dispiace", nome, "non sei maggiornne.")
elif eta >= 18 and not invito:
    print("Mi dispiace", nome, "non puoi entrare, non sei stato invitato.")
else:
    print("Mi dispiace", nome, "non puoi entrare, non hai 18 anni ne hai l'invito.")