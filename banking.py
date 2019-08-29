"""1. open account
	1. account number
	2. name
	3. opening balance
2. list account
3. update account
4. debit
5. credit
6. mini statement"""



class bank:
	ob=0
	num=0
	name=""
	balance=0
	amt=0
	amt1=0
	credit=0
	debit=0
	def task(self):
		q=input("do u want to continue:")
		if q is 'y':
			print("1. open account")
			print("2. list account")
			print("3. update account")
			print("4. credit")
			print("5. debit")
			print("6. mini statement")
			
			a=input("choosse the task")
			self.case(a);
		else:
			exit()
	def case(self,a):
			
			if a=='1':
				self.open_Account()
			elif a=='2':
				self.list_Account()
			elif a=='3':
				self.update_Account()
			elif a=='4':
				self.credit()
			elif a=='5':
				self.debit()
			else:
				self.mini_Statement()



	def open_Account(self):
		self.num=input("enter your account number:")
		self.name=input("enter your account name:")
		self.balance=input("enter your opening balance:")
		self.ob=self.balance
		self.task()
	def list_Account(self):
		print(self.num)
		print(self.name)
		print(self.balance)
		self.task()
	def update_Account(self):
		new=input("enter the new name")
		self.name=new
		self.task()
	def credit(self):
		acc=input("enter recipient's account number")
		self.amt=input("enter the amount you want to credit")
		if acc==self.num:
			self.balance=float(self.balance)+float(self.amt)
		self.credit=self.balance
		self.task()
	def debit(self):
		acc=input("enter recipient's account number")
		self.amt1=input("enter the amount you want to debit")
		if acc==self.num:
			self.balance=float(self.balance)-float(self.amt1)
		self.debit=self.balance
		self.task()
	def mini_Statement(self):
		acc=input("enter recipient's account number")
		if acc==self.num:
			print(self.num)
			print(self.name)
			print("opening balance is :")
			print(self.ob)
			print("cedit amount:")
			print(self.amt)
			print("balance:")
			print(self.credit)
			print("debit amount:")
			print(self.amt1)
			print("balance:")
			print(self.debit)
			self.task()

obj=bank()
obj.task()


