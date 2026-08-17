turno = input("Digite o turno que você estuda (M - Matutino, V - Vespertino, N - Noturno): ").upper()
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!") 
elif turno == "N":
    print("Boa noite!")
else:
    print("Turno inválido!")    