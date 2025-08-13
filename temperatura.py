temperatura = float(input("Digite a temperatura em Celsius: "))
if temperatura < 10:
    print("Está muito frio!")
elif temperatura < 20:
    print("Está Normal!")
elif temperatura < 30:
    print("Está Quente!")

else:
    print("Está muito quente!")
print("Obrigado por usar o sistema de temperatura!")