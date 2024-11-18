import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('2_DATEN_CSVS/09_stichwortsuche')

# Create a bar chart
fig = px.bar(
    df,
    x='doc_id',
    y='reitschule',
    labels={'doc_id': 'Partei', 'reitschule': 'Erwähnungen'},
    color_discrete_sequence=['#b3d6d8'],  # Bar color
    category_orders={'doc_id': df.sort_values('reitschule', ascending=False)['doc_id'].tolist()}
)

# Update the layout and background
fig.update_layout(
    plot_bgcolor='white',  # Plot area background color
    title=dict(automargin=False, yref='paper'),
)

# Add gridline color
fig.update_yaxes(gridcolor='lightgray')


fig.update_layout(
    font=dict(
        family="Arial",  # Change font family


    )
)
fig.update_layout(
    autosize=True,
)

fig.update_layout(modebar_remove=("autoScale2d", "autoscale", "editInChartStudio", "editinchartstudio", "hoverCompareCartesian", "hovercompare", "lasso", "lasso2d", "orbitRotation", "orbitrotation", "pan", "pan2d", "pan3d", "reset", "resetCameraDefault3d", "resetCameraLastSave3d", "resetGeo", "resetSankeyGroup", "resetScale2d", "resetViewMap", "resetViewMapbox", "resetViews", "resetcameradefault", "resetcameralastsave", "resetsankeygroup", "resetscale", "resetview", "resetviews", "select", "select2d", "sendDataToCloud", "senddatatocloud", "tableRotation", "tablerotation", "toImage", "toggleHover", "toggleSpikelines", "togglehover", "togglespikelines", "toimage", "zoom", "zoom2d", "zoom3d", "zoomIn2d", "zoomInGeo", "zoomInMap", "zoomInMapbox", "zoomOut2d", "zoomOutGeo", "zoomOutMap", "zoomOutMapbox", "zoomin", "zoomout"))
fig.write_html("3_HTML/11_erwaehnungen_reitschule.html", full_html=False, include_plotlyjs='cdn')

# Display the chart
fig.show(config={'displayModeBar': False})
