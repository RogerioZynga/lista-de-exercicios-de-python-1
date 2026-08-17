medidor = [0, 0, 0, 0, 0]
if input("Telefonou para a vítima? (S/N): ").upper() == "S":
  medidor[0] = 1
if input("Esteve no local do crime? (S/N): ").upper() == "S":
  medidor[1] = 1
if input("Mora perto da vítima? (S/N): ").upper() == "S":
  medidor[2] = 1
if input("Devia para vítima? (S/N): ").upper() == "S":
  medidor[3] = 1
if input("Já trabalho com a vítima? (S/N): ").upper() == "S":
  medidor[4] = 1

if sum(medidor) == 5:
  print("Assassino")
elif sum(medidor) >= 3:
  print("Cúmplice")
elif sum(medidor) == 2:
  print("Suspeito")
else:
  print("Inocente")