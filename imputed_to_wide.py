import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('/home/russell/PycharmProjects/hackathon_day_!/data/imputed_data.csv')
wide_data = pd.DataFrame()
wide_data['Area Name'] = df['Area Name'].unique()

for indicator in df['Indicator ID'].unique():
    indicator_df = df[df['Indicator ID'] == indicator]
    k, p = stats.normaltest(pd.to_numeric(indicator_df['Value']))
    print(k, p)
    if p > 0.05:
        indicator_df['log_transformed'] = indicator_df['Value'].transform(lambda x: np.log(x))
        k, p = stats.normaltest(indicator_df['log_transformed'])
        if p > 0.05:
            continue
        mapping = dict(indicator_df[['Area Name', 'log_transformed']].values)
        wide_data[indicator] = wide_data['Area Name'].map(mapping)
    else:
        mapping = dict(indicator_df[['Area Name', 'Value']].values)
        wide_data[indicator] = wide_data['Area Name'].map(mapping)

print(wide_data.head().to_string())

wide_data.to_csv('wide_data.csv')