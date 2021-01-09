import urllib
import urllib.request
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

def get_data(url):

    with urllib.request.urlopen(url) as f:
        data = f.read()
    json_data_to_dict = json.loads(data)
    return json_data_to_dict

def main():

    all_data = get_data(url)
    all_eq_data = all_data['features']

    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson'

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
            'size': [5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
            }
        }]
    my_layout = Layout(title=all_data['metadata']['title'])
    fig= {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquakes_7day.html')

if __name__=="__main__":
    main()
