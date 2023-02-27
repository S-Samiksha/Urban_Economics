import overpy

api = overpy.Overpass()

# Define a bounding box around the area you want to search in
bbox = (52.5, 13.35, 52.55, 13.4)

# Build a query to search for all nodes tagged as bus stops within 500m of the bounding box
query = """
    node["highway"="bus_stop"](around:500, {}, {}, {}, {});
    out;
""".format(*bbox)

# Execute the query and get the results
result = api.query(query)

# Print the coordinates of each bus stop found
for node in result.nodes:
    print(node.lat, node.lon)
