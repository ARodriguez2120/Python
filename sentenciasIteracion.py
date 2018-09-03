#sentenciasIteracion.py

#While
# i=1


# while i<10:
# 	print(i)
# 	i += 1



# #For

# k=1

# for k in range (10):
# 	print(k)



# for j,k in enumerate( range(10)):
# 	print(j)
# 	print("k", k)


# for item in "[1,2,3,4,5,6,7]":
# 	print(item*2)

# for line in open("archivoTexto.txt"):
#	print(line)


# for l, line in enumerate(open("archivoTexto.txt")):
# 	print(l, ":", line)


# for l, line in enumerate(open("archivoTexto.txt")):
# 	for p in line.split():
# 		print(p)


# for l, line in enumerate(open("archivoTexto.txt")):
# 	for p in line.split():
# 		for f in p:
# 			print(f)


# for l, line in enumerate(open("archivoTexto.txt")):
# 	for p in line.split():
# 		for f in p:
# 			print(f)


# lista = []
# for i in range (10):
# 	lista.append(i)
# print(lista)

# lista = [i for i in range(10) if i %  2 == 0]
# print(lista)



#----------------- While-----------------
import random

r=1
c = 0
while c<50 or  r== 99 :
	r = random.randint(1,10000)
	c+=1
	print(r)



