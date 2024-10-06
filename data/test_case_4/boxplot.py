
import pandas as pd
import plotly.express as px


size_df_path = './test_case_4_size_tall.csv'
size_df = pd.read_csv(size_df_path)

speed_df_path = './test_case_4_speed_tall.csv'
speed_df = pd.read_csv(speed_df_path)

df = pd.concat([
    size_df,
    speed_df
], ignore_index=True)


df['Object, Intent'] = df['object_intent']
df['Mean Absolute Deviation (MAD) % of 100'] = df['diff']

fig = px.box(
    df,
    x='Object, Intent',
    y='Mean Absolute Deviation (MAD) % of 100',
    color_discrete_sequence=['rgb(0,0,0)']
)
fig.update_layout(
    #marker_color='rgb(7,40,89)',
    #line_color='rgb(7,40,89)',
    plot_bgcolor='rgb(255,255,255)',
    paper_bgcolor='rgb(255,255,255)',
    #grid_color="Grey"
)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Grey')
fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Grey')
fig.show()
