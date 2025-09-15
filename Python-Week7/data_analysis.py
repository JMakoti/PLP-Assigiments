# Task 1: Load and Explore the Dataset

# Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
# Load the dataset using pandas.
# Display the first few rows of the dataset using .head() to inspect the data.
# Explore the structure of the dataset by checking the data types and any missing values.
# Clean the dataset by either filling or dropping any missing values.

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Iris.csv')

# Display first few rows
print("First 10 rows of the dataset:")
print(df.head(10))
# Output
# First 10 rows of the dataset:
#    Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
# 0   1            5.1           3.5            1.4           0.2  Iris-setosa
# 1   2            4.9           3.0            1.4           0.2  Iris-setosa
# 2   3            4.7           3.2            1.3           0.2  Iris-setosa
# 3   4            4.6           3.1            1.5           0.2  Iris-setosa
# 4   5            5.0           3.6            1.4           0.2  Iris-setosa
# 5   6            5.4           3.9            1.7           0.4  Iris-setosa
# 6   7            4.6           3.4            1.4           0.3  Iris-setosa
# 7   8            5.0           3.4            1.5           0.2  Iris-setosa
# 8   9            4.4           2.9            1.4           0.2  Iris-setosa
# 9  10            4.9           3.1            1.5           0.1  Iris-setosa

# Check dataset structure
print("\nDataset Info:")
print(df.info())

# output
# Dataset Info:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 150 entries, 0 to 149
# Data columns (total 6 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   Id             150 non-null    int64  
#  1   SepalLengthCm  150 non-null    float64
#  2   SepalWidthCm   150 non-null    float64
#  3   PetalLengthCm  150 non-null    float64
#  4   PetalWidthCm   150 non-null    float64
#  5   Species        150 non-null    object 

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Output
# Missing values per column:
# Id               0
# SepalLengthCm    0
# SepalWidthCm     0
# PetalLengthCm    0
# PetalWidthCm     0
# Species          0
# dtype: int64

# Cleaning:  Drop rows with missing values
df_dropped = df.dropna()
print("\nDataset after dropping missing values:")
print(df_dropped.head())

# Output
# Dataset after dropping missing values:
#    Id  SepalLengthCm  ...  PetalWidthCm      Species
# 0   1            5.1  ...           0.2  Iris-setosa
# 1   2            4.9  ...           0.2  Iris-setosa
# 2   3            4.7  ...           0.2  Iris-setosa
# 3   4            4.6  ...           0.2  Iris-setosa
# 4   5            5.0  ...           0.2  Iris-setosa

# [5 rows x 6 columns]

# Cleaning: Fill missing numeric values with mean
# df_filled = df.fillna(df.mean(numeric_only=True))
# print("\nDataset after filling missing values with mean:")
# print(df_filled.head())

# Task 2: Basic Data Analysis
# Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
# Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
# Identify any patterns or interesting findings from your analysis.

# Basic statistics of numerical columns
stats = df.describe()
print("Basic Statistics:\n", stats)
# Output
# Basic Statistics:
#                 Id  SepalLengthCm  ...  PetalLengthCm  PetalWidthCm
# count  150.000000     150.000000  ...     150.000000    150.000000
# mean    75.500000       5.843333  ...       3.758667      1.198667
# std     43.445368       0.828066  ...       1.764420      0.763161
# min      1.000000       4.300000  ...       1.000000      0.100000
# 25%     38.250000       5.100000  ...       1.600000      0.300000
# 50%     75.500000       5.800000  ...       4.350000      1.300000
# 75%    112.750000       6.400000  ...       5.100000      1.800000
# max    150.000000       7.900000  ...       6.900000      2.500000

# [8 rows x 5 columns]

# Grouping by a categorical column (e.g., species/region/department)
# Group by Species and calculate mean SepalLengthCm
grouped_means = df.groupby("Species")["SepalLengthCm"].mean()
print("\nMean Sepal Length by Species:\n", grouped_means)
# Output
# Mean Sepal Length by Species:
#  Species
# Iris-setosa        5.006
# Iris-versicolor    5.936
# Iris-virginica     6.588
# Name: SepalLengthCm, dtype: float64


# Task 3: Data Visualization
# Create at least four different types of visualizations:
# Line chart showing trends over time (for example, a time-series of sales data).
# Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
# Histogram of a numerical column to understand its distribution.
# Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
# Customize your plots with titles, labels for axes, and legends where necessary.

# 1. Line Chart (fake time-series: use Id as index to simulate time)
plt.figure(figsize=(8,5))
plt.plot(df["Id"], df["SepalLengthCm"], label="Sepal Length")
plt.xlabel("Id (as time)")
plt.ylabel("Sepal Length (cm)")
plt.title("Line Chart - Sepal Length over Time (Id)")
plt.legend()
plt.savefig("line_chart.png") 
plt.close()


# 2. Bar Chart (Average petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="Species", y="PetalLengthCm", data=df, estimator="mean", palette="Set2")
plt.title("Bar Chart - Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.savefig("bar_chart.png") 
plt.close()


# 3. Histogram (distribution of SepalWidthCm)
plt.figure(figsize=(8,5))
plt.hist(df["SepalWidthCm"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram - Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig("histogram_chart.png") 
plt.close()


# 4. Scatter Plot (Sepal Length vs Petal Length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="SepalLengthCm", y="PetalLengthCm", hue="Species", data=df, palette="Set1")
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.savefig("scatter_plot.png") 
plt.close()



