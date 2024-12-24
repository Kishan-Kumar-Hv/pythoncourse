import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("studentmarks.csv")
df["Student"] = df["Student"].fillna("Unknown").astype(str)
plt.scatter(df["Student"], df["Math"], label="Math Scores", color="blue")
plt.scatter(df["Student"], df["Science"], label="Science Scores", color="green")
plt.title("Comparison of Math and Science Scores")
plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.legend()
plt.grid()
plt.show()
