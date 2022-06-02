# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:24:58 2022

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)

# Conocer las dimensiones del archivo (data.shape)

# Conocer las columnas del arhivo(data.columns)

# Cantidad de elementos del arhivo (data.size)

# Para saber cuantos registros hay por columna (data.count())

# Acceder a los elementos de una columna
data['Código ISO del país']

# Eliminar columnas de un dataset

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)


# Agrupar por columnas los resultados
data['Estado'].value_counts()

# Normalizar la columna de Estado

data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

# Cuantas personas murieron por covid en Colombia
cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
print(cantidad_muertes)

# Normalizar columna sexo

data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'

# Cuantas mujeres fallecieron en Colombia
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F') ]
cantidad_muertes_mujeres = aux.shape[0]

# Cuantas personas fallecieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Nombre municipio'] == 'BARRANQUILLA') ]
cantidad_muertes_BQ = aux.shape[0]

# Cuantas mujeres fallecieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F') & (data['Nombre municipio'] == 'BARRANQUILLA') ]
cantidad_muertes_mj_BQ = aux.shape[0]


# Tasa de mortalidad del covid en Colombia

cantidad_casos = data.shape[0]
tasa_mortalidad = cantidad_muertes / cantidad_casos * 100

# Agrupar por Coluna Sexo, Estado
data.groupby(['Sexo', 'Estado']).size()
data.groupby(['Estado', 'Sexo']).size()

# Normalizar columna Estado

data.loc[data['Estado'] == 'M'] = 'Moderado'
data.loc[data['Sexo'] == 'F'] = 'Fallecido'

# Normalizar columna Ubicacion del caso
data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'

data.loc[data['Edad'] == 'Casa'] = 36
data.loc[data['Edad'] == 'Leve'] = 36
data.loc[data['Edad'] == 'M'] = 36
data.loc[data['Edad'] == 'F'] = 36

# Liste por orden descendente las 10 ciudades con mas casos reportados

data['Nombre municipio' ].value_counts().head(10)

# Eliminar filas por condicion

# Curva de contagios en Barranquilila

data[(data['Nombre municipio'] == 'BOGOTA') & (data['Estado'] == 'Fallecido')].groupby('Fecha de diagnóstico').size().plot()

#TALLER

#1. Número de casos de Contagiados en el País.
contagiados = data['Estado'].count()
print(f'El numero de contagiados es: {contagiados}')


#2. Número de Municipios Afectados
municipios = data['Nombre municipio'].nunique()
print(f'El numero de Municipios Afectados es: {municipios}')

#3. Liste los municipios afectados (sin repetirlos)
Muni = data['Nombre municipio'].value_counts()
print(f'Lista de los municipios afectados (sin repetirlos): \n {Muni}')

#4. Número de personas que se encuentran en atención en casa
aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
NumeroDePersonasEnCasa = aux.shape[0]
print(f'Numero de personas que se encuentran en atención en casa: {NumeroDePersonasEnCasa}')

#5. Número de personas que se encuentran recuperados
aux = data.loc[(data['Recuperado'] == 'Recuperado')]
NumeroDePersonasRecuperadas = aux.shape[0]
print(f'Numero de personas que se encuentran Recuperados: {NumeroDePersonasRecuperadas}')

#6. Número de personas que ha fallecido
aux = data.loc[(data['Estado'] == 'Fallecido')]
NumPersonasFallecidas = aux.shape[0]
print(f'Numero de personas que han fallecido: {NumPersonasFallecidas}')

#7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,Relacionado)
data.sort_values(by=data.loc[(data['Tipo de contagio'] == 'Importado')],ascending=False )
data.sort_values(by=data.loc[(data['Tipo de contagio'] == 'Relacionado')],ascending=False )

#8. Número de departamentos afectados
data['Nombre departamento'].nunique()
dpto = data['Nombre departamento'].nunique()
print(f'El numero de departamentos Afectados es: {dpto}')

#9. Liste los departamentos afectados(sin repetirlos)
Adpto = data['Nombre departamento'].value_counts()
print(f'Lista de los departamentos afectados (sin repetirlos): \n {Adpto}')

#10. Ordene de mayor a menor por tipo de atención
data.sort_values(by='Tipo de recuperación',ascending=False )

#11.Liste de mayor a menor los 10 departamentos con mas casos de contagiados
aux = data[(data['Estado'] == 'Leve') & (data['Estado'] == 'Moderado') & (data['Estado'] == 'Grave')].groupby('Nombre departamento').size()
dptomayor = data['Nombre departamento'].value_counts().head(10)
print(f'Lista de los 10 departamentos con mas casos: \n {dptomayor}')






























