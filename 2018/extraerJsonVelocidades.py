import requests
import json
import arcpy

url = "http://www.simur.gov.co/SimurMapaMovilidadWA/SketchesService"
response = requests.get(url)
velo = response.json()
velo_s = json.dumps(velo)
velocidades = json.loads(velo_s)
#
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\Users\alex\Documents\ALEX\Semestre 1 - Maestria\analisis espacial\ScriptTallerF"
salida = r"C:\Users\alex\Documents\ALEX\Semestre 1 - Maestria\analisis espacial\ScriptTallerF"
nombre_salida = "velocidades.shp"
geometria = "POLYLINE"
template = r"C:\Users\alex\Downloads\PROYECTO SCJ MAURICIO\Mallav.shp"
refS = arcpy.Describe(template).spatialReference
arcpy.CreateFeatureclass_management(salida,nombre_salida,geometria,spatial_reference=refS)
#

for clave, valor in velocidades[0].items():
    if len(clave)>10:
        clave = clave[0:9]
        
    else:
        pass
    arcpy.AddField_management(nombre_salida,clave,"TEXT", field_length=100)

##for i in range(1):
##    coords = list()
##    for clave, valor in velocidades[i].items():
##        if clave == 'points':
##            lista= valor.split(" ")
##            for j in range(len(lista)):
##                lista_2 = lista[j].split(",")
##                if len(lista_2)<=1:
##                    pass
##                else:
##                    n_l = list()
##                    for x in range(len(lista_2)):
##                        numero = float(lista_2[x])
##                        n_l.append(numero)
##                    coords.append(n_l)
##    arreglo = arcpy.Arreay()
##    puntos = arcpy.Point()
##    for c in coords:
##        puntos.X = c[0]
##        puntos.Y = c[1]
##        arreglo.add(puntos)
##    trazo=arcpy.Polyline(arreglo)
##    linea = arcpy.da.InsertCursor(nombre_salida,['@Shape'])
##    new_row = [trazo]
##    linea.insertRow(new_row)
##    del linea
##                    
    
