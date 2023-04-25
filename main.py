import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math

flight = pd.read_csv('flight.csv')
# print(flight.head())
'''
The mean and median price of a ticket + graph
'''
# print(np.mean(flight.coach_price))
# print(np.median(flight.coach_price))
# sns.histplot(flight.coach_price)
# plt.show()
# plt.clf()
'''
8-hour flights tickets + graph
'''
# print(np.mean(flight.coach_price[flight.hours == 8]))
# print(np.median(flight.coach_price[flight.hours == 8]))
# sns.histplot(flight.coach_price[flight.hours == 8])
# plt.show()
'''
Plotting the delays between 1 and 50 minutes
'''
# sns.histplot(flight.delay[(flight.delay <= 50) & (flight.delay > 0)])
# plt.show()
'''
The relationship between coach and first-class prices. 10percent sample taken
'''
# perc = 0.1
# flight_sub = flight.sample(n=int(flight.shape[0] * perc))
# sns.lmplot(x="coach_price",
#            y="firstclass_price",
#            data=flight_sub,
#            line_kws={'color': 'black'},
#            lowess=True)
# plt.show()
'''
The relationship between coach prices and inflight features
'''
# Inflight Meals
# sns.histplot(flight, x="coach_price", hue=flight.inflight_meal)
# plt.show()

# Inflight Entertainment
# sns.histplot(flight, x="coach_price", hue=flight.inflight_entertainment)
# plt.show()

# Inflight WiFi
# sns.histplot(flight, x="coach_price", hue=flight.inflight_wifi)
# plt.show()
'''
The relationship between the number of passengers and the length of flight
'''
perc = 0.1
flight_sub = flight.sample(n=int(flight.shape[0] * perc))
# sns.lmplot(x="hours",
#            y="passengers",
#            data=flight_sub,
#            x_jitter=0.25,
#            scatter_kws={
#              "s": 5,
#              "alpha": 0.2
#            },
#            fit_reg=False)
# plt.show()
'''
The relationship between coach and first-class prices on weekends compared to weekdays
'''
# sns.lmplot(x='coach_price',
#            y='firstclass_price',
#            hue='weekend',
#            data=flight_sub,
#            fit_reg=False)
# plt.show()
'''
How do coach prices differ for redeyes and non-redeyes on each day of the week?
'''
sns.boxplot(x='day_of_week', y='coach_price', hue='redeye', data=flight)
plt.show()