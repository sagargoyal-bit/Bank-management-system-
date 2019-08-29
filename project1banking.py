import json
class AccountManagement:
	account_dict={}
	statement_list=[]
	def __init__(self):
		ch='y'
		while(1):
			if ch=='y' or ch=='Y':
				print("\n----------------------------------------------WELCOME TO BANKING SOFTWARE----------------------------------------------")
				print("\n\n\t\t\t\t\t\t1.Add new Account \n\t\t\t\t\t\t2.Update Account \n\t\t\t\t\t\t3.Delete Account \n\t\t\t\t\t\t4.Credit Amount \n\t\t\t\t\t\t5.Debit Amount \n\t\t\t\t\t\t6.Mini statement of Account \n\t\t\t\t\t\t7.Display Account \n\t\t\t\t\t\t8.Exit")
				self.enter_choice()
				ch=input("\n\n\t\t\t\tDo you want to continue(Y-YES,N-NO)")
			else:
				exit()
		
	def enter_choice(self):
		a=input("\n\n\t\t\t\tEnter your choice:")
		if a=="1":
			self.open_account()
		elif a=="7":
			self.display_list()
		elif a=="2":
			self.update_account()
		elif a=="3":
			self.delete_account()
		elif a=="4":
			self.credit_amount()
		elif a=="5":
			self.debit_amount()
		elif a=="6":
			self.mini_statement()
		elif a=='8':
			exit()
		else:
			print("\t\t\t\tYou have entered wrong choice")
			self.enter_choice()
			
	def open_account(self):
		fread=open('account.txt','r')
		read_json=fread.read()
		self.account_dict=json.loads(read_json)
		fread.close()
		acc_no=self.account_number()
		if acc_no in self.account_dict.keys():
			print("\t\t\t\tAccount already exists")
			return self.open_account()
		acc_name=self.holder_name()
		open_type=self.account_type()
		open_amt=self.open_amount()
		fwrite=open('account.txt','w')
		self.account_dict[acc_no]={"acc_no":acc_no,"name":acc_name,"acc_type":open_type,"amount":open_amt}
		print("\t\t\t\tsuccessfully open new account")
		acc_json=json.dumps(self.account_dict)
		fwrite.write(acc_json)
		fwrite.close()
	def account_number(self):
		acc_no=input("\t\t\t\tEnter account no:")
		if acc_no=="exit":
			self.__init__()
		elif acc_no>='a' and acc_no<='z':
			print("\t\t\t\taccount number should be in numbers")
			return self.account_number()
		elif acc_no=="":
			print("\t\t\t\tthe account number can not be null")
			return self.account_number()
		return acc_no
		
	def holder_name(self):
		name=input("\t\t\t\tEnter the name:")
		if name>="0" and name<="9":
			print("\t\t\t\tname should be in alphabets")
			return self.holder_name()
		elif name=="":
			return self.holder_name()
		return name
		
	def account_type(self):
		a_type=("savings","current","s","c")
		open_type=input("\t\t\t\tEnter open account type:")
		if open_type not in a_type:
			print("\t\t\t\tyou have entered wrong account type")
			return self.account_type()
		elif a_type=="":
			return self.account_type()
		return open_type
	
	def check_amount(self):
		amt=input("\t\t\t\tEnter the amount:")
		if amt>='a' and amt<='z':
			print("\t\t\t\tamount should be in numbers")
			return self.check_amount()
		elif amt=="":
			print("\t\t\t\tamount can not be null")
			return self.check_amount()	
		elif int(amt)<=0:
			print("\t\t\t\tamount can not be negative")
			return self.check_amount()
		return amt
	
	def open_amount(self):
		open_amt=input("\t\t\t\tEnter the opening amount:")
		if(open_amt >= 'a'  and open_amt <= 'z'):
			print("\t\t\t\tamount should be in numbers")
			return self.open_amount()
		elif open_amt=="":
			print("\t\t\t\tamount can not be null")
			return self.open_amount()	
		elif int(open_amt)<100:
			print("\t\t\t\tamount should be more than 100")
			return self.open_amount()
		return open_amt
		
	def display_list(self):
		fread=open('account.txt','r')
		read_json=fread.read()
		self.account_dict=json.loads(read_json)
		print("\n\t\t\t\tAccount_no\tName\t\tAccount type\t\tBalance\t")
		for data in self.account_dict.keys():
			print("\t\t\t\t",end="")
			print(str(self.account_dict[data]['acc_no'])+"\t\t"+
				  str(self.account_dict[data]['name'])+"\t\t"+
				  str(self.account_dict[data]['acc_type'])+"\t\t\t"+
				  str(self.account_dict[data]['amount'])
				 )	
		fread.close()
	
	def update_account(self):
		fread=open('account.txt','r')
		read_json=fread.read()
		self.account_dict=json.loads(read_json)
		acc_no=self.account_number()
		if acc_no not in self.account_dict.keys():
			print("\t\t\t\tAccount does not exists")
			acc_no=self.account_number()
		get_acc=self.account_dict[acc_no]
		fread.close()
		fwrite=open('account.txt','w')
		print("\t\t\t\t1.Update name \t\t\t\t2.Update account type \t\t\t\t3.Both")
		choice=input("\n\t\t\t\tEnter your choice:")
		if choice=='1':
			name=self.holder_name()
			get_acc['name']=name
			print("\t\t\t\tAccount name updated successfully")
		elif choice=='2':
			acc_type=self.account_type()
			get_acc['acc_type']=acc_type
			print("\t\t\t\tAccount type updated successfully")
		elif choice=='3':
			name=self.holder_name()
			acc_type=self.account_type()
			get_acc['name']=name
			get_acc['acc_type']=acc_type
			print("\t\t\t\tAccount name and type updated successfully")
		else:
			print("\t\t\t\tYou have entered wrong choice")
			self.update_account()
		acc_json=json.dumps(self.account_dict)
		fwrite.write(acc_json)		
		fwrite.close()
	def delete_account(self):
		fread=open('account.txt','r')
		read_json=fread.read()
		self.account_dict=json.loads(read_json)
		acc_no=self.account_number()
		if acc_no not in self.account_dict.keys():
			print("\t\t\t\tAccount does not exists")
			acc_no=self.account_number()
		del self.account_dict[acc_no]
		print("\t\t\t\tSuccessfully deleted account")
		fread.close()
		fwrite=open('account.txt','w')
		acc_json=json.dumps(self.account_dict)
		fwrite.write(acc_json)
		fwrite.close()
		
	def credit_amount(self):
		fread=open('account.txt','r')
		read_json=fread.read()
		self.account_dict=json.loads(read_json)
		acc_no=self.account_number()
		if acc_no not in self.account_dict.keys():
			print("\t\t\t\tAccount does not exists")
			acc_no=self.account_number()
		get_Acc=self.account_dict[acc_no]
		fread.close()
		fwrite=open('account.txt','w')
		balance=int(get_Acc['amount'])
		amt2=self.check_amount()
		get_Acc['amount']=int(balance)+int(amt2)
		self.statement_list.append("Credited : " + str(amt2))
		self.account_dict[acc_no]['statement_history']=self.statement_list
		#print(self.account_dict['statement_history'])
		acc_json=json.dumps(self.account_dict)
		fwrite.write(acc_json)
		fwrite.close()
		
	def debit_amount(self):
		fread=open('account.txt','r')
		read_json=fread.read()
		self.account_dict=json.loads(read_json)
		acc_no=self.account_number()
		if acc_no not in self.account_dict.keys():
			print("\t\t\t\tAccount does not exists")
			acc_no=self.account_number()
		get_Acc=self.account_dict[acc_no]
		fread.close()
		fwrite=open('account.txt','w')
		balance=int(get_Acc['amount'])
		amt2=self.check_amount()
		if balance<=0  or balance< int(amt2):
			print("\n\t\t\t\tyou can't withdraw as you are not having enough money in account")
			return self.__init__()
		get_Acc['amount']=int(balance)-int(amt2)
		self.statement_list.append("Debited : -" + str(amt2))
		self.account_dict[acc_no]['statement_history']=self.statement_list
		#print(self.account_dict['statement_history'])
		acc_json=json.dumps(self.account_dict)
		fwrite.write(acc_json)
		fwrite.close()
		
	def mini_statement(self):
		fread=open('account.txt','r')
		read_json=fread.read()
		self.account_dict=json.loads(read_json)
		acc_no=self.account_number()
		if acc_no not in self.account_dict.keys():
			print("\t\t\t\tAccount does not exists")
			acc_no=self.account_number()
		print("\n\t\t\t\tAcc_no.\tName \t")
		acc_detail=self.account_dict[acc_no]
		print("\t\t\t\t",end="")
		print(acc_detail['acc_no'] + "\t" + str(acc_detail['name']))
		print("\n\t\t\t\tTotal : " + str(acc_detail['amount']))
		print("\n\t\t\t\tTransaction History : ")
		if 'statement_history' in acc_detail.keys():
			for data in acc_detail['statement_history']:
				print("\t\t\t\t",data)
		fread.close()	
			
obj=AccountManagement()