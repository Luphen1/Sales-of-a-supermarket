# Sales-of-a-supermarket


#### Table of Contents
---------------------

-  [Project Overview](#Project_Overview)

-  [Data Source](#Data_Source)

-  [Tools](#Tools)

-  [Data Cleaning/Preparation](#Data_Cleaning/Preparation)

-  [Exploration Data Analysis](#Exploration_Data_Analysis)

-  [Results/Findings](#Results/Findings)

-  [Recommendations](#Recommendations)


### Project Overview

The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data. 

I utilize the 'groupby' function in pandas to identify trends and patterns throughout my analysis. This approach will make informed decisions aimed at enhancing the business.

![Screenshot (33)](https://github.com/Luphen1/Sales-of-a-supermarket/assets/140397207/3011c378-1c90-46e3-a939-4005fa48fc58)

### Data Sources
The primary dataset used for this project was downloaded here [https://www.kaggle.com/datasets/lovishbansal123/sales-of-a-supermarket](https)

Below is a detailed breakdown of each column descriptions below:


Invoice id: Computer generated sales slip invoice identification number.

Branch: Branch of supercenter (3 branches are available identified by A, B and C).

City: Location of supercenters.

Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.

Gender: Gender type of customer.

Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel.

Unit price: Price of each product in $.

Quantity: Number of products purchased by customer.

Tax: 5% tax fee for customer buying.

Total: Total price including tax.

Date: Date of purchase (Record available from January 2019 to March 2019).

Time: Purchase time (10am to 9pm).

Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet).

COGS: Cost of goods sold.

Gross margin percentage: Gross margin percentage.

Gross income: Gross income.

### Tools

I analyzed a dataset of 1000 records using Python, leveraging libraries such as pandas for data manipulation, NumPy for statistical insights, and seaborn and matplotlib for data visualization. This approach allowed me to interpret and communicate insights effectively through visual representations.




### Data Cleaning/Preparing
In the initial data preparation, I performed the following tasks below:


1. Data loading and inspection.
2. Identify and handling for missing values.
3. Checking for duplicate values.
4. Standardizing datatypes
5. Visualized column quantity with boxplot to check if there were outliers across the dataset.


### Exploration Data Analysis

EDA involved exploring the supermarket dataset to answer key questions such as:
1.	What was the distribution of sales across different branches?
2.	How does customer type (member/normal) sales revenue varies across the dataset?
3.	What was the average gross income for each product line?
4.	What month has the best revenue income?
5.	Find payment type with the most revenue.
6.	Find the correlation relationship between cogs, gross income, Rating, Unit price, Quantity and Tax 5%
7.	What was the percentage gender demographic in the dataset?
8.	What was the average rating for each product line?
9.	What city has the best order quantity?
10.	Which product lines have the highest and lowest percentage sales volumes?
11.	How does weekly sales vary across the dataframe?



### Results/Findings:


1.	Branches "C" and "B" tend to generate high and low distribution sales of $110,568.71 and $106,197.67 across different branches.
2.	Member and Normal payment types generate $164,223.44 and $158,743.40 respectively.
3.	Home and lifestyle tend to have the highest average income of $16.03, while fashion and accessories tend to have the lowest average income.
4.	January tends to generate the best revenue income of $116,291.87 compared to other months.
5.	Cash payment type tends to generate the most revenue of $112,206.57.
6.	"COGS" and "gross income" have a perfect positive correlation of 1.0, indicating they move together perfectly.
7.	"Rating" has a weak negative correlation with "COGS" and "gross income" (-0.03), suggesting that as "Rating" decreases slightly, "COGS" and "gross income" may also decrease slightly.
8.	"Unit price" has a moderately positive correlation with "COGS" and "gross income" (0.63), indicating that as the unit price increases, both "COGS" and "gross income" tend to increase.
9.	"Quantity" has a strong positive correlation with "COGS" and "gross income" (0.70), indicating that as the quantity sold increases, both "COGS" and "gross income" tend to increase.
10.	"Tax 5%" has a perfect positive correlation with "COGS" and "gross income" (1.00), suggesting they move together perfectly, possibly implying that the tax is directly proportional to both "COGS" 
     and "gross income".
11.	There was a high percentage of 50.10% female and 49.90% male across the dataset.
12.	Food beverage and home lifestyle tend to have the highest and lowest average ratings of 7.11 and 6.84 respectively.
13.	Yangon city tends to have the highest order quantity.
14.	Product lines with the highest and lowest percentages are food and beverages and health and beauty, with 17.38% and 15.23% respectively.



### Recommendations:

1.	Branch Performance Analysis: Identifying what makes Branch "C" successful and implementing similar strategies in Branch "B" could help improve its performance.
2.	Payment Type Analysis: Since member payment types generate higher revenue compared to normal payment types, efforts should be made to encourage more customers to become members or to promote member-exclusive offers to increase revenue.
3.	Product Category Analysis: Home and lifestyle products seem to be performing well compared to fashion and accessories. This suggests a potential opportunity to optimize the product mix or marketing strategies for fashion and accessories to increase sales and average income.
4.	Monthly Revenue Analysis: January is identified as the month generating the best revenue income. Understanding the factors contributing to this peak performance, such as seasonal trends or promotional activities, can help in planning future marketing campaigns and sales strategies.
5.	Payment Method Impact: Cash payment type generates the most revenue, indicating that offering discounts or incentives for cash payments could be beneficial. However, exploring reasons behind this preference and ensuring convenient payment options for all customers is essential.
6.	Correlation Analysis: Understanding the correlations between variables like "cogs," "gross income," and others could help in predicting and managing financial performance. Monitoring these correlations over time could provide insights into changing business dynamics.
7.	Gender Demographics: The nearly equal distribution of male and female customers suggests that marketing strategies should cater to both demographics equally, ensuring inclusivity and broad appeal in advertising and product offerings.
8.	Product Rating Analysis: Analyzing product ratings across different categories could provide insights into customer preferences and satisfaction levels. Improving the quality or variety of products with lower ratings could enhance overall customer experience and loyalty.
9.	Location-Based Analysis: Yangon city stands out for having the highest order quantity. Further investigation into the reasons behind this trend could uncover opportunities for targeted marketing or expansion strategies in similar locations.
10.	Product Line Performance: Understanding the performance of different product lines, such as food and beverages versus health and beauty, could help in optimizing inventory management, marketing efforts, and overall business focus. Identifying the reasons behind the success of certain product lines could inform strategic decision-making.







