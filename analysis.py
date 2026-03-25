import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset: energy consumption (example)
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Energy_Consumption": [120, 150, 130, 170, 160]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display basic statistics
print("Dataset Summary:")
print(df.describe())

# Plot the data
plt.figure()
plt.plot(df["Day"], df["Energy_Consumption"], marker='o')
plt.title("Energy Consumption Analysis")
plt.xlabel("Day")
plt.ylabel("Energy Consumption")
plt.grid()

# Show plot
plt.show()
