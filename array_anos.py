import numpy as np  # Importa a biblioteca NumPy para operações avançadas com arrays

ano_inicial = 2000
ano_final = 2096

# Utiliza np.arange para gerar um array de anos a cada 4 anos, começando de ano_inicial até ano_final + 1
anos = np.arange(ano_inicial, ano_final + 1, 4)
print(anos)
