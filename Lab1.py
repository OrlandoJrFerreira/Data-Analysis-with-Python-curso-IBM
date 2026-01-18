import pandas as pd
import numpy as np

# Se variável url_PC = True uso a planilha do site [url/http:]; se url_PC = False uso a planilha armazenada no disco C:
url_PC = False

# A variável [endereco] contém o arquivo .csv que vai ser usado do url do site ou do arquivo.csv salvo na máquina local
if url_PC:
          # atribuo a variável endereco ao http do site com o dataset em formato .csv
          endereco = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01"
else:
          endereco ='C:/Users/Orlando Jr/PycharmProjects/Lab1analiseDeDados/imports-85.csv'
# Indentação (no IF/ELSE) é o afastamento de um texto ou código em relação à margem, usado para criar estrutura visual e hierárquica, sendo fundamental na legibilidade de documentos (como parágrafos) e obrigatória em linguagens como Python para definir blocos de código.
# O python não usa chaves { } para delimitar o if/else, ele usa a indentação!!!


# A função pd.read_csv(url/local C:) lê o arquivo csv. Nos parênteses, coloco o url(ou endereço C:), o Pandas irá ler o arquivo dentro do dataframe daquele endereço/local.
df = pd.read_csv(endereco,header=None)
#Os dados não possuem cabeçalho, usei o argumento [headers = None] dentro do métod0 read_csv(), assim o Pandas não irá configurar a primeira linha como [header/cabeçalho].

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
print(df.head(5))

# show the last 10 rows using dataframe.tail() method
print("The last 10 rows of the dataframe\n")
print(df.tail(10))

# Pandas automatically set the header with an integer starting from 0.
# To better describe our data, we can introduce a header.
# Thus, we have to add headers manually.
# First, we create a list "headers" that include all column names in order. Then, we use dataframe.columns = headers to replace the headers with the list we created.

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

# We replace headers and recheck our dataframe:
df.columns = headers
print(df.head(10))

# We need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
df1=df.replace('?',np.nan)
# The Python replace() method is a built-in string method used to return a copy of the string with all or a specified number of occurrences of a substring replaced with a new substring. It does not modify the original string because strings in Python are immutable.
# Data Type: np.nan is a float value. If you introduce np.nan into an array of integers, the entire array will be cast to a float data type to accommodate it.
df=df1.dropna(subset=["price"], axis=0)
# The dropna() function in Python is a pandas method used to remove missing values (NaN, None, or NaT) from a DataFrame or Series. By default, it removes any row that contains at least one missing value.
# In Python's data analysis libraries like pandas and NumPy, axis=0 primarily refers to operations along the rows (index), typically applied column-wise.
print(df.head(10))

# Find the name of the columns of the dataframe.
print(df.columns)

# Correspondingly, Pandas enables us to save the dataset to csv. By using the dataframe.to_csv() method, you can add the file path and name along with quotation marks in the brackets.
# For example, if you would save the dataframe df as automobile.csv to your local machine, you may use the syntax below, where index = False means the row names will not be written.
df.to_csv("automobile.csv", index=False)
# We can also read and save other file formats. We can use similar functions like pd.read_csv() and df.to_csv() for other data formats.

# The main types stored in Pandas dataframes are object, float, int, bool and datetime64. In order to better learn about each attribute, it is always good for us to know the data type of each column. In Pandas:
# O comando df.dtypes retorna uma series with the data type of each column.
# check the data type of data frame "df" by .dtypes
print(df.dtypes)
# As shown above, it is clear to see that the data type of "symboling" and "curb-weight" are int64, "normalized-losses" is object, and "wheel-base" is float64, etc.

# If we would like to get a statistical summary of each column e.g. count, column mean value, column standard deviation, etc., we use the describe method: dataframe.describe()
# This method will provide various summary statistics, excluding NaN (Not a Number) values: df.describe()
print(df.describe())

# This shows the statistical summary of all numeric-typed (int, float) columns.
# For example, the attribute "symboling" has 205 counts, the mean value of this column is 0.83, the standard deviation is 1.25, the minimum value is -2, 25th percentile is 0, 50th percentile is 1, 75th percentile is 2, and the maximum value is 3.
# However, what if we would also like to check all the columns including those that are of type object?
# You can add an argument include = "all" inside the bracket.
# describe all the columns in "df": df.describe(include = "all")
print(df.describe(include = "all"))
# Now it provides the statistical summary of all the columns, including object-typed attributes.
# We can now see how many unique values there, which one is the top value and the frequency of top value in the object-typed columns.
# Some values in the table above show as "NaN". This is because those numbers are not available regarding a particular column type.



#You can select the columns of a dataframe by indicating the name of each column. For example, you can select the three columns as follows:
# dataframe[[' column 1 ',column 2', 'column 3']]
# Where "column" is the name of the column, you can apply the method ".describe()" to get the statistics of those columns as follows:
# dataframe[[' column 1 ',column 2', 'column 3'] ].describe()
# Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.

# df[['length', 'compression-ratio']].describe()
print(df[['length', 'compression-ratio']].describe())

# df[['length', 'compression-ratio']].describe()
print (df[['length', 'compression-ratio']].describe())

# Another method you can use to check your dataset is: dataframe.info()
# It provides a concise summary of your DataFrame.
# This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
# look at the info of "df": df.info()
print(df.info())
