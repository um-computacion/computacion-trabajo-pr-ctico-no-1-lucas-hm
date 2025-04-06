from test import test_roman_converter
print("convertidor de numeros a numeros romanos")
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

numero = int(input("ingresa un numero y luego se convertira a romano desde otra carpeta: "))

def decimal_to_roman(number: int) -> str:
    if not (1 <= number <= 3999):
        raise ValueError("El número debe estar entre 1 y 3999")

    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    roman_numeral = []
    for value, symbol in roman_map:
        while number >= value:
            roman_numeral.append(symbol)
            number -= value
    return "".join(roman_numeral)