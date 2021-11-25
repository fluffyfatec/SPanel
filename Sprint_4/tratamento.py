import pandas as pd
import numpy as np

# ==================================================================
# Tratamento dos dados
# Tratando df_state.csv
df_state = pd.read_csv('docs/df_state.csv', sep=";")
df_state = df_state.drop(
    columns=['dia', 'mes', 'casos_pc', 'casos_mm7d', 'obitos_pc', 'obitos_mm7d', 'letalidade', 'nome_ra'
         , 'cod_ra', 'nome_drs', 'cod_drs', "pop_60", 'area', 'map_leg', 'map_leg_s', 'latitude', 'longitude','semana_epidem','codigo_ibge'])
df_state['nome_munic'] = df_state['nome_munic'].str.upper()
df_state['datahora'] = pd.to_datetime(df_state['datahora'],format='%d/%m/%Y')

# Tratando dados estado
df_estadotratado = df_state.drop(
    columns=['nome_munic'])
df_estadotratado = df_estadotratado.assign(estado='SÃO PAULO')
df_estadotratado.sort_values("datahora")
df_estadotratado['casos'] = df_estadotratado.groupby('datahora')["casos"].transform(sum)
df_estadotratado['casos_novos'] = df_estadotratado.groupby('datahora')["casos_novos"].transform(sum)
df_estadotratado['obitos'] = df_estadotratado.groupby('datahora')["obitos"].transform(sum)
df_estadotratado['obitos_novos'] = df_estadotratado.groupby('datahora')["obitos_novos"].transform(sum)
df_estadotratado['pop'] = df_estadotratado.groupby('datahora')["pop"].transform(sum)
df_estadotratado=df_estadotratado.drop_duplicates(subset='datahora', keep='first')

# Tratando vacinas.csv
df=pd.read_csv("docs/vacinas.csv", sep=';')
df = df.rename(
    columns={'Município':'nome_munic'})
# ==================================================================
df_unica = df[df['Dose'] =='UNICA']
df_unica = df_unica.rename(
    columns={'Total Doses Aplicadas':'doseunica'})
df_unica = df_unica.drop(
    columns=['Dose'])
# ==================================================================
df_primeira = df[df['Dose'] =='1° DOSE']
df_primeira = df_primeira.rename(
    columns={'Total Doses Aplicadas': 'primeiradose'})
df_primeira = df_primeira.drop(
    columns=['Dose'])
# ==================================================================
df_segunda = df[df['Dose'] =='2° DOSE']
df_segunda = df_segunda.rename(
    columns={'Total Doses Aplicadas':'segundadose'})
df_segunda = df_segunda.drop(
    columns=['Dose'])
# ==================================================================
df_terceira = df[df['Dose'] =='3º DOSE']
df_terceira = df_terceira.rename(
    columns={'Total Doses Aplicadas':'terceiradose'})
df_terceira = df_terceira.drop(
    columns=['Dose'])
df_pop = df_state.drop(
    columns=['datahora', 'casos','casos_novos','obitos','obitos_novos'])
df_pop=df_pop.drop_duplicates(subset='nome_munic', keep='first')

# Junção das doses no df_vacinas
df_vacinastratado = pd.merge(df_unica,df_primeira, how='inner', on='nome_munic')
df_vacinastratado = pd.merge(df_vacinastratado,df_segunda, how='inner', on='nome_munic')
df_vacinastratado = pd.merge(df_vacinastratado,df_terceira, how='inner', on='nome_munic')
df_vacinastratado = pd.merge(df_vacinastratado,df_pop, how='inner', on='nome_munic')
df_vacinastratado.fillna(('-'), inplace=True)


# Junção das vacinas.csv e df_state.csv no df_tratado.csv
df_state.sort_values("datahora")
df_state.to_csv("docs/df_tratado.csv")
df_vacinastratado.to_csv("docs/df_vacinastratado.csv")
df_estadotratado.to_csv("docs/df_estadotratado.csv")

# Tratando df_regiao

df_regiao_tratado = pd.read_csv("docs/df_regiao.csv", sep=';')
df_regiao_tratado = df_regiao_tratado.drop(
    columns= [ 'pacientes_uti_mm7d','total_covid_uti_mm7d','internacoes_7d_l','internacoes_7v7', 'pacientes_uti_ultimo_dia',
        'pacientes_enf_mm7d','total_covid_enf_mm7d','pacientes_enf_ultimo_dia','total_covid_enf_ultimo_dia', 'leitos_pc'])
df_regiao_tratado.to_csv('docs/df_regiao_tratado.csv')

df_regiao_tratado = pd.read_csv("docs/df_regiao_tratado.csv")
conditions = [
    (df_regiao_tratado["nome_drs"] == 'DRS 01 Grande São Paulo'),
    (df_regiao_tratado['nome_drs'] =='DRS 02 Araçatuba'),
    (df_regiao_tratado['nome_drs'] =='DRS 03 Araraquara'),
    (df_regiao_tratado['nome_drs'] =='DRS 04 Baixada Santista'),
    (df_regiao_tratado['nome_drs'] =='DRS 05 Barretos'),
    (df_regiao_tratado['nome_drs'] =='DRS 06 Bauru'),
    (df_regiao_tratado['nome_drs'] =='DRS 07 Campinas'),
    (df_regiao_tratado['nome_drs'] =='DRS 08 Franca'),
    (df_regiao_tratado['nome_drs'] =='DRS 09 Marília'),
    (df_regiao_tratado['nome_drs'] =='DRS 10 Piracicaba'),
    (df_regiao_tratado['nome_drs'] =='DRS 11 Presidente Prudente'),
    (df_regiao_tratado['nome_drs'] =='DRS 12 Registro'),
    (df_regiao_tratado['nome_drs'] == 'DRS 13 Ribeirão Preto'),
    (df_regiao_tratado['nome_drs'] =='DRS 14 São João da Boa Vista'),
    (df_regiao_tratado['nome_drs'] =='DRS 15 São José do Rio Preto'),
    (df_regiao_tratado['nome_drs'] =='DRS 16 Sorocaba'),
    (df_regiao_tratado['nome_drs'] =='DRS 17 Taubaté')]

choices = ['- ARUJÁ, - BARUERI, - BIRITIBA MIRIM, - CAIEIRAS, - CAJAMAR, - CARAPICUÍBA, - COTIA, - DIADEMA, - EMBU, - EMBU GUAÇU, - FERRAZ DE VASCONCELOS, - FRANCISCO MORATO, - FRANCO DA ROCHA, - GUARAREMA, - GUARULHOS, - ITAPECERICA DA SERRA, - ITAPEVI, - ITAQUAQUECETUBA, - JANDIRA, - JUQUITIBA, - MAIRIPORÃ, - MAUÁ, - MOGI DAS CRUZES, - OSASCO, - PIRAPORA DO BOM JESUS, - POÁ, - RIBEIRÃO PIRES, - RIO GRANDE DA SERRA, - SALESÓPOLIS, - SANTA ISABEL, - SANTANA DE PARNAÍBA, - SANTO ANDRÉ, - SÃO BERNARDO DO CAMPO, - SÃO CAETANO DO SUL, - SÃO LOURENÇO DA SERRA, - SÃO PAULO, - SUZANO, - TABOÃO DA SERRA, - VARGEM GRANDE PAULISTA.',
           '- ALTO ALEGRE, - ANDRADINA, - ARAÇATUBA, - AURIFLAMA, - AVANHANDAVA, - BARBOSA, -BENTO DE ABREU, - BILAC, - BIRIGUI, - BRAÚNA, - BREJO ALEGRE, - BURITAMA, - CASTILHO, - CLEMENTINA, - COROADOS, - GABRIEL MONTEIRO, - GLICÉRIO, - GUARAÇAÍ, - GUARARAPES,- GUZOLÂNDIA, - ILHA SOLTEIRA, - ITAPURA, - LAVÍNIA, - LOURDES, - LUIZIÂNIA, - MIRANDÓPOLIS, - MURUTINGA DO SUL, - NOVA CASTILHO, - NOVA INDEPENDÊNCIA, - NOVA LUZITÂNIA, - PENÁPOLIS, - PEREIRA BARRETO, - PIACATU, - RUBIÁCEA, - SANTO ANTÔNIO DO ARACANGUÁ, - SANTÓPOLIS DO AGUAPEÍ, - SUD MENNUCCI, - SUZANÁPOLIS, - TURIÚBA,- VALPARAÍSO.',
           '- AMÉRICO BRASILIENSE, - ARARAQUARA, - BOA ESPERANÇA DO SUL, - BORBOREMA, - CÂNDIDO RODRIGUES, - DESCALVADO, - DOBRADA, - DOURADO, - GAVIÃO PEIXOTO, - IBATÉ, - IBITINGA, - ITÁPOLIS, - MATÃO, - MOTUCA, - NOVA EUROPA, -PORTO FERREIRA, - RIBEIRÃO BONITO, - RINCÃO, - SANTA ERNESTINA, - SANTA LÚCIA, - SÃO CARLOS, - TABATINGA, - TAQUARITINGA, - TRABIJU.',
           '- BERTIOGA, - CUBATÃO, - GUARUJÁ, - ITANHAÉM, - MONGAGUÁ, - PERUÍBE, - PRAIA GRANDE, - SANTOS, - SÃO VICENTE.',
           '- ALTAIR, - BARRETOS, - BEBEDOURO, - CAJOBI, - COLINA, - COLÔMBIA, - GUAÍRA, - GUARACI, - JABORANDI, - MONTE AZUL PAULISTA, - OLÍMPIA, - SEVERÍNIA, - TAIAÇU, - TAIÚVA, - TAQUARAL, - TERRA ROXA, - VIRADOURO, - VISTA ALEGRE DO ALTO.',
           '- ÁGUAS DE SANTA BÁRBARA, - AGUDOS, - ANHEMBI, - ARANDU, - AREALVA, - AREIÓPOLIS, - AVAÍ, - AVARÉ, - BALBINOS, - BARÃO DE ANTONINA, - BARIRI, - BARRA BONITA, - BAURU, - BOCAINA, - BOFETE, - BORACÉIA, - BOREBI, - BOTUCATU, - BROTAS, - CABRÁLIA PAULISTA, - CAFELÂNDIA, - CERQUEIRA CÉSAR, - CONCHAS, - CORONEL MACEDO, - DOIS CÓRREGOS, - DUARTINA, - FARTURA, - GETULINA, - GUAIÇARA, - IACANGA, - IARAS, - IGARAÇU DO TIETÊ, - ITAÍ, - ITAJU, - ITAPORANGA, - ITAPUÍ, - ITATINGA, - JAÚ, - LARANJAL PAULISTA, - LENÇÓIS PAULISTA, - LINS, - LUCIANÓPOLIS, - MACATUBA, - MANDURI, - MINEIROS DO TIETÊ, - PARANAPANEMA, - PARDINHO, - PAULISTÂNIA, - PEDERNEIRAS, - PEREIRAS, - PIRAJU, - PIRAJUÍ, - PIRATININGA, - PONGAÍ, - PORANGABA, - PRATÂNIA,- PRESIDENTE ALVES, - PROMISSÃO,- REGINÓPOLIS, - SABINO, - SÃO MANUEL, - SARUTAIÁ, - TAGUAÍ, - TAQUARITUBA, - TEJUPÁ, - TORRE DE PEDRA, - TORRINHA, - URU.',
           '- ÁGUAS DE LINDÓIA, - AMERICANA, - AMPARO, - ARTUR NOGUEIRA, - ATIBAIA, - BOM JESUS DOS PERDÕES, - BRAGANÇA PAULISTA, - CABREÚVA, - CAMPINAS, - CAMPO LIMPO PAULISTA, - COSMÓPOLIS, - HOLAMBRA, - HORTOLÂNDIA, - INDAIATUBA, - ITATIBA, - ITUPEVA, - JAGUARIÚNA, - JARINU, - JOANÓPOLIS, - JUNDIAÍ, - LINDÓIA, - LOUVEIRA, - MONTE ALEGRE DO SUL, - MONTE MOR, - MORUNGABA, - NAZARÉ PAULISTA, - NOVA ODESSA, - PAULÍNIA, - PEDRA BELA, - PEDREIRA, - PINHALZINHO, - PIRACAIA, - SANTA BÁRBARA D OESTE, - SANTO ANTÔNIO DA POSSE, - SERRA NEGRA, - SOCORRO,SUMARÉ, - TUIUTIVALINHOS, - VARGEM,VÁRZEA PAULISTA, - VINHEDO.',
           '- ARAMINA, - BURITIZAL, - CRISTAIS PAULISTA, - FRANCA, - GUARÁ, - IGARAPAVA, - IPUÃ, - ITIRAPUÃ, - ITUVERAVA, - JERIQUARA, - MIGUELÓPOLIS, - MORRO AGUDO, -NUPORANGA, - ORLÂNDIA, - PATROCÍNIO PAULISTA, - PEDREGULHO, - RESTINGA, - RIBEIRÃO CORRENTE, - RIFAINA, - SALES OLIVEIRA, - SÃO JOAQUIM DA BARRA, - SÃO JOSÉ DA BELA VISTA.',
           '- ADAMANTINA, - ÁLVARO DE CARVALHO, - ALVINLÂNDIA, - ARCO ÍRIS, - ASSIS, - BASTOS, - BERNARDINO DE CAMPOS, - BORÁ, - CAMPOS NOVOS PAULISTA, - CÂNDIDO MOTA, - CANITAR, - CHAVANTES, - CRUZÁLIA, - ECHAPORÃ, - ESPÍRITO SANTO DO TURVO, - FERNÃO, - FLÓRIDA PAULISTA, - FLORÍNIA, - GÁLIA, - GARÇA, - GUAIMBÊ, - GUARANTÃ, - HERCULÂNDIA, - IACRI, - IBIRAREMA, - INÚBIA PAULISTA, - IPAUSSU, - JÚLIO MESQUITA, - LUCÉLIA, - LUPÉRCIO, - LUTÉCIA, - MARACAÍ, - MARIÁPOLIS, - MARÍLIA, - OCAUÇU, - ÓLEO, - ORIENTE, - OSCAR BRESSANE, - OSVALDO CRUZ, - OURINHOS, - PACAEMBU, - PALMITAL, - PARAGUAÇU PAULISTA, - PARAPUÃ, - PEDRINHAS PAULISTA, - PLATINA, - POMPÉIA, - PRACINHA, - QUEIROZ, - QUINTANA, - RIBEIRÃO DO SUL, - RINÓPOLIS, - SAGRES, - SALMOURÃO, - SALTO GRANDE, - SANTA CRUZ DO RIO PARDO, - SÃO PEDRO DO TURVO, - TARUMÃ, - TIMBURI, - TUPÃ, - UBIRAJARA, - VERA CRUZ.',
           '- ÁGUAS DE SÃO PEDRO, - ANALÂNDIA, - ARARAS, - CAPIVARI, - CHARQUEADA, - CONCHAL, - CORDEIRÓPOLIS, - CORUMBATAÍ, - ELIAS FAUSTO, - ENGENHEIRO COELHO, - IPEÚNA, - IRACEMÁPOLIS, - ITIRAPINA, - LEME, - LIMEIRA, - MOMBUCA, - PIRACICABA, - PIRASSUNUNGA, - RAFARD, - RIO CLARO, - RIO DAS PEDRAS, - SALTINHO, - SANTA CRUZ DA CONCEIÇÃO, - SANTA GERTRUDES,- SANTA MARIA DA SERRA, - SÃO PEDRO',
           '- ALFREDO MARCONDES, - ÁLVARES MACHADO, - ANHUMAS, - CAIABU, - CAIUÁ, - DRACENA, - EMILIANÓPOLIS, - ESTRELA DO NORTE, - EUCLIDES DA CUNHA PAULISTA, - FLORA RICA, - IEPÊ, - INDIANA, - IRAPURU, - JOÃO RAMALHO, - JUNQUEIRÓPOLIS, - MARABÁ PAULISTA, - MARTINÓPOLIS, - MIRANTE DO PARANAPANEMA, - MONTE CASTELO, - NANTES, - NARANDIBA, - NOVA GUATAPORANGA, - OURO VERDE, - PANORAMA, - PAULICÉIA, - PIQUEROBI, - PIRAPOZINHO, - PRESIDENTE BERNARDES, - PRESIDENTE EPITÁCIO, - PRESIDENTE PRUDENTE, - PRESIDENTE VENCESLAU, - QUATÁ, - RANCHARIA, - REGENTE FEIJÓ, - RIBEIRÃO DOS ÍNDIOS, - ROSANA, - SANDOVALINA, - SANTA MERCEDES, - SANTO ANASTÁCIO, - SANTO EXPEDITO, - SÃO JOÃO DO PAU D ALHO, - TACIBA, - TARABAI, - TEODORO SAMPAIO, - TUPI PAULISTA.',
           '- BARRA DO TURVO, - CAJATI, - CANANÉIA, - ELDORADO, - IGUAPE, - ILHA COMPRIDA, - IPORANGA, - ITARIRI, - JACUPIRANGA, - JUQUIÁ, - MIRACATU, - PARIQUERA AÇU, - PEDRO DE TOLEDO, - REGISTRO, - SETE BARRAS.',
           '- ALTINÓPOLIS, - BARRINHA, - BATATAIS, - BRODOWSKI, - CAJURU, - CÁSSIA DOS COQUEIROS, - CRAVINHOS, - DUMONT, - GUARIBA, -GUATAPARÁ, - JABOTICABAL, - JARDINÓPOLIS, - LUÍS ANTÔNIO, - MONTE ALTO, - PITANGUEIRAS, - PONTAL, - PRADÓPOLIS, - RIBEIRÃO PRETO, - SANTA CRUZ DA ESPERANÇA, - SANTA RITA DO PASSA QUATRO, - SANTA ROSA DE VITERBO, - SANTO ANTÔNIO DA ALEGRIA, - SÃO SIMÃO, - SERRA AZUL, - SERRANA,- SERTÃOZINHO.',
           '- AGUAÍ, - ÁGUAS DA PRATA, - CACONDE, - CASA BRANCA, - DIVINOLÂNDIA, - ESPÍRITO SANTO DO PINHAL, - ESTIVA GERBI, - ITAPIRA, - ITOBI, - MOCOCA, - MOGI GUAÇU, - MOGI MIRIM, - SANTA CRUZ DAS PALMEIRAS, - SANTO ANTÔNIO DO JARDIM, - SÃO JOÃO DA BOA VISTA, - SÃO JOSÉ DO RIO PARDO, - SÃO SEBASTIÃO DA GRAMA, - TAMBAÚ, - TAPIRATIBA, - VARGEM GRANDE DO SUL.',
           ''' - ADOLFO, - ÁLVARES FLORENCE, - AMÉRICO DE CAMPOS, - APARECIDA D OESTE, - ARIRANHA, - ASPÁSIA, - BADY BASSIT, - BÁLSAMO, - CARDOSO, - CATANDUVA, - CATIGUÁ, - CEDRAL, - COSMORAMA, - DIRCE REIS, - DOLCINÓPOLIS, - ELISIÁRIO, - EMBAÚBA, - ESTRELA D OESTE, - FERNANDÓPOLIS, - FERNANDO PRESTES, - FLOREAL, - GASTÃO VIDIGAL, - GENERAL SALGADO, - GUAPIAÇU, - GUARANI D OESTE, - IBIRÁ, - ICÉM, - INDIAPORÃ, - IPIGUÁ, - IRAPUÃ, - ITAJOBI, - JACI, - JALES, - JOSÉ BONIFÁCIO, - MACAUBAL, - MACEDÔNIA, - MAGDA, - MARAPOAMA, - MARINÓPOLIS, - MENDONÇA, - MERIDIANO, - MESÓPOLIS, - MIRA ESTRELA, - MIRASSOL, - MIRASSOLÂNDIA, - MONÇÕES, - MONTE APRAZÍVEL, - NEVES PAULISTA, - NHANDEARA, - NIPOÃ, - NOVA ALIANÇA, - NOVA CANAÃ PAULISTA, - NOVA GRANADA, - NOVAIS, - NOVO HORIZONTE, - ONDA VERDE, - ORINDIÚVA, - OUROESTE, - PALESTINA, - PALMARES PAULISTA, - PALMEIRA D OESTE, - PARAÍSO, - PARANAPUÃ, - PARISI, - PAULO DE FARIA, - PEDRANÓPOLIS, - PINDORAMA, - PIRANGI, - PLANALTO, - POLONI, - PONTALINDA, - PONTES GESTAL, - POPULINA, - POTIRENDABA, - RIOLÂNDIA, - RUBINÉIA, - SALES, - SANTA ADÉLIA, - SANTA ALBERTINA, - SANTA CLARA D OESTE, - SANTA FÉ DO SUL, - SANTA RITA D OESTE, - SANTA SALETE - ,- SANTANA DA PONTE PENSA, - SÃO FRANCISCO, - SÃO JOÃO DAS DUAS PONTES, - SÃO JOÃO DE IRACEMA,- SÃO JOSÉ DO RIO PRETO, - SEBASTIANÓPOLIS DO SUL, - TABAPUÃ, - TANABI, - TRÊS FRONTEIRAS, - TURMALINA, - UBARANA, - UCHOA, - UNIÃO PAULISTA, - URÂNIA, - URUPÊS, - VALENTIM GENTIL, - VITÓRIA BRASIL, - VOTUPORANGA, - ZACARIAS.''',
           '- ALAMBARI, - ALUMÍNIO, - ANGATUBA, - APIAÍ, - ARAÇARIGUAMA, - ARAÇOIABA DA SERRA, - BARRA DO CHAPÉU, - BOITUVA, - BOM SUCESSO DE ITARARÉ, - BURI, - CAMPINA DO MONTE ALEGRE, - CAPÃO BONITO, - CAPELA DO ALTO, - CERQUILHO, - CESÁRIO LANGE, - GUAPIARA, - GUAREÍ, - IBIÚNA, - IPERÓ, - ITABERÁ, - ITAÓCA, - ITAPETININGA, - ITAPEVA, - ITAPIRAPUÃ PAULISTA, - ITARARÉ, - ITU, - JUMIRIM, - MAIRINQUE, - NOVA CAMPINA, - PIEDADE, - PILAR DO SUL, - PORTO FELIZ, - QUADRA, - RIBEIRA, - RIBEIRÃO BRANCO, - RIBEIRÃO GRANDE, - RIVERSUL, - SALTO, - SALTO DE PIRAPORA, - SÃO MIGUEL ARCANJO, - SÃO ROQUE, - SARAPUÍ, - SOROCABA, - TAPIRAÍ, - TAQUARIVAÍ, - TATUÍ, - TIETÊ, - VOTORANTIM.',
           '- APARECIDA, - ARAPEÍ, - AREIAS, - BANANAL, - CAÇAPAVA, - CACHOEIRA PAULISTA, - CAMPOS DO JORDÃO, - CANAS, - CARAGUATATUBA, - CRUZEIRO, - CUNHA, - GUARATINGUETÁ, - IGARATÁ, - ILHA BELA, - JACAREÍ, - JAMBEIRO, - LAGOINHA, - LAVRINHAS, - LORENA, - MONTEIRO LOBATO, - NATIVIDADE DA SERRA, - PARAIBUNA, - PINDAMONHANGABA, - PIQUETE, - POTIM, - QUELUZ, - REDENÇÃO DA SERRA, - ROSEIRA, - SANTA BRANCA, - SANTO ANTÔNIO DO PINHAL, - SÃO BENTO DO SAPUCAÍ, - SÃO JOSÉ DO BARREIRO, - SÃO JOSÉ DOS CAMPOS, - SÃO LUIZ DO PARAITINGA, - SÃO SEBASTIÃO, - SILVEIRAS, - TAUBATÉ, - TREMEMBÉ, - UBATUBA.',

           ]
df_regiao_tratado['Cidades'] = np.select(conditions, choices, default='Todos os municípios do estado de São Paulo')

df_regiao_tratado.to_csv("docs/df_regiao_tratado.csv")
