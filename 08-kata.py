
def calculateIMC(weight, height):
    return round(float(weight) / float(height) ** 2, 2)


w = input('weight (kg): ')
h = input('height (m): ')

print(str(calculateIMC(w, h)))

# Peso inferior al normal	Menos de 18.5
# Normal	18.5 – 24.9
# Peso superior al normal	25.0 – 29.9
# Obesidad	Más de 30.0

