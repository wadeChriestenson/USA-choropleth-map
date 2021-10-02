# Packages needed
import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    # CSV to pull population per county for Choropleth
df = pd.read_csv("population.csv",
                 dtype={"fips": str})
# Ploty function to render Choropleth
usa = px.choropleth(df,
                    geojson=counties,
                    locations='fips',
                    color='uep',
                    color_continuous_scale="Portland",
                    range_color=(0, 10),
                    hover_name='county_name',
                    hover_data=['fips', 'uep', 'tot_pop'],
                    labels={"fips": "FIPS", 'uep': 'Unemployment Rate', 'tot_pop': 'Population'},
                    # template='presentation',

                    )
usa.update_layout(
    title={
        'text': "United States Unemployment per County ",
        'y': 0.05,
        'x': 0.45,
        'font_size': 28,
        'xanchor': 'center',
        'yanchor': 'top'},
    # separators=',',
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
)
usa.update_geos(
    scope='usa',
    visible=False,

)

usa.show()
