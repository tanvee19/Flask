from.Query import * #if file is in same place then we use this type to import
#pitho.models.query
import random
class Users:
	def login(self,data):
		#print(data)
		uname=data.get("username")
		password = data.get("password")
		obj = Query()
		dataobj = obj.select_row("select * from users where email=%s and password=%s",(uname,password))
		print(dataobj)
		if dataobj is not None:
			return dataobj
		else:
			return False
	def signup(self,data):
		query = Query()
		email= data.get("Email")
		dataobj = query.select_row("select id from users where Email=%s",(email))
		if dataobj is not None:
			return False
		query.insert("insert into users(Name,Email,Password) values(%s,%s,%s)",(data.get("Name"),data.get("Email"),data.get("Password")))
		return True
	def forgotpassword(self,data):
		email= data.get("Email")
		query = Query()
		dataobj = query.select_row("select id from users where Email=%s",(email))
		if dataobj is None:
			return False
		otp = random.randint(100000,999999)
		query.update("update users set activation_key=%s where Email=%s",(str(otp),email))
	def password_reset(self,data):
		email=data.get("Email")
		otp=data.get("otp")
		password=data.get("Password")
		query=Query()
		dataobj=query.select_row("select * from users where Email=%s and Activation_key=%s",(email,str(otp)))
		if dataobj is None:
			return False
		newotp=random.randint(100,999)
		query.update("update users set Password=%s,Activation_key=%s where Email=%s",(str(password),str(newotp),email))
		return True

