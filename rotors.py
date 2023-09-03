import random
import pickle

alphabet = 'abcdefghijklmnopqrstuvwxyz '

r1 = (list(alphabet))
r2 = (list(alphabet))
r3 = (list(alphabet))

random.shuffle(r1)
r1 = ''.join(r1)

random.shuffle(r2)
r2 = ''.join(r2)

random.shuffle(r3)
r3 = ''.join(r3)

f = open('./rotors_state.enigma', 'wb')
pickle.dump((r1, r2, r3), f)
f.close()