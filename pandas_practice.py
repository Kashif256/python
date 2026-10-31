print("Pandas")

# Pandas is a Python library used for data manipulation, data cleaning, data analysis and handling structured data.
# Pandas helps us work with data stored in Excel files, CSV files and tables.

# DataFrame - > df

print ("The method is for pdf reader")

## Import PdfReader from pypdf
#from pypdf import PdfReader

## Open the PDF file
#reader = PdfReader(r"C:\Users\kashi\Downloads\dummy_employee_dataset_readable.pdf")


# #Loop through every page in the PDF
#for page in reader.pages:

    # #Extract and print the text from each page
    #print(page.extract_text())

print("for printing csv files")
import pandas as pd

df = pd.read_csv(r"C:\Users\kashi\Downloads\duumy_dataset_py.csv")

#print(df)

#print(df.head(5))  # for printing only first  5 rows

#print(df.tail(2)) # for printing last values

#df.info() # for printing the information which means what does it contains 

# print(df.describe()) 

####  df.head() → What does my data look like?
####  df.info() → What is the structure of my data?
####  df.describe() → What do the numerical statistics tell me?


# print(df.columns) # print the columns name

# print(df.T)  # transpose  is used to change the row to column and column to row

#new_df = df.sort_values('Age')
#print(new_df.head(5))
#print(new_df)   # the sort_values is used to assign data from assending to desending order

#new_df_1= df.sort_values('Name', ascending = True)  # the true is used for ascending order if we need in descendign then we can give ascending as false
# print(new_df_1)

#print(df['Salary_INR'])   # for specific column from the table

# df_new = df['Salary_INR'] + 1000
# print(df_new.head(5))  # it will add plus 1000 in salary 

# df_age=df[df.Age>30]
# print(df_age)  
# print(len(df_age))

print("To fill the null value we use 'fillna' tp fill the null values")

# df_age=df['Age'].fillna(15):
# print(df_age)


print("To remove column we use 'df.pop or df.drop' with use of that we can remove the column")

# df_column = df.pop('Salary_INR')
# print(df_column)
# print(df.head())
      