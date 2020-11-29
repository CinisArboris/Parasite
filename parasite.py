#import
from PIL import Image
import numpy

class Parasite :	
	#variables
	fila		= 0
	columna		= 0
	imagenFoto	= 0
	imagenDato	= 0
	textoASCII	= "default"
	vectorDEC	= []
	
	
	def __init__ (self, fila, columna, textoASCII, vectorDEC):
		self.fila		= fila
		self.columna	= columna
		self.textoASCII	= textoASCII
		self.vectorDEC	= vectorDEC
		print ("==============================")
		
	#funciones
	def guardarCerrar(self):
		self.imagenFoto.save('nox.png')
		print ("==============================")

	def imprimirPixel(self):
		self.vector = numpy.asarray(self.imagenFoto)
		#print(self.vector[0])	#Imprimir fila [0,1,...31]
		#print ("- - - - - - -")
		#print ("1er linea")
		#inicio = 0
		#while inicio < len(textoASCII):
		#	print (">>>>>>>>>>")
		#	#print(textoASCII[inicio], list(map(bin,bytearray(textoASCII[inicio], encoding='utf-8'))))
		#	temporal = list(map(bin,bytearray(textoASCII[inicio], encoding='utf-8')))
		#	temporal = temporal[0]
		#	temporal = temporal[2:]
		#	pixel = self.vector[0][0]
		#	print (pixel)
		#	print (temporal)
		#	inicio=inicio+1
		resultado = self.asciiTObin()
		print (resultado)

	def banner(self):
		print ("You did't say the magic word !!!")
		print ("You did't say the magic word !!!")
		print ("You did't say the magic word !!!")
		print ("You did't say the magic word !!!")
		print ("You did't say the magic word !!!")
		print ("You did't say the magic word !!!")
		print ("You did't say the magic word !!!")
		print ("You did't say the magic word !!!")
		print ("==============================")

	def crearImagen(self):
		dimensiones=(self.fila, self.columna)
		self.imagenFoto = Image.new('RGB', dimensiones, 'white')
		self.imagenDato = self.imagenFoto.load()
		self.guardarCerrar()
		print ("Imagen base creada :)")
		print ("==============================")

	def asciiTObin (self):
		for x in self.textoASCII:
			#print (x)
			#print (bytearray(x, encoding='utf-8'))
			#print (ord(x))
			#print (hex(ord(x)))
			#print (bin(ord(x)))
			self.vectorDEC.append(bin(ord(x)))#[2:])
		print (self.vectorDEC)
		print ("Texto convertido a binarios. :)")
		print ("==============================")

	def insertarDatos(self):
		self.imagenFoto = Image.open('nox.png')
		self.imagenDato = self.imagenFoto.load()
		#saco de 3 en 3 o de 1 en 1
		tope = len(self.vectorDEC)
		inicio = 0
		while (inicio < tope):
			fila = 0
			columna = 0
			#print (self.fila, self.columna)
			while (fila < self.fila):
				columna = 0
				while (columna < self.columna):
					
					if inicio == tope:
						self.guardarCerrar()
						return 'fin'
					#print (int(x,2))
					x = self.vectorDEC[inicio]
					inicio = inicio + 1
					x = int(x,2)
					r,g,b = (self.imagenDato[fila,columna])
					self.imagenDato[fila,columna] = (x,x,x)
					#print (self.imagenDato[fila,columna])
					#print (r,g,b)
					columna = columna + 1
					print ('')
				fila = fila + 1
			inicio = inicio + 1
		self.guardarCerrar()

# main
parasite = Parasite(10, 10, "Buenas noches mi amor :)", [])
parasite.banner()
parasite.crearImagen()
parasite.asciiTObin()
parasite.insertarDatos()












