import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("studentimformation.csv")  # Replace with the correct file path

# Filter data for a specific student (e.g., "MCE24CS407D08")
student_data = data[data['RegNo'] == 'MCE24CS406'].iloc[:, 2:]  # Adjust column slicing if needed

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Student Information', fontsize=16)

# Bar plot
student_data.T.plot(kind='bar', legend=False, ax=axes[0], color='blue')
axes[0].set_title('MCE24CS406', fontsize=14, color='red')
axes[0].set_xlabel('Courses')
axes[0].set_ylabel('Marks')

# Line plot
student_data.T.plot(kind='line', marker='o', legend=False, ax=axes[1], color='red')
axes[1].set_title('MCE24CS406', fontsize=14, color='red')
axes[1].set_xlabel('Courses')
axes[1].set_ylabel('Marks')

# Show the plots
plt.tight_layout()
plt.show()

