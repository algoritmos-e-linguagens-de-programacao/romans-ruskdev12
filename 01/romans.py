def int_to_roman(num):
    sub = num
    resultado = ""

    while sub != 0:
        if sub == 4:
            resultado += "IV"
            sub -= 4
        elif sub == 9:
            resultado += "IX"
            sub -= 9
        elif sub >= 40 and sub < 50:
            resultado += "XL"
            sub -= 40
        elif sub >= 90 and sub < 100:
            resultado += "XC"
            sub -= 90
        elif sub >= 400 and sub < 500:
            resultado += "CD"
            sub -= 400
        elif sub >= 900 and sub < 1000:
            resultado += "CM"
            sub -= 900
        elif sub == 1:
            resultado += "I"
            sub -= 1
        elif sub < 5:
            resultado += "I"
            sub -= 1
        elif sub < 10:
            resultado += "V"
            sub -= 5
        elif sub < 50:
            resultado += "X"
            sub -= 10
        elif sub < 100:
            resultado += "L"
            sub -= 50
        elif sub < 500:
            resultado += "C"
            sub -= 100
        elif sub < 1000:
            resultado += "D"
            sub -= 500
        elif sub >= 1000:
            resultado += "M"
            sub -= 1000
            
    return resultado

def roman_to_int(s):
    roman_to_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        current_value = roman_to_value[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value

    return total
