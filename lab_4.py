#treść zadania:
			# Opracuj klasę (z określeniem ale bez implementacji metod) opisującą dowolne urządzenie
			# techniczne. Przedstaw szkielet w j. Python.
class Kalkulator:
	def __init__(self):
		self.wlacz()

	def __del__(self):
		self.wylacz()

	def wlacz(self):
		print('wlaczono')
	
	def wylacz(self):
		print('wylaczono')

	@staticmethod
	def dodaj(a,b):
		return a+b

	@staticmethod
	def odejmij(a,b):
		return a-b

	@staticmethod
	def podziel(a,b):
		return a/b
	
	@staticmethod
	def poteguj(a,b):
		return a**b


class Komputer(Kalkulator):
	
	def __init__(self):
		self.wlacz()
	
	def __del__(self):
		self.wylacz()

	def wlaczEkran(self):
		print('Wlaczono ekran')
	
	def wylaczEkran(self):
		print('Wylaczono ekran')

	def wlaczPrzegladarke(self):
		print('Wlaczono przegladarke')
	
	def wylaczPrzegladarke(self):
		print('Wylaczono przegladarke')









