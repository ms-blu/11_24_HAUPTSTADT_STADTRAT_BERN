
import pandas as pd
import plotly.express as px

df = pd.read_csv('2_DATEN_CSVS/8_speakingTime_parteien_weighed_noFeuz')

df['redezeit'] = df['redezeit'] * 100 / df['redezeit'].sum()

df['sitze_aktuell'] = df['sitze_aktuell'] * 100 / 80

print(df['sitze_aktuell'])
# Create a scatter chart
fig = px.scatter(
    df,
    x='sitze_aktuell',
    y='redezeit',
    title="Redezeit nach Partei<br><sup>Ohne Gemeinderat und Präsident*in</sup>",
    labels={'partei': 'Partei', 'redezeit': 'Redeanteil in Prozent', 'sitze_aktuell': 'Sitzanteil in Prozent'},
    text='partei',
    color_discrete_sequence=['#b3d6d8'],  # Bar color
    category_orders={'partei': df.sort_values('redezeit', ascending=False)['partei'].tolist()},
)


# Update the background color
fig.update_layout(
    plot_bgcolor='white',  # Plot area background color
    title=dict(automargin=True,yref='paper')
)

fig.add_shape(
    type="line",
    x0=min(df["sitze_aktuell"]),
    y0=min(df["redezeit"]),
    x1=max(df["sitze_aktuell"]),
    y1=max(df["redezeit"]),
    line=dict(color="lightgray", width=2)
)


fig.update_yaxes(gridcolor='lightgray')  # Horizontal grid line color


fig.update_traces(textposition='top center')



fig.show()
fig.write_html('7_speakingTime_parteien_weighed_noFeuz')

fig.show()


