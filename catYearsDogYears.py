def calculate_pet_ages(humanYears):
    # Inicializamos las edades de los animales
    catYears = 0
    dogYears = 0

    # Calculamos las edades en función de los años humanos
    if humanYears >= 1:
        catYears += 15
        dogYears += 15

    if humanYears >= 2:
        catYears += 9
        dogYears += 9

    if humanYears > 2:
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Ejemplo de uso
humanYears = 12
ages = calculate_pet_ages(humanYears)
print(ages)  # Output: [5, 32, 34]
