import urllib
import json
import urllib.request
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


def get_data():
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    with urllib.request.urlopen(url) as f:
        data = f.read()
    return data

def main():

    json_data = get_data()
    json_data = json.loads(json_data)
    all_eq_data = json_data['features']
    
    mags, lons, lats,hover_texts = [], [], [], []
    
    mags = [(eq_dict['properties']['mag']) for eq_dict in all_eq_data]
    lons = [(eq_dict['geometry']['coordinates'][0]) for eq_dict in all_eq_data]
    lats = [(eq_dict['geometry']['coordinates'][1]) for eq_dict in all_eq_data]
    hover_texts = [(eq_dict['properties']['title']) for eq_dict in all_eq_data]

    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size':[5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
            }
        }]
    my_layout = Layout(title= json_data['metadata']['title'])
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquakes.html')
    
    
    
    
if __name__=="__main__":
    main()
