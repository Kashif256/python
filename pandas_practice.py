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
#df_new= df['Salary_INR'].apply(np.sqrt)
# print(df_new)


print("Combining data frames:")

# ==========================================
# COMBINING DATAFRAMES IN PANDAS
# ==========================================

# Combining DataFrames means bringing two or more
# DataFrames together into a single DataFrame.

# Example:

import pandas as pd

# First DataFrame - Employee Details
df1 = pd.DataFrame({
    "Employee_ID": [101, 102, 103],
    "Name": ["Arun", "Kashif", "Sanu"]
})

# Second DataFrame - Employee Salaries
df2 = pd.DataFrame({
    "Employee_ID": [101, 102, 104],
    "Salary": [25000, 30000, 35000]
})

# ==========================================
# JOIN OPERATION IN PANDAS
# ==========================================

# Join operation combines two DataFrames
# based on a common column or index.

# Here, Employee_ID is the common column.

# INNER JOIN
# Returns only matching records from both DataFrames.

inner_df = pd.merge(df1, df2, on="Employee_ID", how="inner")
print(inner_df)


# LEFT JOIN
# Returns all records from the left DataFrame
# and matching records from the right DataFrame.
# If there is no match, NaN will appear.

left_df = pd.merge(df1, df2, on="Employee_ID", how="left")
print(left_df)


# RIGHT JOIN
# Returns all records from the right DataFrame
# and matching records from the left DataFrame.

right_df = pd.merge(df1, df2, on="Employee_ID", how="right")
print(right_df)


# OUTER JOIN
# Returns all records from both DataFrames.
# If there is no match, NaN will appear.

outer_df = pd.merge(df1, df2, on="Employee_ID", how="outer")
print(outer_df)


# ==========================================
# DIFFERENCE BETWEEN CONCAT, MERGE AND JOIN
# ==========================================

# 1. concat() - Combines DataFrames vertically or horizontally.
# 2. merge() - Combines DataFrames using common columns or keys.
# 3. join()  - Joins DataFrames mainly using their indexes.


# ==========================================
# QUICK SUMMARY
# ==========================================

# INNER JOIN  - Only matching records from both DataFrames.
# LEFT JOIN   - All records from the left DataFrame, if not exist same then NaN will appear
# RIGHT JOIN  - All records from the right DataFrame, if not exist same then NaN will appear
# OUTER JOIN  - All records from both DataFrames, if not exist same then NaN will appear.

# CONCATENATION IN PANDAS
# ==========================================

# pd.concat() is used to combine DataFrames.
# It can combine them vertically (rows)
# or horizontally (columns).

# Example:
# pd.concat([df1, df2], axis=0)  # Vertical
# pd.concat([df1, df2], axis=1)  # Horizontal

print("Concatenation of DataFrames:")

concat_df = pd.concat([df1, df2])
print(concat_df)


# MERGE IN PANDAS

# merge() is used to combine two DataFrames
# based on a common column or key.

# Syntax:
# pd.merge(df1, df2, on="Common_Column")

# Example:
# pd.merge(df1, df2, on="Employee_ID")

# Employee_ID is the common column in both DataFrames.

print("Merge operation of DataFrames:")

import pandas as pd

df1 = pd.DataFrame({
    "Employee_ID": [101, 102, 104],
    "Name": ["Arun", "Kashif", "Sanu"]
})

df2 = pd.DataFrame({
    "Employee_ID": [101, 102, 103],
    "Salary": [25000, 30000, 35000]
})

# Merge two DataFrames using Employee_ID
new_df = pd.merge(df1, df2, on="Employee_ID") # we can also use how="inner" for inner join, how="left" for left join, how="right" for right join, and how="outer" for outer join.

print(new_df)


# ==========================================
# LOC VS ILOC IN PANDAS
# ==========================================

# Both loc and iloc are used to select specific
# rows and columns from a DataFrame.


# ==========================================
# 1. LOC IN PANDAS
# ==========================================

# loc is used to select rows and columns using labels.


# ==========================================
# 2. ILOC IN PANDAS
# ==========================================

# iloc is used to select rows and columns using
# integer positions.

# ==========================================
# 3. PRACTICAL EXAMPLE
# ==========================================

import pandas as pd

df = pd.DataFrame({
    "Name": ["Arun", "Kashif", "Sana", "Rahul"],
    "Age": [24, 22, 23, 28],
    "Salary": [28000, 30000, 32000, 52000]
})
print("loc and iloc examples:")

# Selecting a row using loc
print(df.loc[1])

# Selecting a row using iloc
print(df.iloc[1])

# Selecting specific columns using loc
print(df.loc[:, ["Name", "Salary"]])

# Selecting specific columns using iloc
print(df.iloc[:, [0, 2]])

# Selecting the third employee using iloc
print(df.iloc[2])


# ==========================================
# 4. DIFFERENCE BETWEEN LOC AND ILOC
# ==========================================

# LOC:
# 1. Label-based selection.
# 2. Uses row and column labels.
# 3. Includes the ending label in slicing.

# ILOC:
# 1. Integer position-based selection.
# 2. Uses integer positions.
# 3. Excludes the ending position in slicing.


# ==========================================
# QUICK SUMMARY
# ==========================================

# loc  = Label-based selection.
# iloc = Integer position-based selection.

# Remember:
# loc  -> Labels
# iloc -> Integer positions