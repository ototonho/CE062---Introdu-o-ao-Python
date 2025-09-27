# Teste


import math
print(math.floor(3.7))
print(math.ceil(3.2))
print(math.trunc(-3.9))

import statistics as st
dados = [2, 4, 4, 4, 5, 7, 9]
st.mean(dados)


import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

a * 2
b / 3

maskB = a > 2
print(maskB)
print(a[maskB])

np.mean(b)
np.var(a)

