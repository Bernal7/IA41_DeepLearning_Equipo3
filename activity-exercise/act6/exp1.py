import numpy as np

z = np.array([-2., -1., 0., 1., 2.])
mask = z > 0
out = z.copy()

np.tanh(z, out=out, where=mask)
print("mask: ", mask)
print("reultados con where: ", out)