#Importación
import cvs

#Nombre del archivo cvs
filename = "LecturaE.csv"

#Inicializar titulos y lista de filas
Fields = []
rows = []

#Lectura del archivo csv
with open(filename, "r") as cvsfile

#crar ojeto de lectura de cvs
cvsreader = cvs.reader(cvsfile)

#Extracción de nombres de campos a través de la primera fila
fields = next(cvsreader)

#Extraer cada fila de datos una a una
for row in csvreader:
    rows.append(row)
  
