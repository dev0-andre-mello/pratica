import numpy as np

dados = np.array([100, 150, 200])

normalizado = (dados - np.min(dados)) / (np.max(dados) - np.min(dados))
print(normalizado)
