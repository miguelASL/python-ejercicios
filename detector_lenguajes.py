from langdetect import detect

def detect_language(text):
    try:
        return detect(text)
    except:
        return "Error en la deteccion del idioma"
    
#Test
text= "Hola como estan los maquinas?"
print(detect_language(text))

text= "Hello, How are you?"
print(detect_language(text))

text= "Bonjour, comment allez-vous"
print(detect_language(text))