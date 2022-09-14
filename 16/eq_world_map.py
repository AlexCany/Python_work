import plotly.express as px
from eq_explore_data import lons, lats, titles, mags
import pandas as pd

#data = pd.DataFrame(
#	data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
#)

fig = px.scatter(
	
	x='经度',
	y='纬度',
	range_x=[-200, 200],
	range_y=[-90, 90],
	width=800,
	height=800,
	title='全球地震散点图',
	size='震级',
	size_max=10,
)
fig.write_html('global_earthquakes.html')
fig.show()