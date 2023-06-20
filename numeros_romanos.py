#
"""
Dado un número romano, conviértalo en un número entero.
"""
def romanToInt(s):
    # Crear un diccionario para mapear los símbolos romanos a sus valores numéricos
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    
    # Recorrer la cadena de derecha a izquierda
    for i in range(len(s)-1, -1, -1):
        current_value = roman_values[s[i]]
        
        # Verificar si se debe restar o sumar el valor actual
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        # Actualizar el valor previo para la siguiente iteración
        prev_value = current_value
    
    return total
