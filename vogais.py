b = input("digite")
letra = b.lower()

def vogal(a):
    vogais = ["a", "e", "i", "o", "u"]
    if any(element in a for element in vogais):
        return
    else:
        return ("False")
    
vogal(letra)