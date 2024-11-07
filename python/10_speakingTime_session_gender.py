import random

import pandas as pd
import statistics
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

df = pd.read_csv('2_DATEN_CSVS/010_redezeit_sitzung_gender')

print(df.columns)

average_redezeit = df.groupby(['name','gender'])['redezeit'].mean().reset_index()


print(average_redezeit)


# # Create a scatter chart
# fig = px.scatter(
#     average_redezeit,
#     x='gender',
#     y='redezeit',
#     title="",
#     labels={'gender': 'Geschlecht', 'redezeit': 'Redezeit'},
#     text='name',
#     color_discrete_sequence=['#b3d6d8'],  # Bar color
#     category_orders={'gender': df.sort_values('redezeit', ascending=False)['gender'].tolist()},
# )
#
#
# # Update the background color
# fig.update_layout(
#     plot_bgcolor='white',  # Plot area background color
#     title=dict(automargin=True,yref='paper')
# )
#
#
#
#
# fig.update_yaxes(gridcolor='lightgray')  # Horizontal grid line color
#
#
# fig.update_traces(textposition='top center')
#
#
#
# fig.show()
# fig.write_html('010_redezeit_sitzung_gender')
#
# fig.show()




layout = {'title': 'Durchschnittliche Redezeit pro Sitzung in Sekunden'}
traces = []

traces.append({'x': average_redezeit['gender'], 'y': average_redezeit['redezeit'],'text': average_redezeit['name'],  'marker': {'color': '#b3d6d8'}})


# Update (add) trace elements common to all traces.
for t in traces:
    t.update({'type': 'box',
              'boxpoints': 'all',
              'fillcolor': 'rgba(255,255,255,0)',
              'hoveron': 'points',
              'hovertemplate': '%{text}<br>Geschlecht=%{x}<br>Redezeit=%{y}<extra></extra>',
              'line': {'color': 'rgba(255,255,255,0)'},
              'pointpos': 0,
              'showlegend': False})

fig = px.scatter()
for t in traces:
    fig.add_trace(t)
fig.add_shape(type="line",
              x0=-0.5,
              y0=statistics.mean(average_redezeit[average_redezeit['gender'] == 'male']['redezeit']),
              x1=0.5,
              y1=statistics.mean(average_redezeit[average_redezeit['gender'] == 'male']['redezeit']),
              line=dict(
                  color="LightSeaGreen",
                  width=2,
                  dash="dashdot",
              ),
              label=dict(text=f"Durchschnitt Männer: {round(statistics.mean(average_redezeit[average_redezeit['gender'] == 'male']['redezeit']),2)}",
                         textposition="start")
              )
fig.add_shape(type="line",
              x0=0.5,
              y0=statistics.mean(average_redezeit[average_redezeit['gender'] == 'female']['redezeit']),
              x1=1.5,
              y1=statistics.mean(average_redezeit[average_redezeit['gender'] == 'female']['redezeit']),
              line=dict(
                  color="Red",
                  width=2,
                  dash="dashdot",
              ),
              label=dict(text=f"Durchschnitt Frauen: {round(statistics.mean(average_redezeit[average_redezeit['gender'] == 'female']['redezeit']),2)}",
                         textposition="start")
              )

pio.show(fig)
fig.write_html('10_speakingTime_session_gender.html')