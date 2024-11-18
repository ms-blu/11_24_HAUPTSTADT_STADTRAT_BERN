import pandas as pd
import plotly.express as px
import numpy as np

# Load the data from the updated file path
data = pd.read_csv('2_DATEN_CSVS/07_speakingTime_parteien_weighed')

# Normalize values (assuming total seats are 80)
data['redezeit'] = data['redezeit'] * 100 / data['redezeit'].sum()
data['sitze_aktuell'] = data['sitze_aktuell'].fillna(0)  # Replace NA with 0 for plotting
data['sitze_aktuell'] = data['sitze_aktuell'] * 100 / 80

# List of visible parties (you can change this list to include the parties you want to display)
visible_parties = ['FDP', 'SP', 'SVP', 'GLP', 'GFL', 'AL', 'Mitte', 'GB']  # Example: only these parties will be visible

# Add a new column to mark which parties should be visible
data['visible'] = data['partei'].isin(visible_parties)

# Create the scatter plot
fig = px.scatter(
    data,
    x='sitze_aktuell',
    y='redezeit',
    labels={'partei': 'Partei', 'redezeit': 'Redeanteil in Prozent', 'sitze_aktuell': 'Sitzanteil in Prozent'},
    color_discrete_sequence=['#b3d6d8'],  # Marker color
    hover_name='partei'  # Display labels on hover
)

# Update layout for better visuals
fig.update_layout(
    plot_bgcolor='white',
    font=dict(family="Arial"),
    title=dict(automargin=True, yref='paper'),
)
fig.update_yaxes(gridcolor='lightgray')
fig.update_layout(modebar_remove=("autoScale2d", "autoscale", "editInChartStudio", "editinchartstudio", "hoverCompareCartesian", "hovercompare", "lasso", "lasso2d", "orbitRotation", "orbitrotation", "pan", "pan2d", "pan3d", "reset", "resetCameraDefault3d", "resetCameraLastSave3d", "resetGeo", "resetSankeyGroup", "resetScale2d", "resetViewMap", "resetViewMapbox", "resetViews", "resetcameradefault", "resetcameralastsave", "resetsankeygroup", "resetscale", "resetview", "resetviews", "select", "select2d", "sendDataToCloud", "senddatatocloud", "tableRotation", "tablerotation", "toImage", "toggleHover", "toggleSpikelines", "togglehover", "togglespikelines", "toimage", "zoom", "zoom2d", "zoom3d", "zoomIn2d", "zoomInGeo", "zoomInMap", "zoomInMapbox", "zoomOut2d", "zoomOutGeo", "zoomOutMap", "zoomOutMapbox", "zoomin", "zoomout"))
fig.update_layout(
    autosize=True)
# Add a diagonal reference line
fig.add_shape(
    type="line",
    x0=min(data["sitze_aktuell"]),
    y0=min(data["redezeit"]),
    x1=max(data["sitze_aktuell"]),
    y1=max(data["redezeit"]),
    line=dict(color="lightgray", width=2)
)

# Add annotations dynamically with adjusted positions
for i, row in data.iterrows():
    if row['visible']:  # Only add annotation for visible parties
        fig.add_annotation(
            x=row['sitze_aktuell'],
            y=row['redezeit'],
            text=row['partei'],  # Label text
            showarrow=False,  # No arrow for non-colliding points
            font=dict(color="black"),  # Increased font size
            xanchor='center',  # Center horizontally
            yanchor='bottom',  # Place text above the point
        )

# Save and display the chart
fig.write_html("3_HTML/7_speakingTime_parteien_weighed.html", full_html=False, include_plotlyjs='cdn')
fig.show()
