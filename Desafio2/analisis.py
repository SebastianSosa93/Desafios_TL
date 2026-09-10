import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./Desafio2/data/programming_language_survey4004.csv")
head = df.head()
print("Primeros 5 registros del dataset:")
print(head)

tail = df.tail()
print("\nÚltimos 5 registros del dataset:")
print(tail)

print("\nConjunto de datos completo:")
print(df)

nulos = df.isnull().sum()
print("\nValores nulos por columna:")
print(nulos)

duplicados = df.duplicated().sum()
print("\nCantidad de registros duplicados:", duplicados)

print("\n Informacion del dataset:")
info = df.info()

print("\nDescripción estadística:")
print(df.describe())

print("\nLenguajes de programación únicos:")
print(df['Preferred Programming Language'].unique())

print("\nPuestos de trabajo únicos:")
trabajos = df['Work'].str.lower()
print(trabajos.unique())

print("\nEdades:")
print(df["Age"])

print("\nEdades únicas:")
print(df["Age"].unique())

print("\nEncuestados entre 18 y 30 años:")
print(df[(df['Age'] >= 18) & (df['Age'] <= 30)])

print("\nEncuestados entre 30 y 50 años:")
print(df[(df['Age'] >= 30) & (df['Age'] <= 50)])

print("\nEncuestados entre 50 y 70 años:")
print(df[(df['Age'] >= 50) & (df['Age'] <= 70)])

print("\nEncuestados mayores de 70 años:")
print(df[df['Age'] >= 70])

print("\nWeb developers que prefieren Java:")
print(df[(df['Preferred Programming Language'] == 'Java') & (df['Work'] == 'Web Developer')])

# df = df.drop_duplicates()
# print("\nCantidad de registros duplicados después de eliminar duplicados:", df.duplicated().sum())

df = df.fillna('N/A')
print("\nValores nulos reemplazados por 'N/A':")
print(df.isnull().sum())

df.info()

# popularidad de lenguajes segun preferencia de los encuestados
popularidad = df['Preferred Programming Language'].value_counts()
print("\nPopularidad de lenguajes de programación según preferencia de los encuestados:")
print(popularidad)
plt.figure(figsize=(12,6))
sns.barplot(x=popularidad.index, y=popularidad.values,hue=popularidad.index, palette="viridis")
plt.title("Popularidad de lenguajes de programación según preferencia de los encuestados")
plt.xlabel("Lenguaje de programación")
plt.ylabel("Cantidad de encuestados")
plt.xticks(rotation=45)
plt.show()

#grafico de barras de la edad promedio por lenguaje de programación
promedio = df.groupby('Preferred Programming Language')['Age'].mean().sort_values(ascending=False)
plt.figure(figsize=(12,6))
sns.barplot(x=promedio.values, y=promedio.index, hue=promedio.index, palette="viridis")
plt.title("Edad promedio por lenguaje de programación")
plt.xlabel("Lenguaje de programación")
plt.ylabel("Edad promedio")
plt.xticks(rotation=45)
plt.show()

#grafico de la cantidad de web developers que prefieren cada lenguaje de programación
web_developers = df[df['Work'] == 'Web Developer']['Preferred Programming Language'].value_counts()
plt.figure(figsize=(12,6))
sns.barplot(x=web_developers.index, y=web_developers.values, hue=web_developers.index, palette="viridis")
plt.title("Cantidad de Web Developers por lenguaje de programación preferido")
plt.xlabel("Lenguaje de programación")
plt.ylabel("Cantidad de Web Developers")
plt.xticks(rotation=45)
plt.show()