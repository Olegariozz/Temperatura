# 📜 Descrição do Código

Este código em Python solicita ao usuário uma temperatura em graus Celsius e informa se está muito frio, normal, quente ou muito quente, de acordo com o valor informado.

## 🚀 Como funciona
1. O programa pede ao usuário:
   - Temperatura em Celsius (`input` convertido para `float`)
2. Usa uma estrutura condicional (`if`, `elif`, `else`) para verificar:
   - **Menor que 10°C** → "Está muito frio!"
   - **Entre 10°C e 19,99°C** → "Está Normal!"
   - **Entre 20°C e 29,99°C** → "Está Quente!"
   - **Maior ou igual a 30°C** → "Está muito quente!"
3. Ao final, exibe a mensagem "Obrigado por usar o sistema de temperatura!".

## 📌 Código
```python
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
```

## 🖥️ Exemplo de uso
**Entrada:**
```
Digite a temperatura em Celsius: 25
```

**Saída:**
```
Está Quente!
Obrigado por usar o sistema de temperatura!
```

## 🛠️ Observações
- O valor digitado é convertido para `float` para permitir casas decimais.
- As condições são avaliadas em ordem, e apenas a primeira que for verdadeira será executada.
- O programa cobre qualquer valor de temperatura que
