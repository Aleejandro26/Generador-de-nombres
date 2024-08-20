import random

prefijos = ["Al", "Be", "Ce", "De", "El", "Fe", "Ge", "He", "Il", "Jo"]
sufijos = ["son", "ler", "ton", "den", "man", "ker", "ron", "ber", "ver", "nor"]

def generar_nombre_aleatorio():
    prefijo = random.choice(prefijos)
    sufijo = random.choice(sufijos)
    
    nombre = prefijo + sufijo
    return nombre

def main():
    print("Generador de Nombres Aleatorios")
    while True:
        nombre = generar_nombre_aleatorio()
        
        print(f"Nombre generado: {nombre}")
        
        continuar = input("¿Quieres generar otro nombre? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
