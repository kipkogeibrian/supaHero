                         code 
# ======================
# TASK 1: LOAD AND EXPLORE
# ======================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset with error handling
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    # Display first 5 rows
    print("=== First 5 Rows ===")
    display(df.head())
    
    # Check structure and missing values
    print("\n=== Dataset Info ===")
    print(df.info())
    
    print("\n=== Missing Values ===")
    print(df.isnull().sum())
    
    # Data cleaning (though Iris dataset is clean)
    df_clean = df.copy()  # No cleaning needed for Iris
    
except Exception as e:
    print(f"Error loading data: {e}")

# ======================
# TASK 2: BASIC ANALYSIS
# ======================
# Descriptive statistics
print("\n=== Descriptive Statistics ===")
display(df_clean.describe())

# Group by species and calculate means
print("\n=== Mean Measurements by Species ===")
species_means = df_clean.groupby('species').mean()
display(species_means)

# Key findings
print("\n=== Key Findings ===")
print("1. Setosa has the smallest petal dimensions")
print("2. Virginica has the largest measurements overall")
print("3. Sepal widths are most similar across species")

# ======================
# TASK 3: VISUALIZATION
# ======================
plt.figure(figsize=(15, 10))
sns.set_style("whitegrid")

# 1. Line Chart (using index as pseudo-time)
plt.subplot(2, 2, 1)
df_clean['sepal length (cm)'].plot(kind='line', color='purple')
plt.title('Sepal Length Trend (by Index)')
plt.ylabel('Length (cm)')

# 2. Bar Chart
plt.subplot(2, 2, 2)
species_means['petal length (cm)'].plot(kind='bar', 
                                       color=['red', 'green', 'blue'])
plt.title('Average Petal Length by Species')
plt.ylabel('Length (cm)')
plt.xticks(rotation=0)

# 3. Histogram
plt.subplot(2, 2, 3)
df_clean['sepal width (cm)'].hist(bins=15, color='orange')
plt.title('Distribution of Sepal Width')
plt.xlabel('Width (cm)')
plt.ylabel('Frequency')

# 4. Scatter Plot
plt.subplot(2, 2, 4)
sns.scatterplot(data=df_clean, 
               x='sepal length (cm)', 
               y='petal length (cm)', 
               hue='species',
               palette=['red', 'green', 'blue'])
plt.title('Sepal vs Petal Length')
plt.legend(title='Species')

plt.tight_layout()
plt.savefig('iris_analysis.png')  # Save for submission
plt.show()


                         DISPLAY 


== First 5 Rows ===
sepal length (cm)	sepal width (cm)	petal length (cm)	petal width (cm)	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa

=== Dataset Info ===
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
 4   species            150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None

=== Missing Values ===
sepal length (cm)    0
sepal width (cm)     0
petal length (cm)    0
petal width (cm)     0
species              0
dtype: int64

=== Descriptive Statistics ===
sepal length (cm)	sepal width (cm)	petal length (cm)	petal width (cm)
count	150.000000	150.000000	150.000000	150.000000
mean	5.843333	3.057333	3.758000	1.199333
std	0.828066	0.435866	1.765298	0.762238
min	4.300000	2.000000	1.000000	0.100000
25%	5.100000	2.800000	1.600000	0.300000
50%	5.800000	3.000000	4.350000	1.300000
75%	6.400000	3.300000	5.100000	1.800000
max	7.900000	4.400000	6.900000	2.500000

=== Mean Measurements by Species ===
sepal length (cm)	sepal width (cm)	petal length (cm)	petal width (cm)
species				
setosa	5.006	3.428	1.462	0.246
versicolor	5.936	2.770	4.260	1.326
virginica	6.588	2.974	5.552	2.026

=== Key Findings ===
1. Setosa has the smallest petal dimensions
2. Virginica has the largest measurements overall
3. Sepal widths are most similar across species



           SCREENSHOT OF CHARTS
The link to the screenshot: blob:https://imgur.com/101d1c91-87f3-481f-9022-ac45ca7bbadf
