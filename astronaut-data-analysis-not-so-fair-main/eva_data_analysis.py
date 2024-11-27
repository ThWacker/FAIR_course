import json
import csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# https://data.nasa.gov/resource/eva.json (with modifications)
input_json = open('eva-data.json', 'r')
spacewalks_csv = open('eva-data.csv','w')
spacewalks_plot = 'myplot.png'

fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

data=[]

eva_df= pd.read_json(input_json, convert_dates=['date'])
eva_df['eva']=eva_df['eva'].astype(float)
eva_df.dropna(axis=0, inplace=True)
eva_df.sort_values('date', inplace=True)

eva_df.to_csv(spacewalks_csv, index=False)

eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(spacewalks_plot)
plt.show()

