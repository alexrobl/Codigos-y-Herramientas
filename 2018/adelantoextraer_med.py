from datetime import datetime, date, time
from operator import attrgetter
for clave,valor in estaciones_d[0]['mediciones'].items():
	print clave
	l = list()
	for i in valor:
		lista = i.split(";")
		fecha = lista[0].split("/")
		anio = int(fecha[0])
		mes = int(fecha[1])
		dia = int(fecha[2])
		fecha_py = date(anio,mes,dia)
		tiempo = lista[1].split(":")
		h = int(tiempo[0]) 
		m = int(tiempo[1])
		s = int(tiempo[2])
		tiempo_py = time(h,m,s)
		f_captura = datetime.combine(fecha_py,tiempo_py)
		d_capturado = float(lista[2])
		print f_captura," ", d_capturado
		l.append(f_captura)
	print sorted(l, reverse=True)
        


	# print sorted(l, key=attrgetter('second'), reverse=True)
