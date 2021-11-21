from operator import itemgetter
import numpy as np

Ysort = [0.875, 0.75, 0.625, 0.5, 0.375, 0.25, 0.125]
ord = [1, 2, 3, 4, 5, 6, 7]

memYGr = [0.875, 0.75, 0.625, 0.5, 0.375, 0.25, 0.125]
memCMD = [1, 1, 1, 1, 1, 1, 1]
endCMD = [1, 1, 0, 0, 1, 1, 0]

aux = np.array([ord, memCMD, memYGr, endCMD])
aux = np.transpose(aux)

aux = sorted(aux, key=itemgetter(2), reverse=True)
aux = sorted(aux, key=itemgetter(1))
aux = sorted(aux, key=itemgetter(3), reverse=True)

aux = sorted(aux, key=itemgetter(0))
print(np.array(aux))

aux = np.transpose(aux)
print("\n")

YGr = aux[2]
print(YGr)
