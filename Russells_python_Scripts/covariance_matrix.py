import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/russell/PycharmProjects/hackathon_day_!/data/z_scores.csv')

df_cov = df.cov()
plt.matshow(df.cov())
plt.savefig('/home/russell/PycharmProjects/hackathon_day_!/data/corr_matrix.png')
plt.show()
df_cov.to_csv('/home/russell/PycharmProjects/hackathon_day_!/data/covariate_matrix.csv')