import plotly.express as px


def plot_airport_line(df, airport):
    df = df.loc[df['apt'] == airport]
    fig = px.line(df, x='date', y='traffic', markers=True)
    return fig
