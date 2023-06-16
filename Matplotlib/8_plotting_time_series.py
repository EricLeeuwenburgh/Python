# Youtube: https://www.youtube.com/watch?v=_LWjaAiKaf8&list=PLICW5UpCwEj0GIC7WLVHf3SnZKmAchsUy&index=8

import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

## Time Series plots - Keeping track of certain values over time

plt.style.use('seaborn')

data = pd.read_csv('8_data.csv')        # data = Bitcoin price over a certain period

data['Date'] = pd.to_datetime(data['Date'])     # convert string dates to type pandas "datetime"
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()


##

# plt.style.use('seaborn')

# dates = [                               # 7 random dates
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 6, 5, 7]

# plt.plot_date(dates, y, linestyle="solid")

# plt.gcf().autofmt_xdate()       # automatically fixes the date representation on the x-axis

# date_format = mpl_dates.DateFormatter("%b, %d, %Y")     # automatically formats the date representation (Month, day, Year)
# plt.gca().xaxis.set_major_formatter(date_format)

# plt.tight_layout()

# plt.show()