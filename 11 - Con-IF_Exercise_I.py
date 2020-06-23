print("Este programa pide dos numeros y evalua cual es mayor")
num1 = int(input("Ingresa el primer numero a evaluar: "))
num2 = int(input("Ingresa el segundo numero a evaluar: "))

def DevuelveMax(num1, num2):
   
    if num1 < num2:
        print(num2)
    elif num2 < num1:
        print(num1)
    else:
        print("Son iguales")

print("El numero mas alto es: ")
DevuelveMax(num1, num2)



