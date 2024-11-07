
import pandas as pd
import plotly.express as px

df = pd.read_csv('2_DATEN_CSVS/3_speakingTime_gendered')
df['redezeit'] = df['redezeit'] / 60

# Create a bar chart
fig = px.bar(
    df,
    x='redezeit',
    y='geschlecht',
    title="Redezeit nach Geschlecht<br><sup>Ohne Gemeinderat und Präsident*in</sup>",
    labels={'geschlecht': 'Geschlechtsidentität', 'redezeit': 'Redezeit in Minuten'},
    color_discrete_sequence=['#b3d6d8'],  # Bar color
    category_orders={'geschlecht': df.sort_values('redezeit', ascending=False)['geschlecht'].tolist()},

)

# Update the background color
fig.update_layout(
    plot_bgcolor='white',  # Plot area background color

)

fig.update_yaxes(gridcolor='lightgray')  # Horizontal grid line color
fig.update_yaxes(tickvals=['female', 'male', 'nonbinary'], ticktext=['weiblich', 'männlich', 'nichtbinär'])

fig.show()

#fig.write_html('3_speakingTime_gendered.html')

