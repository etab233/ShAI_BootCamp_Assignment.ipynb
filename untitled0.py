# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oGONJgqzDPgpDuFccyo3gNBUix5TbGJa
"""

import pandas as pd
import numpy as np
from scipy import stats
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
sal=pd.read_csv( "Salaries.csv")
data=pd.DataFrame(sal)
num_rows=len(data)
num_column=len(data.columns)
print("Number of rows=", num_rows)
print("Number of columns=", num_column)
data.dtypes
print(data.isnull())

mean=np.mean(data.loc[:,"TotalPay"])
print("mean= ",mean)
median=np.median(data.loc[:,"TotalPay"])
print("median= ",median)
mode=stats.mode(data.loc[:,"TotalPay"])
print("mode= ",mode)
m2=data["TotalPay"].max()
print("maximum value is ", m2)
m1=data["TotalPay"].min()
print("minimum value is ", m1)
print("Salaries range between " ,m1, " and ", m2)
print("Standard deviation", statistics.stdev(data["TotalPay"]))

# we can delete rows or columns with missing values, but i think that
# filling the missing data with suitable values is better in this case
data["EmployeeName"].fillna("Ali" ,inplace= True)
data["JobTitle"].fillna("Engineer", inplace=True)
data["BasePay"].fillna(data["BasePay"].mean(), inplace=True)
data["OvertimePay"].fillna(data["OvertimePay"].mean(),inplace= True)
data["OtherPay"].fillna(data["OtherPay"].mean(),inplace= True)
data["Benefits"].fillna(0,inplace= True)
data["TotalPay"].fillna(data["TotalPay"].mean(),inplace= True)
data["TotalPayBenefits"].fillna(data["TotalPayBenefits"].mean(),inplace= True)
data["Year"].fillna(2000, inplace=True)
data["Notes"].fillna("No thing", inplace=True)
data["Agency"].fillna("San Francisco", inplace=True)
data["Status"].fillna("Active", inplace=True)

sns.histplot(data["TotalPay"], bins=30, kde=True, color='lightgreen', edgecolor='red')
plt.xlabel('Salaries')
plt.ylabel('Count')
plt.title('histograms to visualize the distribution of salaries')
plt.show()

plt.figure(figsize=(10,5))
data['JobTitle'].value_counts().head(10).plot(kind='pie' , autopct='%1.1f%%')
plt.show()

g = data.groupby('JobTitle')['TotalPay'].mean().sort_values(ascending=False)
print(g)

plt.figure(figsize=(10, 5))
sns.scatterplot(x=data['TotalPay'], y=data['BasePay'])
plt.show()

##################################################
# قمنا بداية بتحليل البيانات وتحدبد عدد ونوع كل عمود
#ثم ايجاد أكبر وأصغر راتب بالاضافة الى اكثر راتب مكرر والمتوسط الحسابي
# ثالثاً قمنا بمعالجة البيانات في الجدول وفضلنا عدم حذف الأسطر أو الأعمدة
#واكتفينا بتعديل البيانات فقط
#وبعد ملاحظة الرسوم البيانية وجدنا أن أكثر مهنة موجودة هي
#transit operator
#بنسبة 22 بالمئة

from google.colab import drive
drive.mount('/content/drive')