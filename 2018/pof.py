import arcpy
from os import walk
lista = list()
for (path, ficheros, archivos) in walk(r"J:\ENINCO\POF\GDB_CARDIQUE_PLANCHAS_IGAC\Base_25k"):
    for archivo in archivos:
        if archivo.endswith("mdb"):
            arcpy.env.workspace = r"%s\%s" % (path,archivo)
            datasets = arcpy.ListDatasets("","feature")
            n = 0
            for data in datasets:
                FeatureClass = arcpy.ListFeatureClasses("","ALL",data)
                for fc in FeatureClass:
                    cadena =  "%s\%s\%s" % (arcpy.env.workspace,data,fc)
                    if cadena.endswith("Drenaje_Doble"):
                        lista.append(cadena)
                        print cadena

print lista
arcpy.Merge_management(lista,"J:\ENINCO\POF\Fusionados.gdb\Drenaje_Doble")
                    
