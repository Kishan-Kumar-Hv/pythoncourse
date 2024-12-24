import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('employe.csv')  # Replace with your actual file path

# Create a figure with subplots
plt.figure(figsize=(14, 7))

# Boxplot for salary distribution by department
plt.subplot(1, 2, 1)
sns.boxplot(x='Department', y='Salary', data=df)
plt.title('Boxplot of Salaries by Department')
plt.xlabel('Department')
plt.ylabel('Salary')

# Violin plot for salary distribution by department
plt.subplot(1, 2, 2)
sns.violinplot(x='Department', y='Salary', data=df)
plt.title('Violin Plot of Salaries by Department')
plt.xlabel('Department')
plt.ylabel('Salary')

# Display the plots
plt.tight_layout()
plt.show()



