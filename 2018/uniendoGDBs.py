import arcpy
from os import walk
arcpy.env.workspace = r"Z:\EJECUCION\2017\PUERTO SALGAR\11. CARTOGRAFIA\IGAC\CARTOGRAFIA 1_10.000-20180417T215049Z-001\CARTOGRAFIA 1_10.000\GEODATABASE\169IIIA4_RS_2013_V1.mdb"
datasets = arcpy.ListDatasets("","feature")
n = 0
lista = list()
arreglo = {}
for data in datasets:	
	FeatureClass = arcpy.ListFeatureClasses("","ALL",data)
	for fc in FeatureClass:
		lista.append(fc)
	arreglo[data]=lista
	lista = list()

for grupo, shps in arreglo.items():
        arcpy.CreateFeatureDataset_management(r"Z:\EJECUCION\2017\PUERTO SALGAR\11. CARTOGRAFIA\IGAC\CARTOGRAFIA 1_10.000-20180417T215049Z-001\CARTOGRAFIA 1_10.000\compilada.gdb", grupo,r"Z:\EJECUCION\2017\PUERTO SALGAR\11. CARTOGRAFIA\IGAC\CARTOGRAFIA 1_10.000-20180417T215049Z-001\CARTOGRAFIA 1_10.000\GEODATABASE\169IIIA4_RS_2013_V1.mdb\Relieve\Curva_Nivel")
        ## la linea anterior crea el dataset de guardado
        for capa in shps:
        	for (path, ficheros, archivos) in walk(r"Z:\EJECUCION\2017\PUERTO SALGAR\11. CARTOGRAFIA\IGAC\CARTOGRAFIA 1_10.000-20180417T215049Z-001\CARTOGRAFIA 1_10.000\GEODATABASE"):
        	    for archivo in archivos:
        	        if archivo.endswith("mdb"):
        	            arcpy.env.workspace = r"%s\%s" % (path,archivo)
        	            datasets = arcpy.ListDatasets("","feature")
        	            n = 0
        	            for data in datasets:
        	                FeatureClass = arcpy.ListFeatureClasses("","ALL",data)
        	                for fc in FeatureClass:
        	                    cadena =  "%s\%s\%s" % (arcpy.env.workspace,data,fc)
        	                    capas = "\%s" % capa
        	                    if cadena.endswith(capas):
        	                    	lista.append(cadena)
        	                    	print cadena
        	
        	forMerge = list()
        	i = 0
        	for Merge in range(len(lista)):
        		if i < len(lista)-1:
        			desc = arcpy.Describe(lista[i])
        			geometry1 = desc.shapeType
        			desc2 = arcpy.Describe(lista[i+1])
        			geometry2 = desc2.shapeType
        		else:
        			desc = arcpy.Describe(lista[i])
        			geometry1 = desc.shapeType

        		print "%s es igual a %s" % (geometry1,geometry2)
        		if geometry1 == geometry2:
        			forMerge.append(lista[i])
        		else:
        			pass
        		i = i+1
        	
        	guardado = r"Z:\EJECUCION\2017\PUERTO SALGAR\11. CARTOGRAFIA\IGAC\CARTOGRAFIA 1_10.000-20180417T215049Z-001\CARTOGRAFIA 1_10.000\compilada.gdb\%s\%s" % (grupo,capa)
        	arcpy.Merge_management(forMerge,guardado)
        	forMerge = list()
        	lista = list()
                
            
        
    
