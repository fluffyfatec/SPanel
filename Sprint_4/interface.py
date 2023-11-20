# SPANEL SPRINT 3

# ==================================================================
# Bibliotecas do layout
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_html_components as html


# ==================================================================
# Bibliotecas dos graficos e tabelas
import plotly.graph_objects as go
import dash_table as dt
from plotly.subplots import make_subplots

# ==================================================================
# Bibliotecas de manipulação de dados
import pandas as pd
pd.options.mode.chained_assignment = None

# ==================================================================
# Pré processamentos
# Leitura de CSVs
df_tratado = pd.read_csv("docs/df_tratado.csv")
df_vacinastratado = pd.read_csv("docs/df_vacinastratado.csv")
df_estadotratado = pd.read_csv("docs/df_estadotratado.csv")
df_vacinas = pd.read_csv("docs/vacinas.csv", sep=';')
df_vacinas = df_vacinas.rename(
    columns={'Município': 'nome_munic'})
df_regiao_tratado = pd.read_csv("docs/df_regiao_tratado.csv")
# Lista de municipios para dropdown
list_municipios = sorted(df_tratado['nome_munic'].unique())
list_drs = sorted(df_regiao_tratado['nome_drs'].unique())
# Pre Tabela
date_column = df_tratado["datahora"]
max = date_column.max()
row = df_tratado.loc[df_tratado["datahora"] == max]
df_vacinastratadonotpop = df_vacinastratado.drop(columns=['pop'])
df_totais = pd.merge(row,df_vacinastratadonotpop, how='inner', on='nome_munic')
df_totais = df_totais.drop(
    columns=['Unnamed: 0_x', 'Unnamed: 0_y'])
df_tratado_rename = df_totais.rename(
                columns={'nome_munic': 'Localização', 'casos': 'Casos Acumulados', 'datahora': 'Data da Atualização',
                         'obitos': "Óbitos Acumulados","pop": "População","doseunica":"Dose Unica","primeiradose":"Primeira Dose",
                         "segundadose":"Segunda Dose","terceiradose":"Terceira Dose"})
df_tratado_rename = df_tratado_rename.reindex(
                columns=['Localização', 'Casos Acumulados', 'Óbitos Acumulados','Dose Unica','Primeira Dose','Segunda Dose','Terceira Dose','População', 'Data da Atualização'])

casosacumulados = df_tratado_rename["Casos Acumulados"].sum()
obitossacumulados = df_tratado_rename["Óbitos Acumulados"].sum()
doseunica = df_tratado_rename["Dose Unica"].sum()
primeiradose = df_tratado_rename["Primeira Dose"].sum()
segundadose = df_tratado_rename["Segunda Dose"].sum()
terceiradose = df_tratado_rename["Terceira Dose"].sum()
populacao = df_tratado_rename["População"].sum()
data = df_tratado_rename['Data da Atualização'].max()
new_row = dict(zip(df_tratado_rename.columns, ['ESTADO DE SÃO PAULO', casosacumulados, obitossacumulados, doseunica, primeiradose, segundadose, terceiradose, populacao, data]))

# Use concat to add the new row to the DataFrame
df_tratado_rename = pd.concat([df_tratado_rename, pd.DataFrame([new_row])], ignore_index=True)

# List of municipalities
list_tabela = ['ESTADO DE SÃO PAULO', 'SÃO PAULO', 'GUARULHOS', 'CAMPINAS', 'SÃO BERNARDO DO CAMPO', 'SÃO JOSÉ DOS CAMPOS', 'SANTO ANDRÉ']

# List of municipalities from the DataFrame
list_municipios2 = sorted(df_tratado_rename['Localização'].unique())

# ==================================================================
# Graficos
# Grafico bar casos novos
fig0 = go.Figure()
fig0.add_trace(go.Bar(x=df_vacinas["Total Doses Aplicadas"], y=df_vacinas["Dose"],text=df_vacinas["Total Doses Aplicadas"],marker_color='#db261f',orientation='h'),)
fig0.update_layout(
    yaxis=dict(showline=True,showticklabels=True,
    linecolor='rgb(204, 204, 204)'),
    xaxis=dict(ticks="outside",gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    title='<b>Vacinas Aplicadas',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    xaxis_title='Total de Doses Aplicadas',
    yaxis_title='Dose',
    plot_bgcolor='white',
    title_x = 0.5,
    autosize=True,
    margin = dict(l=50, r=30, t=40, b=90))

#Grafico pizza imunizados
colors = ['#1f1b18','#db261f']
fig5 = go.Figure()
fig5.add_trace(go.Pie(values= df_vacinas["Total Doses Aplicadas"], labels=df_vacinas["Dose"],pull=[0, 0.05],hole=.3,marker=dict(colors=colors)))
fig5.update_layout(
    title_text='<b>Vacinômetro',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    title_x = 0.5,
    autosize=True,
    margin = dict(l=150, r=50, t=40, b=40),
)

# Grafico linha casos
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df_estadotratado["datahora"], y=df_estadotratado["casos"],fill='tozeroy',line_shape='spline',line=dict(color='#db261f',width=2)))
fig1.update_layout(
    yaxis=dict(ticks="outside",gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    xaxis=dict(gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    title='<b>Casos Acumulados por Período',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    xaxis_title='Data',
    yaxis_title='Casos Acumulados',
    plot_bgcolor='white',
    title_x = 0.5,
    autosize=True,
    margin = dict(l=50, r=30, t=40, b=80),
)

# Grafico bar casos novos
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=df_estadotratado["datahora"], y=df_estadotratado["casos_novos"],text=df_estadotratado["casos_novos"],marker_color='#db261f'),)
fig2.update_layout(
    yaxis=dict(ticks="outside",gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    xaxis=dict(showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    title='<b>Casos Novos por Período',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    xaxis_title='Data',
    yaxis_title='Casos Novos',
    plot_bgcolor='white',
    title_x = 0.5,
    autosize=True,
    margin = dict(l=85, r=20, t=40, b=80))

# Grafico linhas obitos
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=df_estadotratado["datahora"], y=df_estadotratado["obitos"],fill='tozeroy',line_shape='spline',line=dict(color='#db261f',width=2)))
fig3.update_layout(
    yaxis=dict(ticks="outside",gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    xaxis=dict(gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    title='<b>Óbitos Acumulados por Período',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    xaxis_title='Data',
    yaxis_title='Óbitos Acumulados',
    plot_bgcolor='white',
    title_x = 0.5,
    autosize=True,
    margin = dict(l=50, r=30, t=40, b=80),
)

# Grafico bar obitos novos
fig4 = go.Figure()
fig4.add_trace(go.Bar(x=df_estadotratado["datahora"], y=df_estadotratado["obitos_novos"],text=df_estadotratado["obitos_novos"],marker_color='#db261f'),)
fig4.update_layout(
    yaxis=dict(ticks="outside", gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    xaxis=dict(showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    title='<b>Óbitos Novos por Período',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    xaxis_title='Data',
    yaxis_title='Óbitos Novos',
    plot_bgcolor='white',
    title_x = 0.5,
    autosize=True,
    margin = dict(l=85, r=20, t=40, b=80),
    showlegend=False)

# Grafico de linha letalidade
fig6 = go.Figure()
fig6.add_trace(go.Scatter(x=df_tratado["datahora"], y=df_tratado["casos_novos"], fill='tozeroy',line_shape='spline',line=dict(color='#db261f',width=2)))
fig6.update_layout(
    yaxis=dict(ticks="outside",gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    xaxis=dict(gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    title='<b>Letalidade por Período',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    xaxis_title='Data',
    yaxis_title='Letalidade (%)',
    plot_bgcolor='white',
    title_x = 0.5,
    autosize=True,
    margin = dict(l=50, r=30, t=40, b=80),
    showlegend=False
)

# Grafico de Pizza letalidade
colors2 = ['#db261f', '#1f1b18']
fig7 = go.Figure()
fig7.add_trace(go.Pie(values= df_vacinas["Total Doses Aplicadas"], labels=df_vacinas["Dose"],pull=[0, 0.05],hole=.3,marker=dict(colors=colors2)))
fig7.update_layout(
    title_text='<b>Letalidade',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    title_x = 0.5,
    autosize=True,
    margin = dict(l=40, r=50, t=40, b=40),
)

# grafico setor 1 regiões
fig8 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],subplot_titles=['Leitos Ocupados(%)', 'Leitos Ocupados - Ultimos 7 Dias(%)'])
fig8.update_layout(
    margin = dict(l=20, r=50, t=20, b=10),
)

# gráfico barra regiões
fig10 = go.Figure()
fig10.add_trace(go.Bar(x=df_regiao_tratado["datahora"], y=df_regiao_tratado["internacoes_ultimo_dia"],text=df_regiao_tratado["internacoes_ultimo_dia"],marker_color='#db261f'),)
fig10.update_layout(
    yaxis=dict(ticks="outside", gridcolor='#f1f1f1',showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    xaxis=dict(showline=True,showticklabels=True,linewidth=2,linecolor='rgb(204, 204, 204)'),
    title='Internações Confirmadas',
    font=dict(family='Gill Sans, sans-serif',size=12,color='#1f1b18'),
    yaxis_title='Nº Internados',
    plot_bgcolor='white',
    title_x = 0.5,
    autosize=True,
    margin = dict(l=5, r=0, t=25, b=5),
    showlegend=False)

# ==================================================================
# Layout
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE],title='SPanel | COVID-19',update_title="Iniciando...")
app.layout = dbc.Container([
    # Linha 1 - Cabeçario
    dbc.Row([
        # Dados e logotipo
        dbc.Col([
            html.Div([
                html.H6("COVID19", style={"color": "#db261f", "font-weight": "bold", "margin-top": "20px"}),
                html.Img(id="logo", src="assets/logospanel3.png", width=115, style={"margin-top": "-10px"}),
                html.H6("Estado de São Paulo", style={"color": "#a6a6a6"})
            ],id="cabecario")
        ],md=6,style={"margin-left": "5px","margin-right": "-10px"})
        # Modal do Dicas
        , dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Button("Dicas", id="open-modalFaq", className="bt-sobre", n_clicks=0, color="link",
                               style={"margin-bottom": "-10px"}),
                    dbc.Modal([
                        dbc.ModalHeader("DICAS", style={"color": "#1f1b18", "font-weight": "bold","background-color":"#f1f1f1"}),
                        dbc.ModalBody([
                                dbc.Card([
                                    dbc.CardHeader(
                                        html.H2(
                                            dbc.Button(children=(html.Img(src="assets/covid-button.png", width=60, style={'justify-content': 'center','padding-right':'10px'}),
                                                "O que é COVID-19?"),
                                                color="link",
                                                id="group-1-toggle",
                                                n_clicks=0,
                                                className="faqtitulo"
                                            )
                                        )
                                    ),
                                dbc.Collapse(
                                    dbc.CardBody(html.Div([html.H4("A COVID-19 é uma doença causada pelo coronavírus, nomeado SARS-CoV-2, que apresenta um sinal clínico variando de infecções, com quadros graves e assintomáticos."),
                                                          html.H4("De acordo com a OMS (organização mundial de saúde), a maioria dos pacientes com COVID-19 podem ser assintomáticos ou apresentar poucos sintomas, em média 20% dos casos detectados necessitam de atendimento hospitalar, por causar dificuldade respiratória, dos quais 5% podem necessitar de suporte de ventilação mecânica.")
                                                          ])),
                                    id="collapse-1",
                                    is_open=False,
                                    className="faqconteudo"
                                ),
                            ],className="cardmodal"),
                                dbc.Card([
                                    dbc.CardHeader(
                                        html.H2(
                                            dbc.Button(children=(html.Img(src="assets/transmissao-button.png", width=60, style={'justify-content': 'center','padding-right':'10px'}),
                                                "Como se transmite?"),
                                                color="link",
                                                id="group-2-toggle",
                                                n_clicks=0,
                                                className="faqtitulo"
                                            )
                                        )
                                    ),
                                    dbc.Collapse(
                                        dbc.CardBody(html.Div([html.H4("• A transmissão é feita por contato: ou seja, por meio do contato direto com uma pessoa infectada – exemplo: com um aperto de mão seguido do toque nos olhos, nariz ou boca, ou com objetos e superfícies contaminadas;"),
                                                          html.H4("• A transmissão por gotículas: por meio da exposição a gotículas respiratórias expelidas, contendo vírus, por uma pessoa infectada quando ela tosse ou espirra, principalmente quando ela se encontra a menos de 1 metro de distância da outra;")
                                                          ,html.H4("• A transmissão por aerossol: por meio de gotículas respiratórias menores (aerossóis) contendo vírus e que podem permanecer suspensas no ar, serem levadas por distâncias maiores que 1 metro e por períodos mais longos - geralmente horas.")
                                                          ,html.H4("A maioria das infecções se espalha por contato próximo - menos de 1 metro -, principalmente por meio de gotículas respiratórias.")
                                                          ])),
                                        id="collapse-2",
                                        is_open=False,
                                        className="faqconteudo"
                                    ),
                                ], className="cardmodal"),
                                dbc.Card([
                                    dbc.CardHeader(
                                        html.H2(
                                            dbc.Button(children=(html.Img(src="assets/sintomas-button.png", width=60, style={'justify-content': 'center','padding-right':'10px'}),
                                                "Quais os sintomas?"),
                                                color="link",
                                                id="group-3-toggle",
                                                n_clicks=0,
                                                className="faqtitulo"
                                            )
                                        )
                                    ),
                                dbc.Collapse(
                                    dbc.CardBody(html.Div([html.H4("• Caso assintomático: mesmo com o teste laboratorial positivo para covid-19 não apresentam sintomas."),
                                                          html.H4("• Caso leve: indicado pela aparição de sintomas não específicos, como tosse, dor de garganta ou coriza, seguido, ou não, de perda de olfato e paladar, diarreia, dor abdominal, febre, calafrios, mialgia, fadiga e/ou cefaleia;")
                                                          ,html.H4("• Caso moderado: os sintomas mais presentes podem apresentar sinais leves, como tosse persistente e febre persistente diária, até sinais de piora progressiva de outro sintoma relacionado à covid-19 (fraqueza, debilidade física, falta de apetite, diarreia), além da presença de pneumonia sem sinais ou sintomas de gravidade.")
                                                          ,html.H4("• Caso grave: ou a Síndrome Respiratória Aguda Grave (Síndrome Gripal que apresente dificuldade para respirar, desconforto respiratório ou pressão persistente no peito ou saturação de oxigênio menor que 95% em ar ambiente ou coloração azulada de lábios ou rosto.")
                                                          ,html.H4("• Caso crítico: os principais sintomas são infecção, síndrome do desconforto respiratório agudo, deficiência respiratória grave, mal funcionamento de múltiplos órgãos, pneumonia grave, necessidade de suporte respiratório mecânico e internações em UTI (unidades de terapia intensiva).")
                                                          ,html.H4("• As crianças apresentam como os principais sintomas como: aceleração do ritmo respiratório, baixa saturação de oxigenação no sangue, desconforto respiratório, alteração da consciência, desidratação, dificuldade para se alimentar, coloração azulada, letargia, convulsões, recusa alimentar.")
                                                          ])),
                                    id="collapse-3",
                                    is_open=False,
                                    className="faqconteudo"
                                ),
                            ],className="cardmodal"),
                            dbc.Card([
                                    dbc.CardHeader(
                                        html.H2(
                                            dbc.Button(children=(html.Img(src="assets/prev-button.png", width=60, style={'justify-content': 'center','padding-right':'10px'}),
                                                "Qual a prevenção?"),
                                                color="link",
                                                id="group-4-toggle",
                                                n_clicks=0,
                                                className="faqtitulo"
                                            )
                                        )
                                    ),
                                dbc.Collapse(
                                    dbc.CardBody(html.Div([html.H4("As medidas indicadas, estão as não farmacológicas (conjunto de intervenções que visam maximizar o funcionamento cognitivo e o bem-estar da pessoa, bem como ajudá-la no processo de adaptação à doença), como distanciamento social, etiqueta respiratória e de higienização das mãos, uso de máscaras, limpeza e desinfeção de ambientes, isolamento de casos suspeitos e confirmados e quarentena dos contatos dos casos de covid-19, conforme orientações médicas."),
                                                          html.H4("Também é recomendada a vacinação contra a covid-19 dos grupos prioritários conforme o Plano Nacional de Operacionalização da Vacinação.")
                                                          ])),
                                    id="collapse-4",
                                    is_open=False,
                                    className="faqconteudo"
                                ),
                            ],className="cardmodal")

                        ],style={"background-color":"#f1f1f1"}),
                        dbc.ModalFooter([
                            dbc.Button(
                                "Fechar",
                                id="close-modalFaq",
                                className="bt_close_modal",
                                n_clicks=0)
                        ],style={"background-color":"#f1f1f1"}),
                    ],
                        id="body-modalFaq",
                        scrollable=True,
                        is_open=False,),
                ],md=11),
                # Modal do Sobre
                dbc.Col([
                    dbc.Button("Sobre", id="open-modal",className="bt-sobre", n_clicks=0,color="link",style={"margin-bottom": "-10px","margin-left":"70%"}),
                    dbc.Modal([
                        dbc.ModalHeader("SOBRE O SPANEL",style={"color":"#1f1b18","font-weight": "bold","background-color":"#f1f1f1"}),
                        dbc.ModalBody([
                            html.Div([
                                html.H6("Introdução",style={"color":"#1f1b18","font-weight": "bold"}),
                                html.H4("O SPanel foi desenvolvido para a visualização ágil e simplificada dos dados do COVID-19 no Estado de São Paulo e seus respectivos Municípios.",style={"color":"#3B332D"}),

                                html.H6("Limitações",style={"color":"#1f1b18","font-weight": "bold","padding-top":"10px"}),
                                html.H4("Levando em consideração a pluralidade em relação a infraestrutura ao estado e municípios, "
                                        "poderá haver mudanças aos números em decorrência de erros ou atrasos ao repasse de informações.",style={"color":"#3B332D"}),

                                html.H5("Conceitos básicos:",style={"color":"#1f1b18","font-weight": "bold","padding-top":"10px"}),
                                html.H6("Imunizados",style={"color":"#1f1b18","font-weight": "bold"}),
                                html.H4("O número de imunizados, é feito pela soma da população que já efetuou a vacinação da dose "
                                        "única e da segunda dose das vacinas disponibilizadas pelo Governo do Estado de São Paulo.",style={"color":"#3B332D"}),

                                html.H6("Casos Acumulados",style={"color":"#1f1b18","font-weight": "bold","padding-top":"10px"}),
                                html.H4("O número total de casos confirmados por COVID-19, foi disponibilizado pelo Estado de São Paulo em relação ao dia anterior.",style={"color":"#3B332D"}),

                                html.H6("Novos casos no período",style={"color":"#1f1b18","font-weight": "bold","padding-top":"10px"}),
                                html.H4("O número de novos casos no período por COVID-19, foi disponibilizado pelo Estado de São Paulo em relação ao dia anterior realizando a soma dos dias definidos pelo usuario.",style={"color":"#3B332D"}),

                                html.H6("Óbitos Acumulados", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.H4("O número de óbitos acumulados por COVID-19, foi disponibilizado pelo Estado de São Paulo em relação ao dia anterior.",style={"color":"#3B332D"}),

                                html.H6("Novos óbitos no período", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.H4("O número de novos óbitos no período por COVID-19, foi disponibilizado pelo Estado de São Paulo em relação ao dia anterior realizando a soma dos dias definidos pelo usuario",style={"color": "#3B332D"}),

                                html.H6("População", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.H4("O número da população, foi disponibilizado pelo Estado de São Paulo e pode conter uma divergência com a realiadade.",
                                    style={"color": "#3B332D"}),

                                html.H5("Indicadores básicos:", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.H6("Porcentagem Imunizados", style={"color": "#1f1b18", "font-weight": "bold"}),
                                html.H4("A porcentagem de imunizados é dada pelo total de população do estado de São Paulo e seus respectivos municípios, e pelo total de imunizados até o presente momento.",
                                    style={"color": "#3B332D"}),

                                html.H6("Taxa de Letalidade", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.H4("A taxa de letalidade por COVID-19, é feita pelo número de óbitos confirmados em relação, ao total de casos confirmados pelos cidadãos residentes no Estado de São Paulo e seus respectivos Municípios.",
                                    style={"color": "#3B332D"}),

                                html.H5("Fonte", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.A("https://www.saopaulo.sp.gov.br/planosp/simi/dados-abertos/", href='https://www.saopaulo.sp.gov.br/planosp/simi/dados-abertos/', target="_blank",className="bt-link"),

                                # html.Div([
                                # dbc.Button("ARQUIVO .CSV", id="btn_csv",className='bt_close_modal',color="danger",style={"margin-top":"15px"}),
                                # dcc.Download(id="download-dataframe-csv")])
                            ])],style={"background-color":"#f1f1f1"}),
                        dbc.ModalFooter([
                            dbc.Button(
                                "Fechar",
                                id="close-modal",
                                className="bt_close_modal",
                                n_clicks=0)
                        ],style={"background-color":"#f1f1f1"}),
                    ],
                    id="body-modal",
                    scrollable=True,
                    is_open=False),
                ],md=1)
            ],justify='end'),
            dbc.Row([
                # Date Picker
                dbc.Col([
                    html.Div(id="div-test", children=[
                        dcc.DatePickerRange(
                            id="datepicker-range",
                            start_date="2021-01-01",
                            end_date=df_tratado["datahora"].max(),
                            initial_visible_month=df_tratado['datahora'].max(),
                            minimum_nights=1,
                            min_date_allowed=df_tratado["datahora"].min(),
                            max_date_allowed=df_tratado["datahora"].max(),
                            display_format='DD/MM/YY',
                            style={"margin-left": "inherit", "border": "0px solid black"})
                    ], style={"margin-top": "25px"})
                ],md=6),
                # Dropdown de Municipios
                dbc.Col([
                    html.Div([
                        dcc.Dropdown(id="location-dropdown",className="location-dropdown",
                                     options=[{"label": i, "value": i} for i in list_municipios]
                                     ,clearable=True,placeholder="Escolha um município",
                                     style={"background-color": "#1f1b18"}
                                     )
                    ],style={"margin-top": "25px"})
                ],md=4,style={"margin-left": "-11%"})
            ],justify='end')
        ],md=6)
    ], style={"background-color": "#1f1b18"})

# ==================================================================
    # Linha 2 - Vacinados, Casos, Obitos e População
    ,dbc.Row([
        # Coluna 1 - Vacinados
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H5("Imunizados", style={"color": "#f1f1f1"}),
                            html.H1(style={"color": "#f1f1f1"},
                                    id="imunizados-text")
                        ],md=10),
                        dbc.Col([
                            dbc.Button(children=[html.Img(src="assets/information-button.png", width=7, style={'justify-content': 'center'})],
                                       id="hover-target",
                                       className="button",
                                       n_clicks=0)
                            ,dbc.Popover([
                                dbc.PopoverBody([html.H6("Imunizados",style={"font-weight": "bold"}),
                                    html.H6("Os dados imunizados, foram obtidos através de uma soma entre os que tomaram a vacina de dose unica e os que tomaram a segunda dose."),
                                    html.H6("Porcentagem Imunizados",style={"font-weight": "bold"}),
                                    html.H6("A porcentagem foi obtida com base nos imunizados(dose unica + segunda dose) por população.")
                                                 ])
                            ]
                                ,id="hover",
                                target="hover-target",
                                trigger="hover")
                        ],md=2)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.H6(" 1ª Dose ", style={"color": "#f1f1f1", "font-weight": "bold"}),
                            html.H2(style={"color": "#f1f1f1"},
                            id="primeiradose-text")
                        ],md=7),
                        dbc.Col([
                            html.H6("% Imunizados", style={"color": "#f1f1f1", "font-weight": "bold"}),
                            html.H2(style={"color": "#f1f1f1"},
                            id="porcentagemimunizados-text")
                        ],md=5)
                    ])
                ])
            ],className='cardsteste',style={"margin-left": "5px"})
        ], md=3),
        # Coluna 2 - Casos
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H5("Casos Acumulados", style={"color": "#db261f"}),
                            html.H1(style={"color": "#1f1b18"},
                                    id="acumulados-text"),
                        ],md=10),
                        dbc.Col([
                            dbc.Button(children=[html.Img(src="assets/information-button3.png", width=7, style={'justify-content': 'center'})],
                                       id="hover-target3",
                                       className="buttonred",
                                       n_clicks=0)
                            ,dbc.Popover([
                                dbc.PopoverBody([html.H6("Casos Acumulados",style={"font-weight": "bold"}),
                                    html.H6("Os casos acumulados, são a soma do primeiro caso da pandemia até o último período determinado no calendário pelo usuário."),
                                    html.H6("Novos casos no período",style={"font-weight": "bold"}),
                                    html.H6("Novos casos no período, são a soma do primeiro dia selecionado no calendário pelo usuário, até o último período determinado no calendário pelo usuário.")
                                                 ])
                            ]
                                ,id="hover3",
                                target="hover-target3",
                                trigger="hover")
                        ],md=2)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.H6("Novos casos no período", style={"color": "#db261f", "font-weight": "bold"}),
                            html.H2(style={"color": "#1f1b18"},
                                    id="novoscasos-text"),
                        ],md=12)
                    ])
                ])
            ], color="#ffffff",className='cards',style={"margin-left": "2.5px"})
        ], md=3),
        # Coluna 3 - Obitos
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H5("Óbitos Acumulados", style={"color": "#db261f"}),
                            html.H1(style={"color": "#1f1b18"},
                                    id="obacumulados-text"),
                        ],md=10),
                        dbc.Col([
                            dbc.Button(children=[html.Img(src="assets/information-button3.png", width=7, style={'justify-content': 'center'})],
                                       id="hover-target4",
                                       className="buttonred",
                                       n_clicks=0)
                            ,dbc.Popover([
                                dbc.PopoverBody([html.H6("Óbitos Acumulados",style={"font-weight": "bold"}),
                                    html.H6("Os óbitos acumulados, são a soma do primeiro óbito da pandemia até o último período determinado no calendário pelo usuário."),
                                    html.H6("Novos óbitos no período",style={"font-weight": "bold"}),
                                    html.H6("Novos óbitos no período, são a soma do primeiro dia selecionado no calendário pelo usuário, até o último período determinado no calendário pelo usuário.")
                                                 ])
                            ]
                                ,id="hover4",
                                target="hover-target4",
                                trigger="hover")
                        ],md=2)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.H6("Novos óbitos no período", style={"color": "#db261f", "font-weight": "bold"}),
                            html.H2(style={"color": "#1f1b18"}, id="novosob-text")
                        ],md=12)
                    ])
                ])
            ], color="#ffffff",className='cards',style={"margin-right": "2.5px"})
        ], md=3),
        # Coluna 4 - População
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H5('População', style={"color": "#b7b7b7"}),
                            html.H1(style={"color": "#f1f1f1"},
                                    id="populacao-text"),
                        ],md=10),
                        dbc.Col([
                            dbc.Button(children=[html.Img(src="assets/information-button2.png", width=7, style={'justify-content': 'center'})],
                                       id="hover-target2",
                                       className="button",
                                       n_clicks=0)
                            ,dbc.Popover([
                                dbc.PopoverBody([html.H6("População",style={"font-weight": "bold"}),
                                    html.H6("Os dados POPULAÇÃO, foram retirados no site do Estado de São Paulo e pode conter uma pequena divergencia com a atualidade."),
                                    html.H6("Letalidade",style={"font-weight": "bold"}),
                                    html.H6("A letalidade, foi obtido com base nos óbitos por casos.")
                                                 ])
                            ]
                                ,id="hover2",
                                target="hover-target2",
                                trigger="hover")
                        ],md=2)
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.H6('% Letalidade', style={"color": "#b7b7b7", "font-weight": "bold"}),
                            html.H2(style={"color": "#f1f1f1"},
                                id="letalidade-text")
                        ],md=12)
                    ])
                ])
            ],className='cardsteste2',style={"margin-right": "5px"})
        ], md=3)
    ], style={"background-image": "linear-gradient(#1f1b18 50%, #f1f1f1 50%)"})
    # Graficos - Imunizados
    ,dbc.Row([
        dbc.Col([
            dcc.Markdown(['''>
        > Imunizados
        >'''], className="lb_imunizados",style={'margin-top':'30px','margin-left':'10px'})
        ])
    ])
    ,dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="vacinas-graph",className = 'graph1')
                ])
            ],className="cardgraph")
        ], md=6)
        ,dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="vacinas-graph2", className='graph2')
                ])
            ],className="cardgraph2")
        ], md=6)
    ])
    # Graficos - Casos Confirmados
    ,dbc.Row([
        dbc.Col([
            dcc.Markdown(['''>
            > Casos Confirmados
            >'''],className="lb_imunizados",style={'margin-top':'40px','margin-left':'10px'})
        ])
    ])
    , dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="casos-graph", className='graph1')
                ])
            ],className="cardgraph")
        ], md=6)
        , dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="casosnovos-graph", className='graph2')
                ])
            ],className="cardgraph2")
        ], md=6)
    ])
    # Graficos - Óbitos Confirmados
    ,dbc.Row([
        dbc.Col([
            dcc.Markdown(['''>
        > Óbitos Confirmados
        >'''], className="lb_imunizados",style={'margin-top':'40px','margin-left':'10px'})
        ])
    ])
    , dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="obitos-graph", className='graph1')
                ])
            ],className="cardgraph")
        ], md=6)
        , dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="obitosnovos-graph", className='graph2')
                ])
            ],className="cardgraph2")
        ], md=6)
    ])
    # Graficos - População
    ,dbc.Row([
        dbc.Col([
            dcc.Markdown(['''>
        > População
        >'''], className="lb_imunizados",style={'margin-top':'40px','margin-left':'10px'})
        ])
    ])
    , dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="letalidade-graph", className='graph1')
                ])
            ],className="cardgraph")
        ], md=6)
        , dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="mortes-graph2", className='graph2')
                ])
            ],className="cardgraph2")
        ], md=6)
    ])
    # Tabela
    , dbc.Row([
        dbc.Col([
            dcc.Markdown(['''>
    > Tabela de Visualização
    >'''], className="lb_imunizados", style={'margin-top': '40px', 'margin-left': '10px'})
        ])
    ])
    , dbc.Row([
        dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                         dcc.Dropdown(
                                id='demo-dropdown',className="demo-dropdown",
                                options=[{"label": i, "value": i} for i in list_municipios2],
                                value=list_tabela,
                                persistence = "ESTADO DE SÃO PAULO",
                                placeholder="Escolha uma localidade",
                                clearable=True,
                                multi=True
                            ),
                        # Tabela
                        dt.DataTable(
                            id='table',
                            data=df_tratado_rename.to_dict('records'),
                            columns=[{"name": i, "id": i} for i in (df_tratado_rename.columns)],
                            style_table={'overflowY': 'auto', 'height': '300px'},
                            style_cell={'minWidth': '95px', 'width': '180px', 'maxWidth': '180px', 'whiteSpace': 'auto',
                                        'height': 'auto'},
                            editable=False,
                            sort_action="native",
                            sort_mode="single",
                            row_deletable=False,
                            selected_columns=[],
                            selected_rows=[],
                            page_current=0,
                            page_action="native",
                            fixed_rows={'headers': True},
                            style_header={"color": "#f1f1f1", "background-color": "#1f1b18",
                                          'font-family': 'Gill Sans, sans-serif', "font-weight": "bold"},
                            style_data={"color": "#3B332D", 'font-family': 'Gill Sans, sans-serif',
                                        'border': '1px solid grey', 'whiteSpace': 'normal'},
                            style_data_conditional=[
                                {
                                    'if': {
                                        'filter_query': '{Localização} contains "ESTADO DE SÃO PAULO"'

                                    },
                                    'backgroundColor': '#db261f',
                                    'color': 'white'
                                },

                            ],
                            tooltip_delay=0,
                            tooltip_duration=None)
                        ])
                    ],className='card-tabela')
            ])
        ])
    # Macroregioes
    , dbc.Row([
        dbc.Col([
            dcc.Markdown(['''>
        > Outros Dados
        >'''], className="lb_imunizados", style={'margin-top': '40px', 'margin-left': '10px'})
        ])
    ])
    ,dbc.Row([
        dbc.Col([
             html.Div(
                [
                    dbc.Button("Dep. Regionais de Saúde", id="open-xl", n_clicks=0, style={'margin-top': '20px', 'margin-left':'25px'}, className='bt_departamentos'),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Departamentos Regionais de Saúde",
                                            style={"color": "#1f1b18", "font-weight": "bold",
                                                   "background-color": "#f1f1f1"})
                            ,dbc.ModalBody(
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Row([
                                            dbc.Col([
                                                dcc.Dropdown(
                                                    id='demo-reg', className="reg-dropdown",
                                                    options=[{"label": i, "value": i} for i in list_drs],
                                                    value="Estado de São Paulo",
                                                    placeholder="Escolha uma localidade",
                                                    clearable=False),
                                                ],md=10),
                                            dbc.Col([
                                                dbc.Button(children=[
                                                    html.Img(src="assets/information-button3.png", width=7,
                                                             style={'justify-content': 'center'})],
                                                           id="focus-target",
                                                           className="buttondrs",
                                                           n_clicks=0)
                                            ],md=2)
                                        ]),
                                            dbc.Popover(
                                                dbc.PopoverBody(
                                                    [html.H5("Cidades da Região", style={"font-weight": "bold"}),
                                                     html.H4('', style={"color": "black", "align": "right"},
                                                             id="drs-popover",
                                                             )
                                                 ]),
                                                id="focus",
                                                target="focus-target",
                                                trigger="hover",
                                            ),
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.H5("Ocupação de leitos", style={"color": "#f1f1f1"}),
                                                            html.H1(style={"color": "#f1f1f1"},
                                                                id="ocupacao_leitos_ultimo_dia")
                                                        ])
                                                    ]),
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.H6("Ocupação de leitos últimos 7 dias", style={"color": "#f1f1f1"}),
                                                            html.H2(style={"color": "#f1f1f1"},
                                                                id="ocupacao_leitos")
                                                        ])
                                                    ])
                                                ])
                                            ],className='cardsdep'),
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.H5("Leitos de UTI para a COVID",
                                                                style={"color": "#f1f1f1"}),
                                                            html.H1(style={"color": "#f1f1f1"},
                                                                id="total_covid_uti_ultimo_dia")
                                                        ])
                                                    ])
                                                ])
                                            ],className='cardsdep'),
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.H5("Internações confirmadas/ suspeita",
                                                                style={"color": "#f1f1f1"}),
                                                            html.H1(style={"color": "#f1f1f1"},
                                                                id="internacoes_ultimo_dia")
                                                        ])
                                                    ]),
                                                     dbc.Row([
                                                         dbc.Col([
                                                            html.H6("Internações nos últimos 7 dias", style={"color": "#f1f1f1"}),
                                                            html.H2(style={"color": "#f1f1f1"},
                                                                id="internacoes_7d")
                                                        ])
                                                    ])
                                                ])
                                            ],className='cardsdep'),
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.H5("População", style={"color": "#f1f1f1"}),
                                                            html.H1(style={"color": "#f1f1f1"},
                                                                        id="pop")
                                                        ])
                                                    ])
                                                ])
                                            ],className='cardsdep'),
                                    ],md=4),
                                    dbc.Col([
                                        dbc.Row([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dcc.Graph(id="cardgraph-drs1", className='graphdrs')
                                                ])
                                            ], className="cardgraph-drs")
                                        ]),
                                        dbc.Row([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dcc.Graph(id="cardgraph-drs", className='graphdrs')
                                                ])
                                            ], className="cardgraph-drs")
                                        ])
                                    ],md=8),
                                ])
                            ),
                        ],
                        id="modal-xl",
                        size="xl",
                        is_open=False,
                        scrollable=True,
                    ),
                    dbc.Modal(
                        [
                            dbc.ModalHeader("Transparência ",
                                            style={"color": "#1f1b18", "font-weight": "bold",
                                                   "background-color": "#f1f1f1"}),
                            dbc.ModalBody("An extra large modal."),
                        ],
                        id="modal-xl1",
                        size="xl",
                        is_open=False,


                    ),
                ]
            ),
        ])
    ])
    ,dbc.Row([
        dcc.Link(children=html.Img(id="im-telegram", src="assets/imagemtelegram.png", width='100%',
                                   style={'display': 'block', 'margin-top': '40px', 'margin-left': '30px',
                                          'padding-right': '60px'}), href='https://t.me/Fluffyapi_bot',refresh=True)
    ])
    ,dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Row([
                    html.H6("Painel de COVID-19 do Estado de São Paulo | ©Fluffy2021",style={"color":"#1f1b18","margin-top":"30px",'text-align': 'center'}),
                ],style={'display': 'block','margin-left': 'auto','margin-right': 'auto'}),
                dbc.Row([
                    dcc.Link(children=html.Img(id="github-button", src="assets/github-button.png", width=25, style={'position': 'absolute',"margin-top": "3px",'left': '48%','margin-right': '-53%'}),href='https://github.com/fluffyfatec/SPanel',
                         refresh=True),
                    dcc.Link(children=html.Img(id="instagram-button", src="assets/instagram-buttom.png", width=25, style={'position': 'absolute',"margin-top": "3px",'left': '50%','margin-right': '-50%'}),href='https://www.instagram.com/fluffyapi/',
                         refresh=True),
                    dcc.Link(children=html.Img(id="email-button", src="assets/email-button.png", width=25, style={'position': 'absolute',"margin-top": "3px",'left': '52%','margin-right': '-48%'}),href='fluffyfatec@gmail.com',
                         refresh=True)
                ],style={"margin-bottom":"3%"})
            ])
        ])
    ],style={"justify-content": "center"})
], fluid=True,style={"background-color": "#f1f1f1"})

# ==================================================================
# Interatividade

# ==================================================================
# Cards
@app.callback(
    [
        Output("imunizados-text", "children"),
        Output("primeiradose-text", "children"),
        Output("porcentagemimunizados-text", "children"),
        Output("acumulados-text", "children"),
        Output("novoscasos-text", "children"),
        Output("obacumulados-text", "children"),
        Output("novosob-text", "children"),
        Output("populacao-text", "children"),
        Output("letalidade-text", "children")
    ],
    [Input("location-dropdown", "value"),
     Input("datepicker-range", "start_date"),
     Input("datepicker-range", "end_date")]
)
# Chamada dos dados do CSV - Se Dropdown for vazio chama os dados do estado, senão chama os dados do municipio selecionado
def display_status(location, start_date,end_date):
    if not location:
        df_data_var_date = df_estadotratado[(df_estadotratado['datahora'] >= start_date) & (df_estadotratado['datahora'] <= end_date)]
        df_data_on_date = df_estadotratado[(df_estadotratado["datahora"] == end_date)]
        df_data_vacinastratado = df_vacinastratado.assign(doseunica=df_vacinastratado["doseunica"].sum())
        df_data_vacinastratado = df_data_vacinastratado.assign(primeiradose=df_data_vacinastratado["primeiradose"].sum())
        df_data_vacinastratado = df_data_vacinastratado.assign(segundadose=df_data_vacinastratado["segundadose"].sum())
        df_data_vacinastratado = df_data_vacinastratado.assign(pop=df_data_vacinastratado["pop"].sum())
        df_data_vacinastratado = df_data_vacinastratado.assign(Imunizados=df_data_vacinastratado['doseunica'] + df_data_vacinastratado['segundadose'])  # SOMAR PARA TRAZER ESTADO DE SP
        df_data_vacinastratado = df_data_vacinastratado.assign(porcentagemimunizados=df_data_vacinastratado['Imunizados'] / df_data_vacinastratado['pop'] * 100)
        decimals = 2
        df_data_vacinastratado['porcentagemimunizados'] = df_data_vacinastratado['porcentagemimunizados'].apply(lambda x: round(x, decimals))
        df_data_on_date = df_data_on_date.assign(letalidade=df_data_on_date['obitos'] / df_data_on_date['casos'] * 100)
        df_data_on_date['letalidade'] = df_data_on_date['letalidade'].apply(lambda x: round(x, decimals))
    else:
        df_data_var_date = df_tratado[(df_tratado["nome_munic"] == location)]
        df_data_vacinastratado = df_vacinastratado[(df_vacinastratado["nome_munic"] == location)]
        df_data_var_date = df_data_var_date[(df_data_var_date['datahora'] >= start_date) & (df_data_var_date['datahora'] <= end_date)]
        df_data_on_date = df_data_var_date[(df_data_var_date["datahora"] == end_date)]
        df_data_var_date = df_data_var_date.assign(obitos_novos=df_data_var_date['obitos_novos'].sum())
        df_data_var_date = df_data_var_date.assign(casos_novos=df_data_var_date['casos_novos'].sum())
        df_data_vacinastratado = df_data_vacinastratado.assign(Imunizados=df_data_vacinastratado['doseunica'] + df_data_vacinastratado['segundadose'])  # SOMAR PARA TRAZER ESTADO DE SP
        df_data_vacinastratado = df_data_vacinastratado.assign(porcentagemimunizados=df_data_vacinastratado['Imunizados'] / df_data_vacinastratado['pop'] * 100)
        decimals = 2
        df_data_vacinastratado['porcentagemimunizados'] = df_data_vacinastratado['porcentagemimunizados'].apply(lambda x: round(x, decimals))
        df_data_on_date = df_data_on_date.assign(letalidade=df_data_on_date['obitos'] / df_data_on_date['casos'] * 100)
        df_data_on_date['letalidade'] = df_data_on_date['letalidade'].apply(lambda x: round(x, decimals))

# Filtrando caso os dados sejam vazios e trocando ',' por '.'
    imunizados = "-" if df_data_vacinastratado["Imunizados"].isna().values[0] else f'{int(df_data_vacinastratado["Imunizados"].values[0]):,}'.replace(",", ".")
    primeiradose = "-" if df_data_vacinastratado["primeiradose"].isna().values[0] else f'{int(df_data_vacinastratado["primeiradose"].values[0]):,}'.replace(",", ".")
    porcentagemimunizados = "-" if df_data_vacinastratado["porcentagemimunizados"].isna().values[0] else f'{float(df_data_vacinastratado["porcentagemimunizados"].values[0]):,}'.replace(",", ".")
    acumulados_novos = "-" if df_data_on_date["casos"].isna().values[0] else  f'{int(df_data_on_date["casos"].values[0]):,}'.replace(",", ".")
    novos_caso = "-" if df_data_var_date["casos_novos"].isna().values[0] else f'{int(df_data_var_date["casos_novos"].values[0]):,}'.replace(",", ".")
    obacumulados_novos = "-" if df_data_on_date["obitos"].isna().values[0] else f'{int(df_data_on_date["obitos"].values[0]):,}'.replace(",", ".")
    novos_ob = "-" if df_data_var_date["obitos_novos"].isna().values[0] else f'{int(df_data_var_date["obitos_novos"].values[0]):,}'.replace(",", ".")
    populacao = "-" if df_data_on_date["pop"].isna().values[0] else f'{int(df_data_on_date["pop"].values[0]):,}'.replace(",", ".")
    letalidade = "-" if df_data_on_date["letalidade"].isna().values[0] else f'{float(df_data_on_date["letalidade"].values[0]):,}'.replace(",", ".")

# Retorno dos dados nos cards do layout
    return (imunizados,
            primeiradose,
            f'{porcentagemimunizados}%',
            acumulados_novos,
            novos_caso,
            obacumulados_novos,
            novos_ob,
            populacao,
            f'{letalidade}%')


#====================================================================
# Chamada Tabela

@app.callback(
    Output("table", "data"),
    Input("demo-dropdown", "value")
)
def update_table(location):

    if location is not None:
        date_column = df_tratado_rename["Data da Atualização"]
        max = date_column.max()
        row = df_tratado_rename.loc[df_tratado_rename["Data da Atualização"] == max]
        df_municipios = row[row["Localização"].isin(location)]
        df_loc = df_municipios.to_dict('records')
        return df_loc

# ==================================================================
# Chamada graficos

# ==================================================================
# Grafico Vacinas Aplicadas
@app.callback(
    Output("vacinas-graph", "figure"),
    [
    Input("location-dropdown", "value")
    ]
)
def display_vacinas(location):

    if not location:
        soma_unica = df_vacinastratado['doseunica'].sum()
        soma_terceira = df_vacinastratado['terceiradose'].sum()
        soma_segunda = df_vacinastratado['segundadose'].sum()
        soma_primeira = df_vacinastratado['primeiradose'].sum()

        # Cria um novo DataFrame com os dados que deseja adicionar
        novos_dados = pd.DataFrame({
            'nome_munic': ['Estado'],
            'Dose': ['UNICA'],
            'Total Doses Aplicadas': [soma_unica]
        })

        # Concatena o novo DataFrame ao DataFrame original
        df_data_vacinas = pd.concat([df_vacinas, novos_dados], ignore_index=True)

    else:
        df_data_vacinas = df_vacinas[df_vacinas["nome_munic"] == location]

    fig0.update_traces(go.Bar(x=df_data_vacinas["Total Doses Aplicadas"], y=df_data_vacinas["Dose"],text=df_data_vacinas["Total Doses Aplicadas"],marker_color='#db261f'))
    return (
        fig0
    )
# ==================================================================
# Grafico Vacinas Aplicadas
@app.callback(
    Output("vacinas-graph2", "figure"),
    [
    Input("location-dropdown", "value")
    ]
)
def display_imunizados(location):
    df_vacinastratado = pd.read_csv('docs/df_vacinastratado.csv')
    if not location:
        df_data_imunizados1 = df_vacinastratado["segundadose"].sum()
        df_data_imunizados2 = df_vacinastratado["doseunica"].sum()
        df_data_imunizados3 = (df_data_imunizados2 + df_data_imunizados1)
        df_nao_imunizados2 = (44639899 - df_data_imunizados3)
        labels = ['Não Imunizados','Imunizados']
        values = [(df_nao_imunizados2), (df_data_imunizados3)]
    else:
        df_vacinastratado = df_vacinastratado[df_vacinastratado['nome_munic'] == location]
        pop = df_vacinastratado['pop'].values[0]

        df_data_imunizados = df_vacinas[df_vacinas["nome_munic"] == location]
        df_data_imunizados.loc[-1] = [location, 'pop', pop]
        df_data_imunizados = df_data_imunizados.sort_index()
        df_data_imunizados.index = df_data_imunizados.index + 1

        df_data_imunizadosunica = df_data_imunizados[df_data_imunizados['Dose'] == 'UNICA']
        df_data_imunizadosunica = df_data_imunizadosunica['Total Doses Aplicadas'].values[0]

        df_data_imunizados2 = df_data_imunizados[df_data_imunizados['Dose'] == '2° DOSE']
        df_data_imunizados2 = df_data_imunizados2['Total Doses Aplicadas'].values[0]

        df_data_imunizadostotal = df_data_imunizados2 + df_data_imunizadosunica
        df_data_imunizados.loc[-1] = [location, 'Imunizados', df_data_imunizadostotal]
        df_data_imunizados = df_data_imunizados.sort_index()
        df_data_imunizados.index = df_data_imunizados.index + 1

        df_data_naoimunizados = df_data_imunizados[df_data_imunizados['Dose'] == 'pop']
        df_data_naoimunizados = df_data_naoimunizados['Total Doses Aplicadas'].values[0]

        df_data_naoimunizados = df_data_naoimunizados - df_data_imunizadostotal
        df_data_imunizados.loc[-1] = [location, 'Não Imunizados', df_data_naoimunizados]
        df_data_imunizados = df_data_imunizados.sort_index()
        df_data_imunizados.index = df_data_imunizados.index + 1
        df_data_imunizados = df_data_imunizados.query("Dose == 'Não Imunizados' | Dose == 'Imunizados'")
        values = df_data_imunizados['Total Doses Aplicadas']
        labels = df_data_imunizados['Dose']
    fig5.update_traces(go.Pie(values=values, labels=labels))
    return(
        fig5
)

# ==================================================================
# Grafico Casos, Obitos e Letalidade
@app.callback(
    [
    Output("casos-graph","figure"),
    Output("casosnovos-graph","figure"),
    Output("obitos-graph","figure"),
    Output("obitosnovos-graph","figure"),
    Output("letalidade-graph","figure")
    ],
    [
    Input("location-dropdown", "value"),
    Input("datepicker-range", "start_date"),
    Input("datepicker-range", "end_date")
    ]
)
def display_graph(location, start_date, end_date):
    if not location:
        df_data_on_location = df_estadotratado[(df_estadotratado['datahora'] >= start_date) & (df_estadotratado['datahora'] <= end_date)]
        df_data_on_acumulado = df_estadotratado[(df_estadotratado['datahora'] >= '2020-01-01') & (df_estadotratado['datahora'] <= end_date)]
        df_data_on_acumulado = df_data_on_acumulado.assign(letalidade=df_data_on_acumulado['obitos'] / df_data_on_acumulado['casos'] * 100)
        decimals = 2
        df_data_on_acumulado['letalidade'] = df_data_on_acumulado['letalidade'].apply(lambda x: round(x, decimals))
    else:
        df_data_on_location = df_tratado[df_tratado["nome_munic"] == location]
        df_data_on_location = df_data_on_location[(df_data_on_location['datahora'] >= start_date) & (df_data_on_location['datahora'] <= end_date)]
        df_data_on_acumulado = df_tratado[df_tratado["nome_munic"] == location]
        df_data_on_acumulado = df_data_on_acumulado[(df_data_on_acumulado['datahora'] >= '2020-01-01') & (df_data_on_acumulado['datahora'] <= end_date)]
        df_data_on_acumulado = df_data_on_acumulado.assign(letalidade=df_data_on_acumulado['obitos'] / df_data_on_acumulado['casos'] * 100)
        decimals = 2
        df_data_on_acumulado['letalidade'] = df_data_on_acumulado['letalidade'].apply(lambda x: round(x, decimals))

    # update graficos
    fig1.update_traces(go.Scatter(x=df_data_on_acumulado["datahora"], y=df_data_on_acumulado["casos"]))
    fig2.update_traces(go.Bar(x=df_data_on_location["datahora"], y=df_data_on_location["casos_novos"],text=df_data_on_location["casos_novos"]))
    fig3.update_traces(go.Scatter(x=df_data_on_acumulado["datahora"], y=df_data_on_acumulado["obitos"]))
    fig4.update_traces(go.Bar(x=df_data_on_location["datahora"], y=df_data_on_location["obitos_novos"],text=df_data_on_location["obitos_novos"]))
    fig6.update_traces(go.Scatter(x=df_data_on_acumulado["datahora"], y=df_data_on_acumulado["letalidade"]))
    return (
        fig1, fig2, fig3, fig4, fig6
    )

# ==================================================================
# Grafico Letalidade Pizza
@app.callback(
    Output("mortes-graph2","figure"),
    [
    Input("location-dropdown","value"),
    Input("datepicker-range", "start_date"),
    Input("datepicker-range", "end_date")
    ]
)
def display_letal(location,start_date,end_date):
    df_tratado = pd.read_csv('docs/df_tratado.csv')
    if not location:
        df_tratado = df_tratado[df_tratado["datahora"]== end_date]
        casos = df_tratado['casos'].sum()
        obitos = df_tratado['obitos'].sum()
        casosobitos = (casos - obitos)
        labels = ['Casos que não vieram a óbito' , 'Casos que vieram a óbito']
        values = [(casosobitos), (obitos)]
    else:
        df_tratado = df_tratado[df_tratado['nome_munic'] == location]
        df_tratado = df_tratado[df_tratado['datahora'] == end_date]

        casos = df_tratado['casos'].values[0]
        obitos = df_tratado['obitos'].values[0]

        df_data_letalidade = df_vacinas[df_vacinas['nome_munic'] == location]
        casosobitos = casos - obitos

        df_data_letalidade.loc[-1] = [location, 'Casos que vieram a óbito', obitos]
        df_data_letalidade = df_data_letalidade.sort_index()
        df_data_letalidade.index = df_data_letalidade.index + 1

        df_data_letalidade.loc[-1] = [location, 'Casos que não vieram a óbito', casosobitos]
        df_data_letalidade = df_data_letalidade.sort_index()
        df_data_letalidade.index = df_data_letalidade.index + 1

        df_data_letalidade = df_data_letalidade.query("Dose == 'Casos que vieram a óbito' | Dose == 'Casos que não vieram a óbito'")
        values = df_data_letalidade['Total Doses Aplicadas']
        labels = df_data_letalidade['Dose']
    fig7.update_traces(go.Pie(values=values, labels=labels))
    return (
        fig7
    )

# ==================================================================
# Grafico Modal Regioes 1
@app.callback(
     Output("cardgraph-drs1", "figure"),
     Input("demo-reg", "value")
)

def display_ocupacao(location):
     if not location:
         df_data_regiao = df_regiao_tratado[df_regiao_tratado['nome_drs'] == 'Estado de São Paulo']
         end_date = df_data_regiao["datahora"].max()
         df_data_regiao = df_data_regiao[df_data_regiao['datahora'] == end_date]
         ocup_leito = df_data_regiao['ocupacao_leitos'].values[0].replace(',','.')
         ocup_leito = float(ocup_leito)
         desocup_leito = 100 - ocup_leito
         labels = ['Leitos Ocupados', 'Leitos Desocupados']
         values = [(ocup_leito), (desocup_leito)]

         ocup_leito_ultimo = df_data_regiao['ocupacao_leitos_ultimo_dia'].values[0].replace(',', '.')
         ocup_leito_ultimo = float(ocup_leito_ultimo)
         desocup_leito_ultimo = 100 - ocup_leito_ultimo
         values2 = [(ocup_leito_ultimo), (desocup_leito_ultimo)]
     else:
         df_data_regiao = df_regiao_tratado[df_regiao_tratado['nome_drs'] == location]
         end_date = df_data_regiao["datahora"].max()
         df_data_regiao = df_data_regiao[df_data_regiao['datahora'] == end_date]
         ocup_leito = df_data_regiao['ocupacao_leitos'].values[0].replace(',','.')
         ocup_leito = float(ocup_leito)
         desocup_leito = 100 - ocup_leito
         labels = ['Leitos Ocupados', 'Leitos Desocupados']
         values = [(ocup_leito), (desocup_leito)]

         ocup_leito_ultimo = df_data_regiao['ocupacao_leitos_ultimo_dia'].values[0].replace(',', '.')
         ocup_leito_ultimo = float(ocup_leito_ultimo)
         desocup_leito_ultimo = 100 - ocup_leito_ultimo
         values2 = [(ocup_leito_ultimo), (desocup_leito_ultimo)]

     fig8.add_trace(go.Pie(values=values, labels=labels, hole=.3, marker=dict(colors=colors2),
                           name="Ultimos 7 Dias"), 1, 2)
     fig8.add_trace(go.Pie(values=values2, labels=labels, hole=.3, marker=dict(colors=colors2),
                           name="Ultimo Dia"), 1, 1)
     return (
         fig8
     )

# # ==================================================================
#Gráfico Região 3
@app.callback(
     Output("cardgraph-drs", "figure"),
     Input("demo-reg", "value")
)
def display_ocupacao(location):
     if not location:
         pass
     else:
         df_data_regiao = df_regiao_tratado[df_regiao_tratado['nome_drs'] == location]

     fig10.update_traces(go.Bar(x=df_data_regiao["datahora"], y=df_data_regiao['internacoes_ultimo_dia'],text=df_data_regiao["internacoes_ultimo_dia"]))
     return (
         fig10
     )


# Chamada do modal SOBRE
@app.callback(
    Output("body-modal", "is_open"),
    [
        Input("open-modal", "n_clicks"),
        Input("close-modal", "n_clicks"),
    ],
    [State("body-modal", "is_open")],
)

def toggle_modal(n1,n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# ==================================================================
# Chamada do modal Dicas
@app.callback(
    Output("body-modalFaq", "is_open"),
    [
        Input("open-modalFaq", "n_clicks"),
        Input("close-modalFaq", "n_clicks"),
    ],
    [State("body-modalFaq", "is_open")],
)

def toggle_modalFaq(n1,n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    [Output(f"collapse-{i}", "is_open") for i in range(1, 5)],
    [Input(f"group-{i}-toggle", "n_clicks") for i in range(1, 5)],
    [State(f"collapse-{i}", "is_open") for i in range(1, 5)],
)
def toggle_accordion(n1, n2, n3, n4, is_open1, is_open2, is_open3, is_open4):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "group-1-toggle" and n1:
        return not is_open1, False, False, False
    elif button_id == "group-2-toggle" and n2:
        return False, not is_open2, False, False
    elif button_id == "group-3-toggle" and n3:
        return False, False, not is_open3, False
    elif button_id == "group-4-toggle" and n4:
        return False, False, False, not is_open4
    return False, False, False

# ==================================================================
# Cards DRS
@app.callback(
    [
        Output("ocupacao_leitos", "children"),
        Output("pop", "children"),
        Output("internacoes_7d", "children"),
        Output("total_covid_uti_ultimo_dia", "children"),
        Output("ocupacao_leitos_ultimo_dia", "children"),
        Output("internacoes_ultimo_dia", "children"),
    ],
    Input("demo-reg", "value"),
)
def display_status(location):
    df_regiao_tratado=pd.read_csv('docs/df_regiao_tratado.csv')
    if not location:
        pass
    else:
        df_data_regiao=df_regiao_tratado[df_regiao_tratado["nome_drs"]==location]
        end_date=df_data_regiao["datahora"].max()
        df_data_regiao = df_data_regiao[df_data_regiao["datahora"] == end_date]

    leito = "-" if df_data_regiao["ocupacao_leitos"].isna().values[0] else (df_data_regiao["ocupacao_leitos"].values[0])
    pop = "-" if df_data_regiao["pop"].isna().values[0] else f'{int(df_data_regiao["pop"].values[0]):,}'.replace(",", ".")
    internacoes = "-" if df_data_regiao["internacoes_7d"].isna().values[0] else f'{int(df_data_regiao["internacoes_7d"].values[0]):,}'.replace(",", ".")
    coviduti= "-" if df_data_regiao["total_covid_uti_ultimo_dia"].isna().values[0] else f'{int(df_data_regiao["total_covid_uti_ultimo_dia"].values[0]):,}'.replace(",", ".")
    ocupacao= "-" if df_data_regiao["ocupacao_leitos_ultimo_dia"].isna().values[0] else (df_data_regiao["ocupacao_leitos_ultimo_dia"].values[0])
    ultimodia= "-" if df_data_regiao["internacoes_ultimo_dia"].isna().values[0] else f'{int(df_data_regiao["internacoes_ultimo_dia"].values[0]):,}'.replace(",", ".")

    return(f'{leito}%',
           pop,
           internacoes,
           coviduti,
           f'{ocupacao}%',
           ultimodia)
# ==================================================================
# Popover DRS
@app.callback(
    Output("drs-popover", "children"),
    Input("demo-reg","value")
)
def display_status(location):
    df_regiao_tratado=pd.read_csv('docs/df_regiao_tratado.csv')
    if not location:
        pass
    else:
        df_data_regiao=df_regiao_tratado[df_regiao_tratado["nome_drs"]==location]

    cidade = df_data_regiao["Cidades"].values[0]

    return cidade

#================= Callback modal macro=================================================

@app.callback(
    Output("modal-xl", "is_open"),
    [Input("open-xl", "n_clicks")],
    [State("modal-xl", "is_open")],
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open

# ==================================================================
# Chamada de servidor
if __name__ == "__main__":
    app.run_server(debug=True)