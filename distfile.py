import requests
import json# call the OSMR API
import pandas as pd

filepath = "C:/Users/Yong Jian Rong/OneDrive/1NTU Notes/0AY2022-23/HE3613 Urban Economics/Data Set/Public Transport"
filename = '/hdb.csv'

df = pd.read_csv(filepath+filename)

for row in df.iterrows():
    print(row['lng'])
    print(row['lat'])
lon_1 = 103.7233061
lat_1 = 1.333889396
lon_2 = 103.8513
lat_2 = 1.2830

def router(lon_1,lat_1,lon_2,lat_2):
    r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon_1},{lat_1};{lon_2},{lat_2}?overview=false""")# then you load the response using the json libray
    # by default you get only one alternative so you access 0-th element of the `routes`
    
    routes = json.loads(r.content)
    # print(routes)
    route_1 = routes.get("routes")[0]
    # print(f"Overall, the route data is:\n{route_1}\n")
    seconds = route_1['legs'][0]['duration']
    print(f"Duration: {seconds}sec ({seconds/60:.2f} min )")
    print(f"The distance is {route_1['legs'][0]['distance']} metres")