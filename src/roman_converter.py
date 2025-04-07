class decimal_to_roman:
    @staticmethod
    def decimal_to_roman(number):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while number > 0:
            for _ in range(number // val[i]):
                roman_num += syb[i]
                number -= val[i]
            i += 1
        return roman_num

    @staticmethod
    def from_roman(roman):
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        prev_value = 0
        for char in reversed(roman):
            value = roman_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result