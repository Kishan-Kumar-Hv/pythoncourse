import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("stocks.csv")  # Replace with your CSV file path
sns.lineplot(data=df, x="Date", y="Open", hue="Symbol", style="Symbol", markers=True)
plt.xlabel("Date")
plt.ylabel("Opening Price (INR)")
plt.title("Adani Stocks Opening Prices Over Time")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


