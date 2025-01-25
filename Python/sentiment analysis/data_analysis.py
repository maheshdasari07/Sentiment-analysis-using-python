import pandas as pd
import matplotlib.pyplot as plt # import after complete pandas

#load the csv file
df = pd.read_csv('data.csv')

#display the first few rows of the data
print(df.head())

#calculate the avarage of a column
avg = df['Age'].mean()
print(f"Age avarage: {avg}")

#count the Unique Values
uv = df['Age'].nunique()
print(f"Unique values: {uv}")

#Describe the data, get descriptive statistics for all numerical column in your dataset
print(df.describe())

#find Missing Values in each column
mv = df.isnull().sum()
print("Missing values in each column:\n", mv)

#Filter Rows based on a condition, eg - filter all employees from the engineering department
eng_emp = df[df['Department'] == 'Engineering']
print(eng_emp)

#Find min and max, eg - get the employee with the highest salary
max_salary = df['Salary'].max()
ms_emp = df[df['Salary'] == max_salary]
print("Highest paid employee:\n",ms_emp)

#count frequency of each value in a column, eg - count how many employees are in each department
dep_count = df['Department'].value_counts()
print("Number of employees in each departmnet:\n",dep_count)

#sort data by column
sort = df.sort_values(by='Age', ascending=False)
print("Senior to junior employee:\n",sort)

#add a new column based on condition, eg - add Experience based on age
df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x>=30 else 'Junior')
print("Data with Experience:\n",df)

# data visualization

#plot a pie chat
plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140)
plt.title("Department")
plt.show()