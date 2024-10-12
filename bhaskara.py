import math

a = 0  
while a == 0 or delta < 0:
    a = float(input("Digite o valor de a (não pode ser 0): "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    if a == 0:
        print("O valor de 'a' deve ser diferente de 0. Tente novamente.")
        continue  # Volta ao início do loop
    
    delta = b**2 - 4*a*c


    if delta < 0:
        print("Delta negativo. A equação não possui raízes reais. Tente novamente.")
        continue


raiz_delta = math.sqrt(delta)
x1 = round(-b + raiz_delta) / (2 * a)
x2 = round(-b - raiz_delta) / (2 * a)

print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")
