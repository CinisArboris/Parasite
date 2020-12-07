#import
from PIL import Image
import numpy

class Parasite :	
	#variables
	fila		= -1#default
	columna		= -1#default
	imagenPNG	= -1#default
	imagenPX	= -1#default
	cadenaSTR	= -1#default
	vectorDEC	= []
	
	
	def __init__ (self, fila, columna, cadenaSTR, vectorDEC):
		self.fila		= fila
		self.columna	= columna
		self.cadenaSTR	= cadenaSTR
		self.vectorDEC	= vectorDEC
	# ------------------------------------------------
	def guardarCerrar(self):
		self.imagenPNG.save('nox.png')
	# ------------------------------------------------
	def banner(self):
		for a in range(10):
			print (' '*a+"You did't say the magic word !!!")
	# ------------------------------------------------
	def crearImagen(self):
		dimensiones=(self.fila, self.columna)
		self.imagenPNG = Image.new(
							'RGB',
							dimensiones,
							'white'
						)
		self.imagenPX = self.imagenPNG.load()
		self.guardarCerrar()

	def strTObin (self):
		for x in self.cadenaSTR:
			self.vectorDEC.append(bin(ord(x)))#[2:])
	# ------------------------------------------------
	def insertarDatos(self):
		sum = 0
		self.imagenPNG = Image.open('nox.png')
		self.imagenPX = self.imagenPNG.load()
		tope = len(self.vectorDEC)
		inicio = 0
		while (inicio < tope):
			fila = 0
			columna = 0
			while (fila < self.fila):
				columna = 0
				while (columna < self.columna):
					if inicio == tope:
						self.guardarCerrar()
						return 'fin'
					x = self.vectorDEC[inicio]
					inicio = inicio + 1
					x = int(x,2)
					r,g,b = (self.imagenPX[fila,columna])
					self.imagenPX[fila,columna] = (x,x,x)
					columna = columna + 1
					sum = sum + 1
				fila = fila + 1
			inicio = inicio + 1
		self.guardarCerrar()
# ================================================
# =============     M A I N     ==================
parasite = Parasite(10, 10, "Buenas noches mi amor :)", [])
parasite.banner()
parasite.crearImagen()
parasite.strTObin()
parasite.insertarDatos()












