import re
class Calculate1:
	def __init__(self):
		self.count = 0
		self.count1 = 0
		self.ktest = " "
		self.val = " "
		self.ktest1 = " "
		self.val2 = " " 
		self.dict1 = {}
		self.dict2 = {}
		self.li1 = []
		self.li2 = []
		self.s1=open("SAME",'w+')
		self.d1=open("DIFF",'w+')
		self.a1=open("ANY",'w+')
		self.no1=open("NOT1",'w+')
		self.no2=open("NOT2",'w+')
	def filematching(self):
		print"----------------------Count of tempest lines 1st file---------->"
		with open('source.txt','rb') as self.f:
			try:
				for lines in self.f:
					re1 = re.match('tempest.(.*)',lines,re.M)
					if re1:
						re1 = str(re1.group().strip('\r'))
						re2 = re1.split(' ... ')
						self.ktest = re2[0]
						self.val = re2[1]	
						self.dict1[self.ktest] = self.val
						dat = str(self.ktest)+' ... '+str(self.val)
						self.li1.append(dat)
						self.count += 1	
	
			except:
				print self.count
		print"<---------------------Count of tempest lines in 2nd file------->"
		with open('destination.txt','rb') as self.f1:
			for lines in self.f1:
				res1 = re.match('tempest.(.*)',lines,re.I)
				if res1:
					res1 = str(res1.group().strip('\r'))
					res2 = res1.split(' ... ')
					self.ktest1 = res2[0]
					self.val1 = res2[1]
					self.dict2[self.ktest1] = self.val2
					dat1 = str(self.ktest1)+' ... '+str(self.val1)
					self.li2.append(dat1)
					self.count1 += 1
			print self.count1
			print"<---------------------Count of same---------------------------->"
			count2 = 0
			for i in self.li1:
				for j in self.li2:
					if i==j:
						count2 += 1
						self.s1.writelines(i+'\n')
			self.s1.close()
			print count2
		
			print"<---------------------Count of anything------------------------>"
			count3 = 0
			for i1 in self.dict1:
				for j1 in self.dict2:
					if i1==j1:
						if(self.dict1[i1]!=self.dict2[j1]):
							count3 += 1
							self.d1.writelines(i1+'\n')
			self.d1.close()
			print count3


			print"<---------------------Count of different----------------------->"
			count4 = 0
			for i in self.dict1:
				for j in self.dict2:
					if(i==j):
						if(((self.dict1[i]!='ok')&(self.dict2[i]!='FAIL'))&((self.dict1[j]!='ok')&(self.dict2[j]!='FAIL'))):
							count4 += 1
							self.a1.writelines(i+'\n')
			self.a1.close()
			print count4
		

			print"<---------------------Not in second---------------------------->"
			count5 = 0
			for i in self.dict1:
				if i in self.dict2:
					continue
				else:
					count5 += 1
					self.no1.writelines(i+'\n')
			self.no1.close()
			print count5
		


			print"<---------------------Not in first----------------------------->"
			count6 = 0
			for i in self.dict2:
				if i in self.dict1:
					continue
				else:
					count6 += 1
					self.no2.writelines(i+'\n')
			self.no2.close()
			print count6



obj=Calculate1()
obj.filematching()
			
	        
          	
	
