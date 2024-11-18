import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('2_DATEN_CSVS/05_speakingTime_gendered_weighed_noFeuz')

# Normalize values
df['redezeit'] = df['redezeit'] * 100 / df['redezeit'].sum()
df['sitze_aktuell'] = df['sitze_aktuell'] * 100 / 80

# Gender translation dictionary
gender_translation = {
    'male': 'männlich',
    'female': 'weiblich',
    'non-binary': 'Nicht-binär',  # Example, adjust based on actual values
}

# Add a column with translated gender labels for display
df['geschlecht_anzeige'] = df['geschlecht'].map(gender_translation)

# Create a scatter chart
fig = px.scatter(
    df,
    x='sitze_aktuell',
    y='redezeit',
    labels={'geschlecht': 'Geschlecht', 'redezeit': 'Redeanteil in Prozent', 'sitze_aktuell': 'Sitzanteil in Prozent'},
    text='geschlecht_anzeige',  # Use translated labels for text
    color_discrete_sequence=['#b3d6d8'],
    category_orders={'geschlecht': df.sort_values('redezeit', ascending=False)['geschlecht'].tolist()},
)

# Update the layout
fig.update_layout(
    plot_bgcolor='white',
    font=dict(family="Arial"),
    title=dict(automargin=False, yref='paper'),
)

# Add a diagonal reference line
fig.add_shape(
    type="line",
    x0=min(df["sitze_aktuell"]),
    y0=min(df["redezeit"]),
    x1=max(df["sitze_aktuell"]),
    y1=max(df["redezeit"]),
    line=dict(color="lightgray", width=2)
)

# Update axes and traces
fig.update_yaxes(gridcolor='lightgray')
fig.update_traces(textposition='top center')
fig.update_layout(modebar_remove=("autoScale2d", "autoscale", "editInChartStudio", "editinchartstudio", "hoverCompareCartesian", "hovercompare", "lasso", "lasso2d", "orbitRotation", "orbitrotation", "pan", "pan2d", "pan3d", "reset", "resetCameraDefault3d", "resetCameraLastSave3d", "resetGeo", "resetSankeyGroup", "resetScale2d", "resetViewMap", "resetViewMapbox", "resetViews", "resetcameradefault", "resetcameralastsave", "resetsankeygroup", "resetscale", "resetview", "resetviews", "select", "select2d", "sendDataToCloud", "senddatatocloud", "tableRotation", "tablerotation", "toImage", "toggleHover", "toggleSpikelines", "togglehover", "togglespikelines", "toimage", "zoom", "zoom2d", "zoom3d", "zoomIn2d", "zoomInGeo", "zoomInMap", "zoomInMapbox", "zoomOut2d", "zoomOutGeo", "zoomOutMap", "zoomOutMapbox", "zoomin", "zoomout"))
fig.update_layout(
    autosize=True)
# Remove mode bar
fig.show(config={'displayModeBar': False})

# Save the chart
fig.write_html("3_HTML/5_speakingTime_gendered_noFeuz.html", full_html=False, include_plotlyjs='cdn')
