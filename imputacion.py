import pandas as pd

file = r"Students_Grading_Dataset.csv"
df = pd.read_csv(file)
df.drop(columns=["First_Name","Last_Name","Email"],inplace=True)

df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()

df["attendance (%)"] = df["attendance (%)"].fillna(df.groupby(["department","gender","age"])["attendance (%)"].transform("mean")) 
df["assignments_avg"] = df["assignments_avg"].fillna(df.groupby(["department","gender","age"])["assignments_avg"].transform("mean")) 


tabla = pd.crosstab(df["parent_education_level"],df["family_income_level"]) 

# Veo que no hay relacion directa como tal entre a mayor grado de educacion de los padres mas alto el ingreso, por lo tanto pongo Unknown

df["parent_education_level"].fillna("Unknown",inplace=True)





                    

