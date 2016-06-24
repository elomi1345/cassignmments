import numpy as np
nodes=np.genfromtxt('coordinate.txt', delimiter=' ', names=True)
xcord=nodes['x']
ycord=nodes['y']
zcord=nodes['z']
elements=np.genfromtxt('elements.txt', delimiter=' ', names=True)
numelem=len(elements['node1'])
numnodes=len(xcord)
for i in range(1,numelem)
    element()
print(numnodes)
print(numelem)
