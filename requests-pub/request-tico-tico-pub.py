import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

CURR_DIR = os.getcwd()

url = '?'

headers = {?}


data ='javax.faces.partial.ajax=true&javax.faces.source=form%3AticoTable&javax.faces.partial.execute=form%3AticoTable&javax.faces.partial.render=form%3AticoTable&form%3AticoTable=form%3AticoTable&form%3AticoTable_filtering=true&form%3AticoTable_encodeFeature=true&form=form&form%3AcomboPostoGraduacao=&form%3AcomboQuadro=&form%3AcomboEspecialidade=&form%3Aj_idt194=&form%3Aj_idt196=&form%3Aj_idt199=&form%3AcomboOM=162024&form%3AcomboQuadroTurma=&form%3AmesAno=&form%3AticoTable%3Aj_idt210%3Afilter=&form%3AticoTable%3Aj_idt214%3Afilter=&form%3AticoTable%3Aj_idt216%3Afilter=&form%3AticoTable%3Aj_idt218%3Afilter=&form%3AticoTable%3Aj_idt220%3Afilter=&form%3AticoTable%3Aj_idt223%3Afilter=&form%3AticoTable%3Aj_idt225%3Afilter=&form%3AticoTable%3Aj_idt227%3Afilter=&form%3AticoTable_rppDD=50&javax.faces.ViewState=-5158285750612643417%3A-4763409496948808531'

response = requests.post(url,headers=headers,data=data,verify=False)
grossResult = response.content
tree = ET.ElementTree(ET.fromstring(grossResult))
root = tree.getroot()
changes = root.find('changes')
update = changes[1]

text = update.text
html = f'<html><table>{text}</table></html>'

bs = BeautifulSoup(html, "html.parser")

trs = bs.findAll("tr")

dados = []

df = pd.DataFrame(data=dados, columns=['nome','posto','quadro','saram'])

i =1
for item in trs:
    tds = item.findAll("td")
    nome = (tds[4].text)
    saram = (tds[3].text)
    posto = (tds[1].text)
    quadro = (tds[2].text)
    entrada = [nome,posto, quadro, saram]
    df.loc[i] = entrada
    i += 1

writer = pd.ExcelWriter(f'{CURR_DIR}/listafetivo.xlsx')
df.to_excel(writer,sheet_name='lista',index=False)
writer.save()

