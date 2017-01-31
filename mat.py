class Matrix:
	def __init__(self):
		self.a = []
		self.b = []
		self.res = [] 
	def matrix1(self):
		print"***********1ST SET MATRIX*******"
		for i in range(3):
			row = []
			for j in range(3):
				k = input()
				row.append(k)
			self.a.append(row)
			print (self.a)
		print"***********2ND SET MATRIX*******"
		for i in range(3):
			row = []
			for j in range(3):
				k = input()
				row.append(k)
			self.b.append(row)
			print self.b
		print"*************Addition***********"
		res = []
		for i in range(len(self.a)):
			for j in range(len(self.a[0])):
				self.res.append(self.a[i][j] + self.b[i][j])
		for r in self.res:
			print r 
		print"*************SUBTRATION*********"	
		res2 = []
		for i in range(len(self.a)):
			for j in range(len(self.a[0])):
				res2.append(self.a[i][j] - self.b[i][j])
		for r1 in res2:
			print r1
		
		print"************MULTIPLICATION******"	
		res3 = []
		for i in range(len(self.a)):
			for j in range(len(self.a[0])):
				res3.append(self.a[i][j] * self.b[i][j])
		for r1 in res3:
			print r1

obj = Matrix()
obj.matrix1()
