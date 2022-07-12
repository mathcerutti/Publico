import os
import pandas as pd
import requests
import json

CURR_DIR = os.getcwd()

url = 'https://mail.fab.mil.br/service/soap/AutoCompleteRequest'

listanomes=[]

def get_email(nome):
    headers = {
    'Host': 'mail.fab.mil.br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/soap+xml; charset=utf-8',
    'X-Zimbra-Csrf-Token': '0_1d749b4707669f24a9d36b97c6591af56f96d53a',
    'Content-Length': '386',
    'Origin': 'https://mail.fab.mil.br',
    'Proxy-Authorization': '?',
    'Connection':'keep-alive',
    'Referer': 'https://mail.fab.mil.br/',
    'Cookie': '?'
    }

    data = {
        "Body": {
            "AutoCompleteRequest": {
                "_jsns": "urn:zimbraMail",
                "name": {
                    "_content": f"{nome}"
                },
                "needExp": 1
            }
        },
        "Header": {
            "context": {
                "_jsns": "urn:zimbra",
                "account": {
                    "_content": "ceruttimcm@fab.mil.br",
                    "by": "name"
                },
                "csrfToken": "0_1d749b4707669f24a9d36b97c6591af56f96d53a",
                "session": {
                    "_content": 1667456,
                    "id": 1667456
                },
                "userAgent": {
                    "name": "ZimbraWebClient - FF102 (Win)",
                    "version": "8.8.15_GA_4303"
                }
            }
        }
    }

    response = requests.post(url,headers=headers, json=data)
    resultado = response.json()['Body']['AutoCompleteResponse']['match'][0]['email']
    return resultado
    

nomes = ["TC BARROS","MJ DANIEL SOUZA","MJ PORTELLA","MJ PACHECO","MJ SANTIAGO","MJ CEZAR","CP SOUZA","CP JACOBS","CP LEONARDO","CP SALDANHA","CP MAURICIO","CP MAIA","CP LEAL","CP ITALO","CP TORRES","CP HANDA","CP RAMOS","CP TIRADENTES","CP AVILA","CP RAMIRO","CP NUNES","CP POSSIDONIO","CP PROTASIO","CP JOEL","1T AVILA","1T CERUTTI","1T ASSIS","1T JAQUES","1T CAMPANARO","MESTRES DE CARGA (LM)","CP TELMO","1T ALBINO","SO MENDONCA","SO HORLISTEN","SO OTONIEL","SO A. LUIZ","SO TOMAS","1S DANIEL","2S ROMULO","2S NASCIMENTO","2S EDSON AGUIAR","2S RICARDO CUNHA","2S PINHEIRO","2S AMORIM","2S FULVIO","2S RIBEIRO","2S RENAN","2S ABDO","2S RODRIGO","2S DE PAULA","2S MARTINS","3S LAUDSON","3S TERRA","3S MULLER","3S IAN MAYER","3S EDGARD","3S GENUINO","3S DE SOUZA","3S PONTES","3S LUCAS BOTELHO","3S SOUZA PEREIRA","3S BITENCOURT","3S MOTA","1S ALCANTARA","2S GILBERT","2S L SANTOS","2S SARAIVA","2S GAUTERIO","2T SENILDO","SO LEAO","SO AZEVEDO","SO VARGAS","SO LIMA","1S W SILVA","1S BERNARDES","1S ANDRE LUIZ","1S ADSON","1S ELISEU EDUARDO","1S GARCEZ","1S KLEVER","1S SANTOS JUNIOR","2S DIEGO SILVA","2S ANDRADE","2S ANA CAROLINA","3S GABRIELA LAFAIETE","3S MONALISA","3S DOS SANTOS","2T CRISOSTOMO","SO AZEVEDO","SO AGACY","1S KLEVER","1S SANTOS JUNIOR","2S PEDRO","2S TAYSE","2S SALOTO","3S MIKAEL","3S VALENCA","1S RELIQUIAS","2S VOLNEI","2S CAIXETA","3S WAGNO","3S DE FARIA","3S VOLNEY BRITO","3S BITENCOURT","2S FERRAZ","2S WELLINGTON","2S DANIEL","2S ALISSON","3S ARTHUR","3S RENAN","2S ALEIXO","3S AMANDA","2S SOCRATES","1T CROSARA"
] 

for item in nomes:
    try:
        listanomes.append(get_email(item))
    except:
        pass



df = pd.DataFrame(data=listanomes,columns={'email'})
writer = pd.ExcelWriter(f'{CURR_DIR}/listanomes.xlsx')
df.to_excel(writer,index=False)

writer.save()
