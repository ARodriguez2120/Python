# clasesObjetos.py

class MixinsData(object):
	def __init__(
		self,
		user="anonimo",
		password="patito",
		port="1234", 
		host="localhost", 
		db="sqlite3"):
		

		self.user = user
		self.password = password
		self.port = port
		self.host = host
		self.db = db


	def get_username(self):
		return self.user
	def get_password(self):
		return self.password
	def get_port(self):
		return self.port
	def get_host(self):
		return self.host
	def get_db(self):
		return self.db



usuario = str(input("Nombre de Usuario?:__ "))
password = str(input("Password?:__"))

# Instancia en JAVA, C#, C++
# MixinsDAta obj = new MixinsData();

# Instancia en Python

obj = MixinsData(password=password ,user = usuario)

print(obj.user)
print(obj.password)
print(obj.get_username())
print(obj.get_password())
print(obj.get_port())
print(obj.get_host())
print(obj.get_db())



user = obj.get_username()
print(user *10)





