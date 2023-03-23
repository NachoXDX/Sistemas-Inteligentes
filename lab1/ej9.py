import csv
import pandas as pd
from matplotlib import pyplot

url = 'https://raw.githubusercontent.com/TheCodingRecruiter/Machine-Learning-Salary-Prediction-Model/master/Salary_Data.csv'
df1 = pd.read_csv(url)  # Importo el archivo csv desde el url y lo asigno a df1
df1Trad = df1.rename(columns = {"YearsExperience" : "Años De Experiencia", "Salary" : "Salario"})
df1Norm = (df1-df1.min())/(df1.max()-df1.min())

salaryDf = df1["YearsExperience"]
expDf = df1["Salary"]

pyplot.scatter(salaryDf,expDf)
pyplot.title("Dispersion de Experiencia y Salario")
pyplot.xlabel("Experiencia (Años)")
pyplot.ylabel("Salario ($USD)")
pyplot.show()

print(df1[df1["Salary"] > 50000]["YearsExperience"])