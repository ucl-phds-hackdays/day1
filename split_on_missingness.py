import pandas as pd

df = pd.read_csv('/home/russell/PycharmProjects/hackathon_day_!/data/social_determinatants_most_recent.csv')

indicators = df['Indicator ID'].unique()
missing_data = pd.DataFrame()
imputed_data = pd.DataFrame()


for indicator in indicators:
    indicator_df = df[df['Indicator ID'] == indicator]
    if indicator_df['Value'].isna().sum()/len(indicator_df) > 0.1:
        missing_data = missing_data.append(indicator_df)
    else:
        median = indicator_df['Value'].median()
        indicator_df.fillna(median, inplace=True)
        imputed_data = imputed_data.append(indicator_df)


print(missing_data.head(), imputed_data.head())

missing_data.to_csv('/home/russell/PycharmProjects/hackathon_day_!/data/missing_data.csv')
imputed_data.to_csv('/home/russell/PycharmProjects/hackathon_day_!/data/imputed_data.csv')