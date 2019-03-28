import pandas as pd
import numpy as np


def create_z_score(series):
    try:
        list = []
        series[series == -np.inf] = 0
        for value in series:
            list.append((value - np.mean(series)) / np.std(series))
        return list
    except TypeError:
        return series


df = pd.read_csv('/home/russell/PycharmProjects/hackathon_day_!/data/wide_data.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df_z = df.apply(lambda x: create_z_score(x))
df_z.set_index('Area Name', inplace=True)
print(df_z)
df_z.to_csv('/home/russell/PycharmProjects/hackathon_day_!/data/z_scores.csv')



