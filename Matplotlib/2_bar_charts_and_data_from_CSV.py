# Youtube: https://www.youtube.com/watch?v=nKxLfUrkLE8&list=PLICW5UpCwEj0GIC7WLVHf3SnZKmAchsUy&index=2

import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

## (Horizontal) Bar chart

plt.style.use("fivethirtyeight")    # styles often have certain attributes already build in, like "grid", so it isn't needed to call them seperately 

data = pd.read_csv("1_data.csv")
# print(data)

id = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

print(language_counter)

languages = []
language_count = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    language_count.append(item[1])

languages.reverse()         # reverse order so the most popular language is at the top of the plot
language_count.reverse()

plt.barh(languages, language_count)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People")

plt.tight_layout()

plt.show()


## (Vertical) Bar chart - Multiple bars per age

ages_x = [25, 26, 27, 28, 29, 30 , 31, 32, 33, 34, 35] 

x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73852]

plt.bar(x_indexes - width, dev_y, width=width, color="#444444", linestyle="--", label="All Devs") 

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y, width=width, color="#5a7d9a", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746 ,74583]

plt.bar(x_indexes + width, js_dev_y, width=width, color="#adad3b", label="JavaScript") 

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

plt.xticks(ticks=x_indexes, labels=ages_x)  # first argument = position of ticks, second argument = names of ticks on plot

plt.legend()
plt.tight_layout()

#plt.savefig("plot.png")

plt.show()