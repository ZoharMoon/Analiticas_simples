import pandas as pd

# Crear un DataFrame con los datos
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Maria', 'Carlos', 'Estela', 'Juan', 'Alexander', 'Kevin'],
    'Edad': [25, 35, 22, 28, 30, 47, 50, 48, 32, 21],
    'Género': ['Femenino', 'Masculino', 'Masculino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Masculino', 'Masculino'],
    'Fumador': [True, False, True, False, True, False, False, True, True, False]
}

df = pd.DataFrame(data)

# Convertir las columnas 'Edad' y 'Fumador' al tipo de dato correcto
df['Edad'] = df['Edad'].astype(int)
df['Fumador'] = df['Fumador'].astype(bool)

# Verificar tipos de datos en cada columna
print("Tipos de datos en cada columna:")
print(df.dtypes)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
conteo_fumadores = df.groupby(['Género', 'Fumador']).size().unstack()
print("\nCantidad de hombres fumadores vs mujeres fumadoras:")
print(conteo_fumadores)
