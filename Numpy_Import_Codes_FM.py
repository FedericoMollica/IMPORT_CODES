
'''
#XXXXX  NUMPY: ACCESSING, CHANGING SPECIFIC ELEMENTS, ROWS, COLUMNS...  XXXXX

# -*- coding: utf-8 -*-
@author: Federico Mòllica
'''

# -*- coding: utf-8 -*-


import numpy as np

#con il codice np.array creo un simil dataframe con elementi che posso richiamare tramite l'uso di indici
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
#result:
#[[ 1  2  3  4  5  6  7]
# [ 8  9 10 11 12 13 14]]

'''
#XXX GET A SPECIFIC ELEMENT [r, c] XXX
'''

#dopo aver creato un array posso richiarare gli elementi [r, c]
#al posto di [r] metto l'indice della lista (partendo da 0)
#al poscto di [c] metto l'indice dell'elemento nella lista (partendo da 0)
a[0]
#result:
#[1, 2, 3, 5, 6, 7]

a[1]
#result:
#[8, 9, 10, 11, 12, 13, 14]

#il quarto elemento della seconda lista
a[1, 3]
#result:
#11

'''
#XXX GET A SPECIFIC COULMN  XXX
'''

a[:, 2]
#result:
#array([ 3, 10])

'''
#XXX GET A SPECIFIC ROW XXX
'''

a[0, :]
#result:
#array([1, 2, 3, 4, 5, 6, 7])

'''
#XXX CHANGE A SPECIFIC ELEMENT OF THE ARRAY XXX
'''

#posso usare allo stesso modo il codice per riga [x, :] o colonna [:, x] per modificarle interamente 
a[1, 3] = 33
print(a)
##result:
#[[ 1  2  3  4  5  6  7]
# [ 8  9 10 33 12 13 14]] prima al posto di 33 c'era 11

'''
#XXX CREATE A SPECIFIC ARRAY AUTOMATICALLY XXX
'''

#XXX ATTENZIONE QUANDO SI COPIANO GLI ARRAY!!! XXX

a = np.full((2, 3), 77)
b = a 
#in questo caso se modifico b modificherò pure l'originale a
#per evitare questo inserisco .copy()
b = a.copy()


#il primo numero rappresenta le righe, il secondo le colonne [r, c].
#al di fuori della parentesi, l'elemento che vogliamo inserire 
b = np.full((2, 3), 77)
print(b)
#result:
#[[77 77]
# [77 77]]


#codice per creare un array con numeri decimali random(righe, colonne)
d = np.random.rand(4,2)
print(d)
#[[0.12617117 0.08523398]
# [0.24807516 0.84117855]
# [0.68943294 0.84520872]
# [0.54039844 0.93502971]]


#codice per creare un array con numeri random (in questo caso fino a 99, 2 righe, 5 colonne)
e = np.random.randint(100, size = (2, 5))
print(e)
#result:
#[[89 94 10 97 93]
# [ 0 50 75 47 34]]


#possiamo inserire anche stringhe 
c = np.full((2, 3), 'gatto')
print(c)
#result:
#[['gatto' 'gatto' 'gatto']
# ['gatto' 'gatto' 'gatto']]

'''
#XXX  BOOLEAN IN NUMPY  XXX
'''

#numpy consente di ottenere direttamente boolean facendo riferimento all'array 
e = np.random.randint(100, size = (2, 5))
print(e)
print(e == 10)
#[[89 94 10 97 93]
# [ 0 50 75 47 34]]
#([[False, False,  True, False, False],
#  [False, False, False, False, False]])
#in questo caso ho chiesto se ci fossero elementi uguali a 50 nel mio array
#solo l'elemento in posizione 2 ritorna 'True'
