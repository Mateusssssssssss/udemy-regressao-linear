import numpy as np

# Dados
x = np.array([15, 18, 20, 25, 30, 44])
y = np.array([240, 255, 270, 283, 300, 310])

# Calcular a média de x e y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Calcular a correlação de Pearson manualmente
numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
correlation = numerator / denominator

print(f'Correlação de Pearson: {correlation}')

