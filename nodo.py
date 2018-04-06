class nodo(object):
	def __init__(self,data=None,parent=None):
		#print 'node init %s' % data
		self.data = data
		self.children = []
		self.parent = parent
		if self.parent is not None: self.level = parent.level+1
		else: self.level = 0
		if parent is not None: parent.addChildren(self)

	def getChildren(self): return self.children
	def setChildren(self,ch): self.children = ch
	def addChildren(self,ch): self.children.append(ch)
	"""
	start your algorithm by pushing the root of the tree and repeat the following till the queue becomes empty:
	1. Pop the front of the queue "at first its the root"
	2. Process it and push all of its children to the queue
	3. Go to 1
	"""
	def bfs(self):
		q = [self]
		while len(q) !=0:
			act = q.pop(0)
			print '\t'*act.level,act.data
			for c in act.children: q.append(c)
	"""
		DFS-recursive(G, s):
	        	mark s as visited
	        	for all neighbours w of s in Graph G:
		            if w is not visited: DFS-recursive(G, w)
	"""
	def dfs(self,visited=[]):
		print '\t'*self.level,'%s' % self.data
		visited.append(self)
		for ch in self.children:
			if ch not in visited:
				ch.dfs(visited)
