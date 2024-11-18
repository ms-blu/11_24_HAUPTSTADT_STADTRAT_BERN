
import pandas as pd
import plotly.express as px

df = pd.read_csv('2_DATEN_CSVS/03_speakingTime_gendered')
df['redezeit'] = df['redezeit'] / 60

# Create a bar chart
fig = px.bar(
    df,
    y='redezeit',
    x='geschlecht',
    labels={'geschlecht': 'Geschlechtsidentität', 'redezeit': 'Redezeit in Minuten'},
    color_discrete_sequence=['#b3d6d8'],  # Bar color
    category_orders={'geschlecht': df.sort_values('redezeit', ascending=False)['geschlecht'].tolist()},

)

# Update the background color
fig.update_layout(
    plot_bgcolor='white',  # Plot area background color
    title=dict(automargin=True, yref='paper')
)

fig.update_yaxes(gridcolor='lightgray')  # Horizontal grid line color
fig.update_xaxes(tickvals=['female', 'male', 'nonbinary'], ticktext=['weiblich', 'männlich', 'nichtbinär'])

fig.update_layout(
    font=dict(
        family="Arial",  # Change font family

    )
)
fig.update_layout(autosize=True)
fig.show(config={'displayModeBar': False})

fig.update_layout(modebar_remove=("autoScale2d", "autoscale", "editInChartStudio", "editinchartstudio", "hoverCompareCartesian", "hovercompare", "lasso", "lasso2d", "orbitRotation", "orbitrotation", "pan", "pan2d", "pan3d", "reset", "resetCameraDefault3d", "resetCameraLastSave3d", "resetGeo", "resetSankeyGroup", "resetScale2d", "resetViewMap", "resetViewMapbox", "resetViews", "resetcameradefault", "resetcameralastsave", "resetsankeygroup", "resetscale", "resetview", "resetviews", "select", "select2d", "sendDataToCloud", "senddatatocloud", "tableRotation", "tablerotation", "toImage", "toggleHover", "toggleSpikelines", "togglehover", "togglespikelines", "toimage", "zoom", "zoom2d", "zoom3d", "zoomIn2d", "zoomInGeo", "zoomInMap", "zoomInMapbox", "zoomOut2d", "zoomOutGeo", "zoomOutMap", "zoomOutMapbox", "zoomin", "zoomout"))
fig.write_html("3_HTML/3_speakingTime_gendered.html", full_html=False, include_plotlyjs='cdn')
#fig.write_html('3_speakingTime_gendered.html')

