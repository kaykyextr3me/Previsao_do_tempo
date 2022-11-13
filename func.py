def tratar_cidade(municipio):
    nova_lista = list()
    lista_cidade = municipio.split(' ')

    for parte in lista_cidade:
        if parte != 'de':
            parte = parte.title()

        if parte == 'De':
            parte = parte.lower()
        nova_lista.append(parte)

    cidade = ' '.join(nova_lista)
    return cidade


def previsao_atual(cidade):
    from openpyxl import load_workbook
    import requests
    import json
    import datetime

    cidade = tratar_cidade(cidade)

    data_atual = datetime.date.today()
    data_formatada = data_atual.strftime('%d/%m/%Y')

    planilha = load_workbook('municipios.xlsx')
    aba_ativa = planilha.active
    contador = cont = indice = codigo = 0
    for celula in aba_ativa['M']:
        contador += 1
        if celula.value == cidade:
            indice = contador
    for celula in aba_ativa['L']:
        cont += 1
        if cont == indice:
            codigo = celula.value

    if codigo != 0:
        dados = requests.get(f'https://apiprevmet3.inmet.gov.br/previsao/{codigo}')
        temperatura = json.loads(dados.content)
        temp_max = temperatura[f'{codigo}'][f'{data_formatada}']['manha']['temp_max']
        icone = temperatura[f'{codigo}'][f'{data_formatada}']['manha']['icone']
        previsao = dict()
        previsao.update({'temp_max': temp_max,
                         'cidade': cidade,
                         'icone': icone
                         })

        return previsao

    else:
        return 'cidade incorreta'
