from datetime import datetime, date, time
from operator import attrgetter
for clave,valor in estaciones_d[0]['mediciones'].items():
	print clave
	diccionarioCapturas = dict()
	# creo diccionario
	l = list()
	for i in valor:
                diccionarioInterno = dict()
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
		diccionarioInterno['fecha'] = f_captura
		diccionarioInterno['medida'] = d_capturado
		diccionarioInterno['unidadesM'] = lista[3]
		l.append(diccionarioInterno)
        L_orden = sorted(l, reverse=True)
	diccionarioCapturas[clave] = L_orden
	print diccionarioCapturas
	#
