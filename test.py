numbers = input().split(" ")

def triangle(num, num2):
    return (float(num)*float(num2))/2

def circle(num):
    return 3.14159*(float(num)**2)

def trapezium(num, num2, num3):
    return ((float(num) + float(num2))*float(num3))/2
    
def square(num):
    return float(num)**2
    
def rectangle(num, num2):
    return float(num)*float(num2)
dict_values = {"TRIANGULO": triangle(numbers[0], numbers[2]),"CIRCULO": circle(numbers[2]), "TRAPEZIO": trapezium(numbers[0], numbers[1], numbers[2]), "QUADRADO": square(numbers[1]), "RETANGULO": rectangle(numbers[0], numbers[1])}
for forma, area in dict_values.items():
    print(f"{forma}: {area:.3f}")