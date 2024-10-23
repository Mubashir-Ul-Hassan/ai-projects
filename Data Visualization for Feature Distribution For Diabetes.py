# visualization.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('data/diabetes.csv')

# Create a new column for diabetes status (1 = Diabetic, 0 = Non-Diabetic)
data['Diabetes_Status'] = data['Outcome'].apply(lambda x: 'Diabetic' if x == 1 else 'Non-Diabetic')

# Set up the plotting style
sns.set(style="whitegrid")

# Plot the distribution of glucose levels
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='Glucose', hue='Diabetes_Status', multiple='stack', kde=True)
plt.title('Glucose Level Distribution for Diabetic vs Non-Diabetic Individuals')
plt.xlabel('Glucose Level')
plt.ylabel('Frequency')
plt.show()

# Plot the distribution of BMI
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='BMI', hue='Diabetes_Status', multiple='stack', kde=True)
plt.title('BMI Distribution for Diabetic vs Non-Diabetic Individuals')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()
