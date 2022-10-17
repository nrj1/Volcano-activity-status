import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def elev_check(el):
    if el < 1200:
        return "green"
    elif el < 2500:
        return "yellow"
    else:
        return "red"


map = folium.Map(location = [34.052235, -118.243683], tiles = "Stamen Terrain", zoom_start = 8)
fgv = folium.FeatureGroup(name = "Volcanoes")
fgp = folium.FeatureGroup(name = "Population")

for lt,ln,el,nm in zip(lat,lon,elev,name):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], popup = str(nm),radius = 6,
    fill_color =  elev_check(el), color = "grey", fill_opacity = 0.7))

fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(), style_function = lambda x:{"fillColor":"black" 
if x["properties"]["POP2005"]<10000000 else"orange" if 10000000 <= x["properties"]["POP2005"] < 250000000 else "red"}))

#for(lt,ln,nm,el in zip(lat,lon,name,elev)):
 #   folium.


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")

