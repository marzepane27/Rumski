def roman_to_int(s: str) -> int:
    roman_to_int_map = {
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

    for char in s:
        current_value = roman_to_int_map[char]
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value

    return total

# Приклад використання
print(roman_to_int("MCMXCIV"))  
print(roman_to_int("LVIII"))    
print(roman_to_int("IX"))       
