import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file = "data\Students_Grading_Dataset.csv"
df = pd.read_csv(file)
df.drop(columns=["First_Name","Last_Name","Email"],inplace=True)
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()

pass

df["attendance (%)"] = df["attendance (%)"].fillna(df.groupby(["department","gender","age"])["attendance (%)"].transform("mean")) 
df["assignments_Avg"] = df["assignments_avg"].fillna(df.groupby(["department","gender","age"])["assignments_avg"].transform("mean")) 

pass

tabla = pd.crosstab(df["parent_education_level"],df["family_income_level"]) # Me sirve para ver como se relacionan las dos variables
# Veo que no hay relacion directa como tal entre a mayor grado de educacion de los padres mas alto el ingreso, por lo tanto pongo Unknown

df["parent_education_level"].fillna("Unknown",inplace=True)






                    

