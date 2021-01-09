import urllib
import urllib.request
import json
import matplotlib.pyplot as plt
import seaborn
import requests

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson'
with urllib.request.urlopen(url) as f:
    data = f.read()
all_eq_dict = json.loads(data)

all_feature_dict = all_eq_dict['features']

mags, lons, lats, hover_text = [],[],[],[]
[mags.append(eq_dict['properties']['mag']) for eq_dict in all_feature_dict]
[lons.append(eq_dict['geometry']['coordinates'][0]) for eq_dict in all_feature_dict]
[lats.append(eq_dict['geometry']['coordinates'][1]) for eq_dict in all_feature_dict]
[hover_text.append(eq_dict['properties']['title']) for eq_dict in all_feature_dict]

whole_num_mag = []
[whole_num_mag.append(mag//1) for mag in mags]

bins= [0,1,2,3,4,5,6,7,8,9,10]
# plt.style('seaborn')
plt.hist(mags, bins=bins)
plt.show()
