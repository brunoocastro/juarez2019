import numpy as np

pos = [(22, 5), (279, 4), (233, 4), (179, 4), (142, 4), (124, 4), (83, 4)]

test = np.amax(pos, axis=0)

test1 = np.amax(pos, axis=0)[0]

print('\nLINHA = {}\n'.format(test))

print('\nVALOR FODA = {}\n'.format(test[0]))

print('\nLINHA NOVA= {}\n'.format(test1))