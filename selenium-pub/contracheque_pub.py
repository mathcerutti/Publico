import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CURR_DIR = os.getcwd()

driver = webdriver.Firefox(executable_path=r'?')

driver.get("?")

elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "cpf")))
elem.clear()
elem.send_keys("?")
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "senha")))
elem.clear()
elem.send_keys("?")
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "login")))
elem.click()
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/button")))
elem.click()

writer = pd.ExcelWriter(f'{CURR_DIR}/contracheque.xlsx')
row=1

for  ano in range (0,1):
    for mes in range (0,6):
        WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CLASS_NAME,"modal-backdrop fade")))
        sleep(1)
        select_element = Select(WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'ano'))))
        select_element.select_by_index(f'{ano}')
        select_element = Select(WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,'mes'))))
        select_element.select_by_index(f'{mes}')
        elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "buscar")))
        elem.click()
        elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/button")))
        elem.click()
        select_table = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/section[2]/div/div/form/div/div/div[1]/div[3]/table[3]")))
        raw_html_table = select_table.get_attribute('innerHTML')
        html_table=f'<html><table>{raw_html_table}</table></html>'
        table = pd.read_html(html_table)[0]
        df = pd.DataFrame(data=table)
        linhas = df.shape[0]+1
        df.to_excel(writer,sheet_name='contracheque',index=False,startrow=row)
        row += linhas
        writer.save()


        
      






