import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('10_data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

axes[1].plot(ages, py_salaries, label='Python')
axes[1].plot(ages, js_salaries, label='JavaScript')

axes[0].legend()
axes[0].set_title('Median Salary (USD) by Age')
axes[0].set_ylabel('Median Salary (USD)')

axes[1].legend()
axes[1].set_xlabel('Ages')
axes[1].set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

#fig1.savefig('fig1.png')
#fig2.savefig('fig2.png')