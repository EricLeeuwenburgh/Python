# Youtube: https://www.youtube.com/watch?v=x0Uguu7gqgk&list=PLICW5UpCwEj0GIC7WLVHf3SnZKmAchsUy&index=5

import pandas as pd
from matplotlib import pyplot as plt

## Fill betweens - Best used to see where certain values actually are

data = pd.read_csv('5_data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries, 
                 where=(py_salaries > dev_salaries),                    # where = define starting point for the fill
                 interpolate=True, alpha=0.25, label="Above Avg")       # interpolate = smoothens out the fill by filling up gaps
                                                                        # alpha = set transpancy
plt.fill_between(ages, py_salaries, dev_salaries, 
                 where=(py_salaries <= dev_salaries),  
                 interpolate=True, color="red", alpha=0.25, label="Below Avg")

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
#plt.savefig('figures/plot.png')

plt.show()