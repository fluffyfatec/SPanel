# SPANEL SPRINT 2

# ==================================================================
# Bibliotecas do layout
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# ==================================================================
# Bibliotecas de manipulação de dados
import pandas as pd

# ==================================================================
# Pré processamentos
df_tratado = pd.read_csv("docs/df_tratado.csv")
#df_tratado['datahora'] = pd.to_datetime(df_tratado['datahora'],format='%d/%m/%Y') #formatação de datahotra
list_municipios = sorted(df_tratado['nome_munic'].unique()) #formatação de municipios

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
        ],md=7)
        # Modal do Dicas
        , dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Button("Dicas", id="open-modalFaq", className="bt_modalFaq", n_clicks=0, color="link",
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
                                    dbc.CardBody(html.Div([html.P("A COVID-19 é uma doença causada pelo coronavírus, nomeado SARS-CoV-2, que apresenta um sinal clínico variando de infecções, com quadros graves e assintomáticos."),
                                                          html.P("De acordo com a OMS (organização mundial de saúde), a maioria dos pacientes com COVID-19 podem ser assintomáticos ou apresentar poucos sintomas, em média 20% dos casos detectados necessitam de atendimento hospitalar, por causar dificuldade respiratória, dos quais 5% podem necessitar de suporte de ventilação mecânica.")
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
                                        dbc.CardBody(html.Div([html.P("• A transmissão é feita por contato: ou seja, por meio do contato direto com uma pessoa infectada – exemplo: com um aperto de mão seguido do toque nos olhos, nariz ou boca, ou com objetos e superfícies contaminadas;"),
                                                          html.P("• A transmissão por gotículas: por meio da exposição a gotículas respiratórias expelidas, contendo vírus, por uma pessoa infectada quando ela tosse ou espirra, principalmente quando ela se encontra a menos de 1 metro de distância da outra;")
                                                          ,html.P("• A transmissão por aerossol: por meio de gotículas respiratórias menores (aerossóis) contendo vírus e que podem permanecer suspensas no ar, serem levadas por distâncias maiores que 1 metro e por períodos mais longos - geralmente horas.")
                                                          ,html.P("A maioria das infecções se espalha por contato próximo - menos de 1 metro -, principalmente por meio de gotículas respiratórias.")
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
                                    dbc.CardBody(html.Div([html.P("• Caso assintomático: mesmo com o teste laboratorial positivo para covid-19 não apresentam sintomas."),
                                                          html.P("• Caso leve: indicado pela aparição de sintomas não específicos, como tosse, dor de garganta ou coriza, seguido, ou não, de perda de olfato e paladar, diarreia, dor abdominal, febre, calafrios, mialgia, fadiga e/ou cefaleia;")
                                                          ,html.P("• Caso moderado: os sintomas mais presentes podem apresentar sinais leves, como tosse persistente e febre persistente diária, até sinais de piora progressiva de outro sintoma relacionado à covid-19 (fraqueza, debilidade física, falta de apetite, diarreia), além da presença de pneumonia sem sinais ou sintomas de gravidade.")
                                                          ,html.P("• Caso grave: ou a Síndrome Respiratória Aguda Grave (Síndrome Gripal que apresente dificuldade para respirar, desconforto respiratório ou pressão persistente no peito ou saturação de oxigênio menor que 95% em ar ambiente ou coloração azulada de lábios ou rosto.")
                                                          ,html.P("• Caso crítico: os principais sintomas são infecção, síndrome do desconforto respiratório agudo, deficiência respiratória grave, mal funcionamento de múltiplos órgãos, pneumonia grave, necessidade de suporte respiratório mecânico e internações em UTI (unidades de terapia intensiva).")
                                                          ,html.P("• As crianças apresentam como os principais sintomas como: aceleração do ritmo respiratório, baixa saturação de oxigenação no sangue, desconforto respiratório, alteração da consciência, desidratação, dificuldade para se alimentar, coloração azulada, letargia, convulsões, recusa alimentar.")
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
                                    dbc.CardBody(html.Div([html.P("As medidas indicadas, estão as não farmacológicas (conjunto de intervenções que visam maximizar o funcionamento cognitivo e o bem-estar da pessoa, bem como ajudá-la no processo de adaptação à doença), como distanciamento social, etiqueta respiratória e de higienização das mãos, uso de máscaras, limpeza e desinfeção de ambientes, isolamento de casos suspeitos e confirmados e quarentena dos contatos dos casos de covid-19, conforme orientações médicas."),
                                                          html.P("Também é recomendada a vacinação contra a covid-19 dos grupos prioritários conforme o Plano Nacional de Operacionalização da Vacinação.")
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
                                html.P("O SPanel foi desenvolvido para a visualização ágil e simplificada dos dados do COVID-19 no Estado de São Paulo e seus respectivos Municípios.",style={"color":"#3B332D"}),

                                html.H6("Limitações",style={"color":"#1f1b18","font-weight": "bold","padding-top":"10px"}),
                                html.P("Levando em consideração a pluralidade em relação a infraestrutura ao estado e municípios, "
                                        "poderá haver mudanças aos números em decorrência de erros ou atrasos ao repasse de informações.",style={"color":"#3B332D"}),

                                html.H5("Conceitos básicos:",style={"color":"#1f1b18","font-weight": "bold","padding-top":"10px"}),
                                html.H6("Imunizados",style={"color":"#1f1b18","font-weight": "bold"}),
                                html.P("O número de imunizados, é feito pela soma da população que já efetuou a vacinação da dose "
                                        "única e da segunda dose das vacinas disponibilizadas pelo Governo do Estado de São Paulo.",style={"color":"#3B332D"}),

                                html.H6("Casos Acumulados",style={"color":"#1f1b18","font-weight": "bold","padding-top":"10px"}),
                                html.P("O número total de casos confirmados por COVID-19, foi disponibilizado pelo Estado de São Paulo em relação ao dia anterior.",style={"color":"#3B332D"}),

                                html.H6("Novos casos no período",style={"color":"#1f1b18","font-weight": "bold","padding-top":"10px"}),
                                html.P("O número de novos casos no período por COVID-19, foi disponibilizado pelo Estado de São Paulo em relação ao dia anterior realizando a soma dos dias definidos pelo usuario.",style={"color":"#3B332D"}),

                                html.H6("Óbitos Acumulados", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.P("O número de óbitos acumulados por COVID-19, foi disponibilizado pelo Estado de São Paulo em relação ao dia anterior.",style={"color":"#3B332D"}),

                                html.H6("Novos óbitos no período", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.P("O número de novos óbitos no período por COVID-19, foi disponibilizado pelo Estado de São Paulo em relação ao dia anterior realizando a soma dos dias definidos pelo usuario",style={"color": "#3B332D"}),

                                html.H6("População", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.P("O número da população, foi disponibilizado pelo Estado de São Paulo e pode conter uma divergência com a realiadade.",
                                    style={"color": "#3B332D"}),

                                html.H5("Indicadores básicos:", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.H6("Porcentagem Imunizados", style={"color": "#1f1b18", "font-weight": "bold"}),
                                html.P("A porcentagem de imunizados é dada pelo total de população do estado de São Paulo e seus respectivos municípios, e pelo total de imunizados até o presente momento.",
                                    style={"color": "#3B332D"}),

                                html.H6("Taxa de Letalidade", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.P("A taxa de letalidade por COVID-19, é feita pelo número de óbitos confirmados em relação, ao total de casos confirmados pelos cidadãos residentes no Estado de São Paulo e seus respectivos Municípios.",
                                    style={"color": "#3B332D"}),

                                html.H5("Fonte", style={"color": "#1f1b18", "font-weight": "bold","padding-top":"10px"}),
                                html.A("https://www.saopaulo.sp.gov.br/planosp/simi/dados-abertos/", href='https://www.saopaulo.sp.gov.br/planosp/simi/dados-abertos/', target="_blank",className="bt-link"),

                                html.Div([
                                dbc.Button("ARQUIVO .CSV", id="btn_csv",className='bt_close_modal',color="danger",style={"margin-top":"15px"}),
                                dcc.Download(id="download-dataframe-csv")])
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
                            start_date=df_tratado["datahora"].min(),
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
                        dcc.Dropdown(id="location-dropdown",
                                     options=[{"label": i, "value": i} for i in list_municipios]
                                     ,clearable=True,placeholder="Escolha um município",
                                     style={"background-color": "#1f1b18"}
                                     )
                    ],style={"margin-top": "25px"})
                ],md=5)
            ],justify='end')
        ],md=5)
    ], style={"background-color": "#1f1b18"})

# ==================================================================
    # Linha 2 - Vacinados, Casos, Obitos e População
    , dbc.Row([
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
            ], color="#db261f",className='cards')
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
            ], color="#ffffff",className='cards')
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
            ], color="#ffffff",className='cards')
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
            ], color="#201b17",className='cards')
        ], md=3)
    ], style={"border-bottom": "10px solid #f1f1f1", "background-image": "linear-gradient(#1f1b18 50%, #f1f1f1 50%)"})
], fluid=True)

# ==================================================================
# Interatividade
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
        #df_data_var_date = df_tratado.sort_values("datahora").set_index("datahora")[start_date,end_date]
        df_data_var_date = df_tratado[(df_tratado['datahora'] >= start_date) & (df_tratado['datahora'] <= end_date)]
        df_data_on_date = df_tratado[(df_tratado["datahora"] == end_date)]
        df_data_var_date = df_data_var_date.assign(obitos_novos=df_data_var_date['obitos_novos'].sum())# SOMAR PARA TRAZER ESTADO DE SP
        df_data_on_date = df_data_on_date.assign(obitos=df_data_on_date['obitos'].sum())  # SOMAR PARA TRAZER ESTADO DE SP
        df_data_var_date = df_data_var_date.assign(casos_novos=df_data_var_date['casos_novos'].sum())  # SOMAR PARA TRAZER ESTADO DE SP
        df_data_on_date = df_data_on_date.assign(casos=df_data_on_date['casos'].sum())  # SOMAR PARA TRAZER ESTADO DE SP
        df_data_on_date = df_data_on_date.assign(pop=df_data_on_date['pop'].sum())  # SOMAR PARA TRAZER ESTADO DE SP
        df_data_on_date = df_data_on_date.assign(doseunica=df_data_on_date["doseunica"].sum())
        df_data_on_date = df_data_on_date.assign(segundadose=df_data_on_date["segundadose"].sum())
        df_data_on_date = df_data_on_date.assign(Imunizados=df_data_on_date['doseunica'] + df_data_on_date['segundadose'])  # SOMAR PARA TRAZER ESTADO DE SP
        df_data_on_date = df_data_on_date.assign(porcentagemimunizados=df_data_on_date['Imunizados'] / df_data_on_date['pop'] * 100)
        decimals = 2
        df_data_on_date['porcentagemimunizados'] = df_data_on_date['porcentagemimunizados'].apply(lambda x: round(x, decimals))
        df_data_on_date = df_data_on_date.assign(primeiradose=df_data_on_date["primeiradose"].sum())
        df_data_on_date = df_data_on_date.assign(letalidade=df_data_on_date['obitos'] / df_data_on_date['casos'] * 100)
        df_data_on_date['letalidade'] = df_data_on_date['letalidade'].apply(lambda x: round(x, decimals))
    else:
        df_data_var_date = df_tratado[(df_tratado["nome_munic"] == location)]
        df_data_var_date = df_data_var_date[(df_data_var_date['datahora'] >= start_date) & (df_data_var_date['datahora'] <= end_date)]
        df_data_on_date = df_data_var_date[(df_data_var_date["datahora"] == end_date)]
        df_data_var_date = df_data_var_date.assign(obitos_novos=df_data_var_date['obitos_novos'].sum())
        df_data_var_date = df_data_var_date.assign(casos_novos=df_data_var_date['casos_novos'].sum())
        df_data_on_date = df_data_on_date.assign(Imunizados=df_data_on_date['doseunica'] + df_data_on_date['segundadose'])
        df_data_on_date = df_data_on_date.assign(porcentagemimunizados=df_data_on_date['Imunizados'] / df_data_on_date['pop'] * 100)
        decimals = 2
        df_data_on_date['porcentagemimunizados'] = df_data_on_date['porcentagemimunizados'].apply(lambda x: round(x, decimals))
        df_data_on_date = df_data_on_date.assign(letalidade=df_data_on_date['obitos'] / df_data_on_date['casos'] * 100)
        df_data_on_date['letalidade'] = df_data_on_date['letalidade'].apply(lambda x: round(x, decimals))

# Filtrando caso os dados sejam vazios e trocando ',' por '.'
    imunizados = "-" if df_data_on_date["Imunizados"].isna().values[0] else f'{int(df_data_on_date["Imunizados"].values[0]):,}'.replace(",", ".")
    primeiradose = "-" if df_data_on_date["primeiradose"].isna().values[0] else f'{int(df_data_on_date["primeiradose"].values[0]):,}'.replace(",", ".")
    porcentagemimunizados = "-" if df_data_on_date["porcentagemimunizados"].isna().values[0] else f'{float(df_data_on_date["porcentagemimunizados"].values[0]):,}'.replace(",", ".")
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
#Chamada do botão de download CSV
@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df_tratado.to_csv, "docs/df_tratado.csv")



# ==================================================================
# Chamada de servidor
if __name__ == "__main__":
    app.run_server(debug=True)