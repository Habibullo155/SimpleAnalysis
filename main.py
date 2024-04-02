import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating random data
data = np.random.randint(-10000, 10000, 1000)
series = pd.Series(data)

# Standard Numerical Specifications
min_value = series.min()
num_duplicates = series.duplicated().sum()
max_value = series.max()
sum_values = series.sum()
std_dev = series.std()

print("min value:", min_value)
print("Number of duplicate values:", num_duplicates)
print("max value:", max_value)
print("Sum of numbers:", sum_values)
print("Standard deviation:", std_dev)

# Data visualization
plt.figure(figsize=(12, 6))

# Line graph
plt.subplot(121)
plt.plot(series)
plt.title('Line graph of data')
plt.xlabel('index')
plt.ylabel('Value')

# Histogram
plt.subplot(122)
rounded_series = series.round(-2)  # Round values to the nearest hundred
rounded_series.hist()
plt.title('Histogram of data (rounded to the nearest hundred)')
plt.xlabel('value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# creating DataFrame
df = pd.DataFrame(series, columns=['Original'])
df['Sorted_Ascending'] = df['Original'].sort_values(ascending=True).values
df['Sorted_Descending'] = df['Original'].sort_values(ascending=False).values

# Data visualization
plt.figure(figsize=(8, 5))
plt.plot(df['Sorted_Ascending'], label='Ascending')
plt.plot(df['Sorted_Descending'], label='Descending')
plt.title('Sorted values')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend()

plt.show()
