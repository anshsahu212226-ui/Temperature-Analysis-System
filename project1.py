import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = []

print("Enter temperature for 7 days:\n")

# Input from user
for day in days:
    t = float(input(f"{day}: "))
    temps.append(t)

# Analysis
avg = sum(temps) / len(temps)
max_temp = max(temps)
min_temp = min(temps)

print("\n------ Temperature Report ------")
print("Average Temperature:", round(avg, 2))
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)

# Trend Detection
if temps[-1] > temps[0]:
    print("Trend: Increasing 📈")
elif temps[-1] < temps[0]:
    print("Trend: Decreasing 📉")
else:
    print("Trend: Stable ➖")

# Max/Min day
max_day = days[temps.index(max_temp)]
min_day = days[temps.index(min_temp)]

print("Hottest Day:", max_day)
print("Coldest Day:", min_day)

# Graph
plt.figure(figsize=(8,5))

# Line graph
plt.plot(days, temps, marker='o', label="Temperature")

# Bar graph
plt.bar(days, temps, alpha=0.3)

# Highlight max/min
plt.scatter(max_day, max_temp, label="Max Temp", s=100)
plt.scatter(min_day, min_temp, label="Min Temp", s=100)

plt.title("Weekly Temperature Analysis")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid()

plt.show()