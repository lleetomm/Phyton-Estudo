import numpy as np

a = np.random.randn(25)  # Cria um array com 25 valores aleatórios
len(a)  # Informa o tamanho do array

print(a)  # Mostra os valores do array
a = np.array([-0.97662319, -0.91427827, -0.17596519, -1.07721448, -0.64067605,
              -1.21453417, -0.508037, 1.0928856, -0.4206412, -0.40750775,
              -0.83259417, 0.41311712, -0.03811292, -0.41181049, 0.45493473,
              0.5168261, 0.38207838, 1.27969391, -0.91343678, -0.89708382,
              -0.94028084, 0.33992957, -1.73894293, 0.5228072, 0.57514934])

print("============")
print(a[0:10])  # Mostra os valores do array, de 0 até 10
a = np.array([-0.97662319, -0.91427827, -0.17596519, -1.07721448, -0.64067605,
              -1.21453417, -0.508037, 1.0928856, -0.4206412, -0.40750775])

print("============")
a = print(a[0:4] * 2)  # Multiplicação dos valores 0 até 4 por 2
np.array([-1.95324639, -1.82855654, -0.35193039, -2.15442897])
