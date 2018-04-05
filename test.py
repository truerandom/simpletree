"""
			1
		2			3
	4		5	6		7
8
12485367
"""
from nodo import *
"""
n1 = nodo(1)
n2 = nodo(2,n1)
n3 = nodo(3,n1)
n4 = nodo(4,n2)
n5 = nodo(5,n2)
n6 = nodo(6,n3)
n7 = nodo(7,n3)
n8 = nodo(8,n4)
"""
n1 = nodo(1)
n2 = nodo(2,n1)
n3 = nodo(3,n1)
n4 = nodo(4,n2)
n5 = nodo(5,n2)

print "*"*23,"BFS","*"*23
n1.bfs()
print "*"*51

print "*"*23,"DFS","*"*23
n1.dfs()
print "*"*51
