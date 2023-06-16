# Youtube: https://www.youtube.com/watch?v=XDv6T4a0RNc&list=PLICW5UpCwEj0GIC7WLVHf3SnZKmAchsUy&index=6

import pandas as pd
from matplotlib import pyplot as plt

## Histograms - Best used to see how values are distributed between certain "bins"

plt.style.use('fivethirtyeight')

data = pd.read_csv('6_data.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
#plt.savefig('figures/plot.png')

plt.show()


# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# bins = [10, 20, 30, 40, 50, 60]

# plt.hist(ages, bins=bins, edgecolor='black')

# plt.title('Ages of Respondents')
# plt.xlabel('Ages')
# plt.ylabel('Total Respondents')

# plt.tight_layout()

# plt.show()