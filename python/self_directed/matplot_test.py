import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv("data/UNRATE.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])

plt.plot(unrate["DATE"].iloc[:12],unrate["UNRATE"].iloc[:12])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()