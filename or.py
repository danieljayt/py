    
nome= input("come ti chiami?")
print("ciao", nome)

scritto = input("hai superato la prova scritta?")
if scritto == "si":
    scritto = True
else:
    scritto = False
orale= input("hai superato la prova orale?")
if orale == "si":
    orale = True
else:
    orale = False
    
print("prof bravo")
if scritto or orale:
    print("hai superato lesame.")
else:
    print("mi dispiace ma non hai superato l'esame.")
    
print("prof cattivo")
if scritto and orale:
    print("hai superato lesame.")
    
else:
    print("mi dispiace ma non hai superato l'esame.")
    