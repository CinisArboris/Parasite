from PIL import Image


class Parasite:
	gFil = -1
	gCol = -1
	gInp = -1
	gNam = ''

	def __init__(self, fil, col, inp, nam):
		if fil*col < len(inp):
			print('Error: la imagen no es suficientemente grande.')
			print('Longitud del mensaje: ', len(inp))
			print('Dimensiones de la imagen: ', fil, 'x', col, '=', fil*col)
			exit(1)
		self.gFil = fil
		self.gCol = col
		self.gInp = inp
		self.gNam = nam

	@staticmethod
	def banner():
		for a in range(10):
			print(' '*a+"You didn't say the magic word !!!")

	def crearImagen(self):
		dimensiones = (self.gFil, self.gCol)
		imagenObj = Image.new('RGB', dimensiones, 'red')
		self.guardarCerrar(imagenObj)

	def guardarCerrar(self, imagenObj):
		imagenObj.save(self.gNam)

	def strTObin(self) -> list:
		vectorDecimal = []
		for x in self.gInp:
			vectorDecimal.append(bin(ord(x)))
		print('vectorDecimal: ', vectorDecimal)
		return vectorDecimal

	def insertarDatos(self, vectorDecimal):
		imagenObj = Image.open(self.gNam)
		imagenPx = imagenObj.load()
		iteraciones = len(vectorDecimal)
		count = 0
		if count < iteraciones:
			for fila in range(self.gFil):
				for columna in range(self.gCol):
					if count == iteraciones:
						self.guardarCerrar(imagenObj)
						print('Imagen guardada con exito.')
						exit(0)
					imagenPx[fila, columna] = (int(vectorDecimal[count], 2), int(vectorDecimal[count], 2), int(vectorDecimal[count], 2))
					count = count + 1
		self.guardarCerrar(imagenObj)


parasite = Parasite(10, 10, '[fortis fortuna adiuvat]', 'nox.png')
parasite.banner()
parasite.crearImagen()
parasite.insertarDatos(parasite.strTObin())












