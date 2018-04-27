import requests
import json
baseSensor = "sensor"
patronmedida = "unidades"
capturas = "mediciones"

url = 'http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/backendAmbiente/webresources/generic/getAllEstaciones'
r = requests.get(url)
url_1 = 'http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/backendAmbiente/webresources/generic/getAllSensores'
r_1 = requests.get(url_1)
# consultando mediciones
url_2 = 'http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/backendAmbiente/webresources/generic/getAllMedicionesByEstacion'
# consultando mediciones

if r.status_code==200 and r_1.status_code==200:
    estaciones = r.json()
    estaciones_s = json.dumps(estaciones)
    estaciones_d = json.loads(estaciones_s)

    sensores = r_1.json()
    sensores_s = json.dumps(sensores)
    sensores_d = json.loads(sensores_s)
    num = 0

    for i in range(len(estaciones_d)):
        num+=1
        a = estaciones_d[i]
        valorA = a['idEstacion']
        strv = str(valorA)
        #
        med = requests.post(url_2,data=strv)
        medi = med.json()
        med_s = json.dumps(medi)
        med_d = json.loads(med_s)
        mediciones = '%s' % (capturas)
        estaciones_d[i][mediciones] = med_d
        #
        k = 0
        for j in range(len(sensores_d)):
            b = sensores_d[j]
            valorB = b['idEstacion']
            if valorA == valorB:
                
                #estaciones_d[i]['sensors'].append(sensores_d[j])
                k += 1
                nSensor = '%s%d' % (baseSensor,k)
                unidades = '%s%d' % (patronmedida,k)
                
                estaciones_d[i][nSensor] = sensores_d[j]['nombre']
                estaciones_d[i][unidades] = sensores_d[j]['unidades']

# ________
# http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/backendAmbiente/webresources/generic/getAllMedicionesByEstacion
# r = requests.post(url, data = '1')
# j = r.json()
# j
# ________


##    for i in range(len(data_1)):
##        a = data_1[i]
##        elementos = a.items()
##        for clave, valor in elementos:
##            print clave,"= ", valor
else:
    print "error"
