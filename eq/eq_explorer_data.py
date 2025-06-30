from pathlib import Path
import json
import plotly.express as px

path = Path(r'eq\eq_data\eq_data_30_day_m1.geojson')

lines = path.read_text(encoding='utf-8')

py_obj = json.loads(lines)



print(len(py_obj['features']))
eq_dicts = py_obj['features']
mags = []
lons = []
lats = []
names = []


for e in eq_dicts:
    mag = e['properties']['mag']
    lon = e['geometry']['coordinates'][0]
    lat = e['geometry']['coordinates'][1]
    name = e['properties']['title']
    
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    names.append(name)
    
print(mags)
    
# cwd = Path.cwd()
# path_nice = Path(r'eq\eq_data') / Path( 'nice_json.json')

# json_obj = json.dumps(py_obj, indent=4)
# path_nice.write_text(json_obj)


title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, hover_name=names, title=title,
                    color=mags,
                    color_continuous_scale='Viridis',
                    labels={'color': 'Magnitude'},
                    projection='natural earth'
                    )
fig.show()