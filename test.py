import plotly.express as px
# Points in (lat, lon) format.
peak_coords = [
(63.069, -151.0063),
(60.5671, -140.4055),
(46.8529, -121.7604),
]
# Make matching lists of lats, lons,
# and labels.
lats = [pc[0] for pc in peak_coords]
lons = [pc[1] for pc in peak_coords]
peak_names = [
"Denali",
"Mt Logan",
"Mt Rainier"
]
elevations = [20_000, 18_000, 14_000]
# Generate initial map.
title = "Selected High Peaks"
fig = px.scatter_geo(
lat=lats,
lon=lons,
title=title,
projection="natural earth",
text=peak_names,
size=elevations,
scope="north america",
)
# Customize formatting options.
fig.update_layout(titlefont_size=24)
fig.update_traces(
textposition="middle right",
textfont_size=18,
)

fig.show()

# test = 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
