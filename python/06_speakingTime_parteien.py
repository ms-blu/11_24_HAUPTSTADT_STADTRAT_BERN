
import pandas as pd
import plotly.express as px

df = pd.read_csv('2_DATEN_CSVS/6_speakingTime_parteien')
df['redezeit'] = df['redezeit'] / 60

# Create a bar chart
fig = px.scatter(
    df,
    y='redezeit',
    x='partei',
    labels={'partei': 'Partei', 'redezeit': 'Redezeit in Minuten'},
    color_discrete_sequence=['#b3d6d8'],  # Bar color
    category_orders={'partei': df.sort_values('redezeit', ascending=False)['partei'].tolist()},

)

# Update the background color
fig.update_layout(
    plot_bgcolor='white',  # Plot area background color
    title=dict(text="Parteien nach Redezeit <br><sup>Ohne Gemeinderat und Präsident*in</sup>", automargin=True, yref='paper')
)

fig.update_yaxes(gridcolor='lightgray')  # Horizontal grid line color
fig.write_html('6_speakingTime_parteien.html')

fig.show()


