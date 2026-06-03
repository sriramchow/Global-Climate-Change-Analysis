import os
import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# ── Load & prepare data ───────────────────────────────────────────────────────
BASE  = os.path.dirname(os.path.abspath(__file__))
CSV   = os.path.join(BASE, '..', 'Final_Project_SDV', 'data', 'GlobalLandTemperaturesByCountry.csv')

df = pd.read_csv(CSV)
df['dt']   = pd.to_datetime(df['dt'])
df['Year'] = df['dt'].dt.year
df         = df[df['Year'] >= 2000]

df = df.rename(columns={
    'AverageTemperature':            'AvgTemp',
    'AverageTemperatureUncertainty': 'TempUncertainty',
})
df = df.dropna(subset=['AvgTemp', 'Country'])

df_grouped = df.groupby(['Country', 'Year'])[['AvgTemp', 'TempUncertainty']].mean().reset_index()
df_grouped['RollingTemp'] = (
    df_grouped.groupby('Country')['AvgTemp']
    .transform(lambda x: x.rolling(window=3, min_periods=1).mean())
)

countries = sorted(df_grouped['Country'].unique())
year_min  = int(df_grouped['Year'].min())
year_max  = int(df_grouped['Year'].max())

# ── App ───────────────────────────────────────────────────────────────────────
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server   # expose for gunicorn

app.layout = dbc.Container([

    # Header
    html.Div([
        html.H1("🌍 Global Climate Change Dashboard",
                style={'textAlign': 'center', 'marginTop': 24, 'marginBottom': 4,
                       'fontWeight': '800', 'letterSpacing': '-.5px'}),
        html.P("Explore global land temperature trends from 2000 to 2015",
               style={'textAlign': 'center', 'color': '#94a3b8', 'marginBottom': 24}),
    ]),

    dbc.Row([

        # ── Sidebar controls ──────────────────────────────────────────────────
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label("🌐 Select Country", className="fw-semibold mb-1"),
                    dcc.Dropdown(
                        id='country-dropdown',
                        options=[{'label': c, 'value': c} for c in countries],
                        value='India',
                        clearable=False,
                        style={'color': '#000'},
                    ),

                    html.Hr(),

                    html.Label("📅 Year Range", className="fw-semibold mb-1"),
                    dcc.RangeSlider(
                        id='year-slider',
                        min=year_min, max=year_max,
                        value=[2000, 2015],
                        marks={y: str(y) for y in range(year_min, year_max+1, 3)},
                        tooltip={"placement": "bottom", "always_visible": False},
                    ),

                    html.Hr(),

                    html.Label("🌡 Temperature Range (°C)", className="fw-semibold mb-1"),
                    dcc.RangeSlider(
                        id='temp-slider',
                        min=-20, max=40,
                        value=[0, 30],
                        marks={i: f"{i}°C" for i in range(-20, 41, 10)},
                        tooltip={"placement": "bottom", "always_visible": False},
                    ),
                ])
            ], style={'position': 'sticky', 'top': 16}),
        ], width=3),

        # ── Charts ───────────────────────────────────────────────────────────
        dbc.Col([
            dcc.Graph(id='line-plot',        style={'marginBottom': 16}),
            dcc.Graph(id='scatter-plot',     style={'marginBottom': 16}),
            dcc.Graph(id='box-plot',         style={'marginBottom': 16}),
            dcc.Graph(id='histogram-plot',   style={'marginBottom': 16}),
            dcc.Graph(id='choropleth-plot'),
        ], width=9),

    ]),

    html.Hr(),
    html.P([
        "Built by ",
        html.A("SriRam Chowdary", href="https://github.com/sriramchow", target="_blank"),
        " · Data: Berkeley Earth / Kaggle",
    ], style={'textAlign': 'center', 'color': '#475569', 'fontSize': '.8rem', 'padding': '1rem 0'}),

], fluid=True)


# ── Callback ──────────────────────────────────────────────────────────────────
@app.callback(
    Output('line-plot',      'figure'),
    Output('scatter-plot',   'figure'),
    Output('box-plot',       'figure'),
    Output('histogram-plot', 'figure'),
    Output('choropleth-plot','figure'),
    Input('country-dropdown','value'),
    Input('year-slider',     'value'),
    Input('temp-slider',     'value'),
)
def update_graphs(country, years, temp_range):
    filtered = df_grouped[
        (df_grouped['Year']    >= years[0])      &
        (df_grouped['Year']    <= years[1])      &
        (df_grouped['AvgTemp'] >= temp_range[0]) &
        (df_grouped['AvgTemp'] <= temp_range[1])
    ]
    cdf = filtered[filtered['Country'] == country]

    line_fig = px.line(
        cdf, x='Year', y='AvgTemp',
        title=f'Average Temperature Over Time — {country}',
        template='plotly_dark', markers=True,
    )
    line_fig.update_traces(line_color='#06b6d4')

    scatter_fig = px.scatter(
        cdf, x='Year', y='TempUncertainty', color='AvgTemp',
        title='Year vs Temperature Uncertainty',
        template='plotly_dark',
        color_continuous_scale='Viridis',
    )

    box_fig = px.box(
        cdf, y='AvgTemp',
        title=f'Temperature Distribution — {country}',
        template='plotly_dark',
    )
    box_fig.update_traces(marker_color='#3b82f6')

    hist_fig = px.histogram(
        cdf, x='AvgTemp', nbins=30,
        title='Temperature Frequency Distribution',
        template='plotly_dark',
    )
    hist_fig.update_traces(marker_color='#10b981')

    choropleth_fig = px.choropleth(
        filtered,
        locations='Country', locationmode='country names',
        color='AvgTemp', hover_name='Country',
        animation_frame='Year',
        color_continuous_scale=px.colors.sequential.Plasma,
        title='World Map — Average Temperature',
    )
    choropleth_fig.update_layout(template='plotly_dark')

    return line_fig, scatter_fig, box_fig, hist_fig, choropleth_fig


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run(debug=False, host='0.0.0.0', port=port)
