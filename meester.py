import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
print("Enter the name of a search term you want to compare to Leighton Meester and Britney Spears:")
trend = str(input())
while (trend == 'Leighton Meester' or trend == 'Britney Spears'):
    print("You can't pick that! Try again:")
    trend = str(input())

kw_list = ['Britney Spears', 'Leighton Meester', trend]

pytrends.build_payload(kw_list, cat=0, timeframe='all', geo='', gprop='')

data = pytrends.interest_over_time()

data=data[['Britney Spears', 'Leighton Meester', trend]].cumsum()

brit_avg = data.iloc[-1, 0]
leight_avg = data.iloc[-1, 1]
trend_avg = data.iloc[-1, 2]

if (trend_avg < 1):
    print("Your search term didn't have enough searches to build a dataset :(")
    exit()

trend_brit = int((round(trend_avg / brit_avg, 2) - 1) * 100)
brit_trend = int((round(brit_avg / trend_avg, 2) - 1) * 100)

trend_leight = int((round(trend_avg / leight_avg, 2) - 1) * 100)
leight_trend = int((round(leight_avg / trend_avg, 2) - 1) * 100)


if (trend_avg > brit_avg):
    print(trend + " is " + str(trend_brit) + "% more popular than Britney Spears since 2004.")

elif (trend_avg == brit_avg):
    print(trend + " is just as popular as Britney Spears since 2004.")

elif (trend_avg < brit_avg):
    print("Britney Spears is " + str(brit_trend) + "% more popular than " + trend + " since 2004.")

if (trend_avg > leight_avg):
    print(trend + " is " + str(trend_leight) + "% more popular than Leighton Meester since 2004.")

elif (trend_avg == leight_avg):
    print(trend + " is just as popular as Leighton Meester since 2004.")

elif (trend_avg < leight_avg):
    print("Leighton Meester is " + str(leight_trend) + "% more popular than " + trend + " since 2004.")

