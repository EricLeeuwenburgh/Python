# Youtube: https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PLICW5UpCwEj0GIC7WLVHf3SnZKmAchsUy&index=1&t=399s

from matplotlib import pyplot as plt

# Simple line plot
# print(plt.style.available)

plt.style.use("ggplot")    # "fivethirtyeight"      # styles often have certain attributes already build in, like "grid", so it isn't needed to call them seperately 

ages_x = [25, 26, 27, 28, 29, 30 , 31, 32, 33, 34, 35] 

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, label="Python")          # color="#5a7d9a", linewidth=3

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746 ,74583]

plt.plot(ages_x, js_dev_y, label="JavaScript")      # color="#adad3b", linewidth=3

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73852]

plt.plot(ages_x, dev_y, color="#444444", linestyle="--", label="All Devs") 

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

plt.legend()
plt.tight_layout()

#plt.savefig("plot.png")

plt.show()