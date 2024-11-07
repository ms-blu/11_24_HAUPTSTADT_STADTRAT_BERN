
import pandas as pd
import plotly.express as px

df = pd.read_csv('2_DATEN_CSVS/2_top10_speakingTime_excl_president_execkutive')
df['redezeit'] = df['redezeit'] / 60

# Create a bar chart
fig = px.bar(
    df,
    y='name',
    x='redezeit',
    title="Top 10 Stadtrats-Mitglieder nach Redezeit <br><sup>Ohne Gemeinderat und Präsident*in</sup>",
    labels={'name': 'Stadtrat-Mitglied', 'redezeit': 'Redezeit in Minuten'},
    color_discrete_sequence=['#b3d6d8'],  # Bar color
    category_orders={'name': df.sort_values('redezeit', ascending=False)['name'].tolist()},

)

# Update the background color
fig.update_layout(
    plot_bgcolor='white',  # Plot area background color
)

fig.update_yaxes(gridcolor='lightgray')  # Horizontal grid line color

fig.show()
fig.write_html('2_top10_speakingTime_excl_president_execkutive.html')


