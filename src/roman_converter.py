class decimal_to_roman:
    @staticmethod
    def decimal_to_roman(number):
        """
        Convierte un número decimal a romano (1-3999).
        Ejemplo: 4 → 'IV'
        """
        if not isinstance(number, int) or number < 1 or number > 3999:
            raise ValueError("Número debe ser entero entre 1 y 3999")

        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman_num = ''
        i = 0
        while number > 0:
            if number >= val[i]:
                roman_num += syb[i]
                number -= val[i]
            else:
                i += 1
        return roman_num

    @staticmethod
    def from_roman(roman):
        """
        Convierte un número romano a decimal.
        Ejemplo: 'IV' → 4
        """
        if not isinstance(roman, str):
            raise ValueError("Debe ingresar una cadena")

        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman = roman.upper()
        
        for char in roman:
            if char not in roman_map:
                raise ValueError(f"Carácter inválido: '{char}'")

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