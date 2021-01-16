import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns

# Read the csv data
df = pd.read_csv('./src/messibetis.csv')

# Convert the data to match mplsoccer statsbomb pitch.
# To see how to create the pitch, watch:
# https://www.youtube.com/watch?v=55k1mCRyd2k
df['x'] = df['x'] * 1.2
df['y'] = df['y'] * 0.8
df['endX'] = df['endX'] * 1.2
df['endY'] = df['endY'] * 0.8

#
fig, ax = plt.subplots(figsize=(13.5, 8))
fig.set_facecolor('white')

# Create the pitch
pitch = Pitch(pitch_type='statsbomb', orientation='horizontal', pitch_color='grass',
              line_color='white', stripe=True, figsize=(13, 8), constrained_layout=False, tight_layout=True)

# Draw the pitch on the ax figure as well as invert the
# axis for the specific pitch
pitch.draw(ax=ax)
plt.gca().invert_yaxis()

# Create the heatmap
kde = sns.kdeplot(x=df['x'], y=df['y'], shade=True,
                  thresh=0.06, alpha=0.7, n_levels=100, fill=True, cmap='YlOrRd', bw_method=0.45)


plt.xlim(0, 120)
plt.ylim(0, 80)

plt.title('Messi Passes Heatmap vs Real Betis', color='black', size=20)
plt.savefig('messi_heatmap_betis.png')
