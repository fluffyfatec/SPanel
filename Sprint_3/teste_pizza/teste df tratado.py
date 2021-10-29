import dash
import dash_core_components as dcc
import dash_table as dt
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import pdb
# ==================================================================
# Pré processamentos
df= pd.read_csv("df_tratado.csv")
df_estado = pd.read_csv("df_estadotratado.csv")
date_column = df_estado["estado"]
max=date_column.max()
row=df_estado.loc[df_estado["estado"] == max]

date_column = df["datahora"]
max=date_column.max()
row=df.loc[df["datahora"] == max]

list_municipios= sorted(row['nome_munic'].unique())
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[{"label": i, "value": i} for i in list_municipios
                 ],
        multi=True
    ),
#Tabela
    dt.DataTable(
        id='table',
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in sorted(df.columns)],
        editable=True,
        sort_action="native",
        sort_mode="single",
        column_selectable="multi",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=8,

        tooltip_conditional=[
            {
                'if': {
                    'filter_query': '{nome_munic} contains "SÃO PAULO"'
                },
                'type': 'markdown',
                'value': 'Uma das 10 maiores cidades do estado de São Paulo.'
            }
        ],

        style_data_conditional=[
            {
                'if': {
                    'filter_query': '{nome_munic} contains "SÃO PAULO"'
                },
                'backgroundColor': '#0074D9',
                'color': 'white',
                'textDecoration': 'underline',
                'textDecorationStyle': 'dotted',
            }
        ],
        tooltip_delay=0,
        tooltip_duration=None
    )])

#======= Callback

@app.callback(
    Output("table", "data"),
    Input("demo-dropdown", "value")
)
def update_table(location):
    if location is not None:

        df_municipios = row[row["nome_munic"].isin(location)]
        df_loc = df_municipios.to_dict('records')
        return df_loc


if __name__ == '__main__':
    app.run_server(debug=True)
