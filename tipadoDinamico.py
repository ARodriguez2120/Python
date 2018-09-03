#tipadoDinamico.py

# Integers

# a=34
# b=23
# c=31


# print (a+b+c)
# print ("Output Vars a, b, c", a, b, c)
# print ("Output Vars a: {0}, b:{1}, c{2}".format(a, b, c))
# print ("")

# #Float
# a=20.90
# b=23.12
# c=22.43

# print(a + b + c)

# #Boolean

# d=True
# e=False

#String

s = "Este es un String de comillas dobles"
ss = 'Este es un String de comillas simples'

#print(s+ss)
#print(s*3)
#print(s[1])
#print(s[1:3])
#print(11)
#print(-11)
#print(s[:-11])
#print(s[-11:])


#print(s.split())
# ssss= s.split()

# #print(len(ssss))

# #List

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(lista)

# #for i in lista:
# 	#print(i)
# 	print(sum (lista))

# 	#lista.append(0)
# 	#print(lista)

# 	lista.insert(0, 0)

# 	lista.pop()
# 	print(lista)




#Tuplas

# t= (1, 2, "abc", True, [4, 5])

# print(t)

# print(t[2])  #Accesar por elementos

# for item in t:
# 	print(item)

#Diccionarios

d = {1:2, "abc": 34, 2:"item", "d":"ch", "li":[1, 2, 3], "dic": {11:23}}

print(d)
print(d["abc"]) 		#Acceder por item segun ID: 
print(d["li"][1])       #Acceder a un item de una lista dentro del diccionario: 
print(d["dic"][11])    #Acceder a al diccionario, al item por ID: 
print(d.keys())        #Claves de diccionario
print(d.values())		#Valores de las claves
print(d.items())		#Claves con valor





#SETS/CONJUNTOS


s={1, 2, 3, 4}

print(s)
print(type(s))

for item in s:
	print(item)

s.add(5)
print(s)