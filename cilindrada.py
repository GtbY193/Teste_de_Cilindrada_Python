import math

diametro = 80
curso = 75
cilindros = 4

cilindrada = (math.pi * diametro**2 * curso * cilindros) // 4000

litros = cilindrada // 1000

print(f"Cilindrada total: {cilindrada:.2f} cm³")
print(f"Cilindrada em litros: {litros:.3f} L")