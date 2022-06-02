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
NPersonasEnCasa = aux.shape[0]
print(f'Numero de personas que se encuentran en atención en casa: {NPersonasEnCasa}')

#5. Número de personas que se encuentran recuperados
aux = data.loc[(data['Recuperado'] == 'Recuperado')]
NPersonasRecuperadas = aux.shape[0]
print(f'Numero de personas que se encuentran Recuperados: {NPersonasRecuperadas}')

#6. Número de personas que ha fallecido
aux = data.loc[(data['Estado'] == 'Fallecido')]
NPersonasFallecidas = aux.shape[0]
print(f'Numero de personas que han fallecido: {NPersonasFallecidas}')

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

#12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size()
dptofallecido = aux.sort_values(ascending=False).head(10)
print(f'Lista de los 10 departamentos con mas fallecidos: \n {dptofallecido}')

#13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size()
dptorec = aux.sort_values(ascending=False).head(10)
print(f'Lista de los 10 departamentos con mas recuperados: \n {dptorec}')

#14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
aux = data[(data['Estado'] == 'Leve') & (data['Estado'] == 'Moderado') & (data['Estado'] == 'Grave')].groupby('Nombre municipio').size()
muncont = data['Nombre municipio'].value_counts().head(10)
print(f'Lista de los 10 municipios con mas casos: \n {muncont}')

#15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size()
munfallecidos = aux.sort_values(ascending=False).head(10)
print(f'Lista de los 10 municipios con mas fallecidos: \n {munfallecidos}')

#16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size()
Munrecuperados = aux.sort_values(ascending=False).head(10)
print(f'Lista de los 10 municipios con mas recuperados: \n {Munrecuperados}')

#17. Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados
aux = data.groupby(['Nombre departamento', 'Nombre municipio']).size()
aux.sort_values(ascending=False)

#18. Número de Mujeres y hombres contagiados por ciudad por departamento
aux = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo']).size()
aux.sort_values(ascending=False)

#19. Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
aux = data.groupby(['Nombre departamento', 'Nombre municipio', 'Edad']).size()
aux.sort_values(ascending=False)

#20. Liste de mayor a menor el número de contagiados por país de procedencia
aux = data.groupby(['Nombre del país']).size()
Paisctg = aux.sort_values(ascending=False)
print(f'Lista de mayor a menor de num de contagiados por Pais: \n {Paisctg}')

#21. Liste de mayor a menor las fechas donde se presentaron mas contagios
aux = data.groupby(['Fecha de diagnóstico']).size()
fechactg = aux.sort_values(ascending=False)
print(f'Lista de mayor a menor de fechas de mas contagios: \n {fechactg}')

#22. Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia

cantfallecidos= data[data['Estado'] == 'Fallecido'].shape[0]
cantrecuperados = data.query('Recuperado == "Recuperado"').shape[0]
cantCasos = data.shape[0]

tasaMortalidad = cantfallecidos / cantCasos * 100
tasaRecuperacion = cantrecuperados / cantCasos * 100

print(f'La tasa de Mortalidad es: {tasaMortalidad}')
print(f'La tasa de Recuperacion es: {tasaRecuperacion}')

#23. Liste la tasa de mortalidad y recuperación que tiene cada departamento

Fallecidosdpto = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size()
Recuperadosdpto = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size()
Casosdpto = data.groupby('Nombre departamento').size()

tasaMortalidadDpto = Fallecidosdpto / Casosdpto * 100
tasaRecuperacionDpto = Recuperadosdpto / Casosdpto * 100

print(f'La tasa de Mortalidad por departamento es: \n {tasaMortalidadDpto}')
print(f'La tasa de Recuperacion por departamento es: \n {tasaRecuperacionDpto}')

#24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad

FallecidosCd = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size()
RecuperadosCd = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size()
CasosCd = data.groupby('Nombre municipio').size()

tasaMortalidadCd = FallecidosCd / CasosCd * 100
tasaRecuperacionCd = RecuperadosCd / CasosCd * 100

print(f'La tasa de Mortalidad por Ciudad es: \n {tasaMortalidadCd}')
print(f'La tasa de Recuperacion por Ciudad es: \n {tasaRecuperacionCd}')

#25. Liste por cada ciudad la cantidad de personas por atención
atencionCd = data.groupby(['Nombre municipio', 'Ubicación del caso']).size()
print(f'Lista de personas en atencion por ciudad: \n{atencionCd}')

#26. Liste el promedio de edad por sexo por cada ciudad de contagiados
promEdadxSexo = data.groupby(['Nombre municipio', 'Sexo']).Edad.mean()
print(f'Lista promedio de edad por ciudad contafiados: \n{promEdadxSexo}')

#27. Grafique las curvas de contagio, muerte y recuperacion de toda Colombia 
contagio = data.groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Contagios')
plt.show(contagio)

fallecido = data[data['Recuperado'] == 'fallecido'].groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Fallecidos')
plt.show(fallecido)

recuperado = data[data['Recuperado'] == 'Recuperado'].groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Recuperados')
plt.show(recuperado)

# 28. Grafique las curvas de contagio, muerte y recuperacion de los 10 departamentos con mas casos acumulados
ctgdpto = data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas contagios')
plt.show(ctgdpto)

curv_fall_dpto = data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas personas fallecidas')
plt.show(curv_fall_dpto)

curv_recu_dpto = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas personas recuperadas')
plt.show(curv_recu_dpto)

# 29. Grafique las curvas de contagio, muerte y recuperacion de las 10 ciudades con mas casos acumulados
curv_contg_mp= data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas contagios')
plt.show(curv_contg_mp)

curv_falle_mp = data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas personas fallecidas')
plt.show(curv_falle_mp)

curv_recu_mp = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas personas recuperadas')
plt.show(curv_recu_mp)

#30. Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia
fallecidos = data[data['Recuperado'] == 'fallecido'].groupby('Edad').size().sort_values(ascending = False)
print(f'{fallecidos}')





























