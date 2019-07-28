import folium
import pandas as p

df = p.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# map = folium.Map(location=[38.58, -99.89], zoom_start = 6, tiles="Mapbox Bright")
map = folium.Map(location=[38.58, -99.89], zoom_start = 6)

#Feature group: add multiple features to a feature group
fgv = folium.FeatureGroup(name="Volcanoes")
#define a single point
#map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
#define as a feature group
#fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
# for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
html = """<h4>Volcano information:</h4>
Height: %s m
"""
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
# fg.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read())))
fgp.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()), 
#set yellow to fill color, if properties "pop2005" is less than 1000000, from json file
style_function=lambda x : {'fillColor': 'green' if x['properties']['POP2005']< 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) 

map.add_child(fgv)
map.add_child(fgp)
#implement layer child
map.add_child(folium.LayerControl())

map.save("Map1.html")