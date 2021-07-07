import numpy as np

m = np.arange(0, 100).reshape(10, 10)
v = np.full((1, 10), 20)

print('\nm:\n', m)
print('\nv:\n', v)

vr = v - m[1]

print('\nvr:\n', vr)

x = m @ vr.T

print('\nm @ vr\n', x)

x = np.round(x / 100)
print('\nround(x / 100):\n', x)

print('\nmax(x):\n', x.max())
