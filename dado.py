import random

def tirar_dado():
	opciones = [i for i in range(1, 7)]
	tiro = random.choice(opciones)
	return tiro


def tirar_dados(numero_tiros, numero_dados):
	secuencia_tiros = []	
	for _ in range(numero_tiros):
		total_tiro = 0
		for _ in range(0, numero_dados):
			tiro = tirar_dado()
			total_tiro += tiro
		secuencia_tiros.append(total_tiro)
	return secuencia_tiros

def simular(numero_tiros, numero_intentos, numero_dados):
	tiros = []
	for _ in range(numero_intentos):
		secuencia_tiros = tirar_dados(numero_tiros, numero_dados)
		tiros.append(secuencia_tiros)
	return tiros

def buscar_numero_en_tiros (tiros, numero):
	tiros_numero = 0
	for tiro in tiros:
		if numero in tiro:
			tiros_numero += 1

	return tiros_numero

if __name__ == '__main__':
	numero_dados = int(input('Cuantos dados quieres usar? '))
	numero_tiros = int(input('Cuantos tiros del (de los) dado(s)? '))
	numero_intentos = int(input('Cuantas veces correrá la simulación? '))
	numero_a_buscar = int(input('Cual número quieres buscar? '))

	tiros = simular(numero_tiros, numero_intentos, numero_dados)
	tiros_con_numero = buscar_numero_en_tiros(tiros, numero_a_buscar)
	probabilidad_numero = tiros_con_numero / numero_intentos

	print(f'El {numero_a_buscar} salió {tiros_con_numero} veces, su probabilidad fue de: {probabilidad_numero}')
