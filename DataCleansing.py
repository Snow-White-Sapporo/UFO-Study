# Import Libraries
import pandas as pd
import numpy as np
import re

# Load Data
data= pd.read_csv("scrubbed.csv")
data.head()
data.info()
data.describe()
data.columns

# Data Preparation

# Trim column names
data.rename(columns={'longitude ': 'longitude'}, inplace = True)
# Check duplicated rows
data[data.duplicated()]
# Check null values
data.isnull().sum()
# Check the percentages of NAN values
round(data.isna().mean() * 100, 2)
# Delete the NAN value rows
data.dropna(subset=['state', 'country', 'shape'], inplace=True)
data.reset_index(drop=True, inplace=True)
# Fill comments column                
data["comments"].fillna("no comment", inplace=True)
# latitude/ longitude to be float
data['latitude'] = pd.to_numeric(data['latitude'], errors = 'coerce')
data['longitude'] = pd.to_numeric(data['longitude'], errors = 'coerce')
# latitude/ longitude 0.0 replaced with NaN
data.loc[:, 'latitude'].replace({0.0: np.nan}, inplace=True)
data.loc[:, 'longitude'].replace({0.0: np.nan}, inplace=True)
# datetime Fix "24:xx"
def custom_to_datetime(date):
    for i in range(len(date)):
        if date[i][11:13] == '24':
            date[i] = str(date[i][:11]) + '23:59'
        elif date[i][10:12] == '24':
            date[i] = str(date[i][:10]) + '23:59'
        elif date[i][9:11] == '24':
            date[i] = str(date[i][:9]) + '23:59'
    return pd.to_datetime(date)

data['datetime'] = custom_to_datetime(data['datetime'])
data['date posted'] = pd.to_datetime(data['date posted'])

# Split datetime into year, month, day, and hour
data["year"] = pd.DatetimeIndex(data['datetime']).year
data["month"] = pd.DatetimeIndex(data['datetime']).month
data["day"] = pd.DatetimeIndex(data['datetime']).day
data["hour"] = pd.DatetimeIndex(data['datetime']).hour
# Delete "duration (hours/min)" after check
data[["duration (seconds)","duration (hours/min)"]].sample(5)
data.drop(columns="duration (hours/min)", axis=1,inplace=True)
# Convert the type of duration columns from object to float
data["duration (seconds)"] = data["duration (seconds)"].astype(float)

# Trim "comments" column
def remove_punctuations(text):
    return re.sub("[!#$%&'("")’“”*+,-./:;<=>?@[\]^_`{|}~©]+","",text)
def remove_spaces(text):
    return re.sub("\s[ ]+","",text)
def to_lower(text):
    text = text.lower()
    return text
comments = data["comments"]
for i in range(len(comments)):
    comments[i] = remove_punctuations(comments[i])
    comments[i] = remove_spaces(comments[i])
    comments[i] = to_lower(comments[i])
comments = [comment for comment in data["comments"]]
text = " ".join(comments)

# Create cleansed csv file
data.to_csv("cleaned_data.csv", index=False)



