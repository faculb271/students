# Students Grading Dataset Imputation

Este proyecto realiza la imputación de datos faltantes en un conjunto de datos de calificaciones de estudiantes sacado de Kaggle

## Estructura del Proyecto

- `imputacion.py`: Script principal que realiza la imputación de datos faltantes.
- `Students_Grading_Dataset.csv`: Conjunto de datos de calificaciones de estudiantes.

## Requisitos

- Python 3
- Pandas

Puedes instalar las dependencias necesarias utilizando `pip`

## Descripción del Script

El script `imputacion.py` realiza las siguientes tareas:

1. Carga el conjunto de datos `Students_Grading_Dataset.csv`.
2. Elimina las columnas `First_Name`, `Last_Name` y `Email`.
3. Limpia los nombres de las columnas eliminando espacios y convirtiéndolos a minúsculas.
4. Imputa los valores faltantes en las columnas `attendance (%)` y `assignments_avg` utilizando la media agrupada por `department`, `gender` y `age`.
5. Crea una tabla cruzada (`crosstab`) para analizar la relación entre el nivel educativo de los padres y el nivel de ingresos familiares.
6. Imputa los valores faltantes en la columna `parent_education_level` con el valor "Unknown".

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.