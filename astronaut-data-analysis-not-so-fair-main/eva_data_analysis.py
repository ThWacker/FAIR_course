import matplotlib.pyplot as plt
import pandas as pd

# https://data.nasa.gov/resource/eva.json (with modifications)
input_json = open('eva-data.json', 'r')
spacewalks_csv = open('eva-data.csv','w')
spacewalks_plot = 'myplot.png'


print("--START--")
print(f"Reading JSON file {input_json}")

# Read the data from the JSON using pandas
eva_df= pd.read_json(input_json, convert_dates=['date'])
eva_df['eva']=eva_df['eva'].astype(float)
#Clean the data by removing incomplete rows and sort it by date
eva_df.dropna(axis=0, inplace=True)
eva_df.sort_values('date', inplace=True)

print(f"Saving to CSV file {spacewalks_csv}")
#Save dataframe to csv for later analysis
eva_df.to_csv(spacewalks_csv, index=False)

print(f"Plotting cumulative spacewalk duration and save to {spacewalks_plot}")

# Get the duration in hours
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
#add cumulative time column 
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# plotting 
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(spacewalks_plot)
plt.show()

print("--END--")