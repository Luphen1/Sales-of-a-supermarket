#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#inspecting and loading of dataframe

df = pd.read_csv(r"C:\Users\LUPHEN\Documents\Kaggle Dataset\supermarket_sales.csv")
df.head()


# In[4]:


#identifying and handling for null values
df.isna().sum()


# In[5]:


#Checking for duplicates values
duplicate=df.drop_duplicates(inplace=True)
duplicate


# In[6]:


#Finding more about the dataframe
df.info()


# In[7]:


#standardizing datatypes
df['Date']=pd.to_datetime(df['Date'])
df['Date'] 
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time
df['Time']


# In[8]:


df.head()


# In[9]:


df.describe()


# In[35]:


#Visualize column Quantity for outliers

plt.figure(figsize=(7,6))
sns.boxplot(data=df, y='Quantity')
plt.ylabel('Quantity')
plt.title('Outliers')
plt.show()


# In[11]:


#1.	What is the distribution of sales across different branches?

#Grouping by branch and summing the Total sales
sales_distribution =df.groupby('Branch')['Total'].sum().round(2).sort_values().reset_index()

#Sorting the result by Total sales in descending order
sales_distribution_sorted=sales_distribution.sort_values('Total', ascending=False)
sales_distribution_sorted


# In[12]:


#Visualize the output code above

plt.figure(figsize=(7, 6))
sns.barplot(data=sales_distribution_sorted, x='Total', y='Branch')
plt.xlabel('Total')
plt.ylabel('Branch')
plt.title('Sales by branch')
plt.show()


# In[13]:


#2.	How does customer type (member/normal) sales revenue varies across the dataset?

customer_sales_revenue =df.groupby('Customer type')['Total'].sum().round(2).reset_index()
customer_sales_revenue


# In[36]:


#Visualize the output code above

plt.figure(figsize=(7,6))
sns.barplot(data=customer_sales_revenue, x='Customer type',y='Total')
plt.xlabel('customer type')
plt.ylabel('Total')
plt.title('Revenue by customer type')
plt.show()


# In[15]:


get_ipython().run_line_magic('pinfo', 'line')

gross_income=df.groupby('Product line')['gross income'].mean().round(2).reset_index()
gross_income_sorted=gross_income.sort_values('gross income',ascending=False)
gross_income_sorted


# In[37]:


plt.figure(figsize=(7,6))
sns.barplot(data=gross_income_sorted,x='gross income',y='Product line')
plt.title('Average gross income by product line')
plt.show()


# In[17]:


#4.What month has the best revenue income?

# Extract month from 'Date' column
df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%b')
df['Month']
monthly_sales = df.groupby('Month')['Total'].sum().round(2).reset_index()
monthly_sales 


# In[38]:


plt.figure(figsize=(7,6))
sns.barplot(monthly_sales, x='Month', y='Total')
plt.title('Revenue income by month')
plt.show()


# In[19]:


#5.Find payment type with the most revenue.

Payment_revenue=df.groupby('Payment')['Total'].sum().round(2).reset_index()
Payment_revenue_sorted=Payment_revenue.sort_values('Total',ascending=False)
Payment_revenue_sorted


# In[39]:


plt.figure(figsize=(7,6))
sns.barplot(Payment_revenue_sorted,x='Total',y='Payment')
plt.title('Payment type by revenue')
plt.show()


# In[21]:


#6.Find the correction relationship between cogs,gross income,Rating,Unit price,Quantity and Tax 5%.

corr_Relationship = df[['cogs','gross income','Rating','Unit price','Quantity','Tax 5%']].corr()
corr_Relationship


# In[41]:


plt.figure(figsize=(10, 7))
sns.heatmap(corr_Relationship, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Relationship')
plt.show()


# In[23]:


#Renaming columns 

df.rename(columns={'cogs': 'Cogs', 'gross margin percentage': 'Gross Margin Percentage', 'gross income': 'Gross Income'}, inplace=True)
df


# In[24]:


df.info()


# In[70]:


#7.What is the percentage gender demographic across the dataset?
total_gender=df['Gender'].size
gender_demographic=(df.groupby('Gender').size()/total_gender*100).round(2)
gender_demographic


# In[50]:


plt.figure(figsize=(7,6))
gender_demographic.plot(kind='pie',autopct='%.2f',startangle= 60)
plt.title('Gender Demographic')
plt.show()


# In[27]:


#8.What is the average rating for each product lines?

product_line_rating = df['Rating'].groupby(df['Product line']).mean().round(2).reset_index()
product_line_rating_sorted=product_line_rating.sort_values('Rating',ascending=False)
product_line_rating_sorted


# In[52]:


sns.barplot(product_line_rating_sorted,x='Rating',y='Product line')
plt.title('Average rating by product line')
plt.show()
         


# In[29]:


#9.What city has the best order quantity?
city_order_quantity=df.groupby('City')['Quantity'].size()
city_order_quantity


# In[53]:


plt.figure(figsize=(7,6))
city_order_quantity.plot(kind='pie',autopct='%.2f',startangle= 60)
plt.title('City Sales')


# In[62]:


#10.Which product lines have the highest and lowest percentage sales volumes?

total_sales = df['Total'].sum()
product_line_sales_percentage = (df.groupby('Product line')['Total'].sum() / total_sales * 100).round(2)
sorted_product_line=product_line_sales_percentage.sort_values(ascending=False)
sorted_product_line


# In[65]:


sorted_product_line.plot(kind='pie',autopct='%.2f',startangle= 60)
plt.title('Percentage sales by product line')
plt.show()

