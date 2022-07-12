import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(executable_path=r'C:\Users\Matheus Cerutti\Documents\GitPublico\Publico\rpa-python\venv\geckodriver.exe')
driver.get("?")

elem = driver.find_element(By.NAME, "form_id:cpf_id")
elem.clear()
elem.send_keys("?")
elem = driver.find_element(By.NAME, "form_id:senha_id")
elem.clear()
elem.send_keys("?")
elem = driver.find_element(By.NAME, "form_id:acessar_id")
elem.click()
elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/form/ul[1]/li[1]/a/i")
sleep(1)
elem.click()
elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/form/ul[2]/li/div/ul/li[10]/a/span[2]")
sleep(1)
elem.click()
elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[1]/td/div/div/table/tbody/tr/td/table/tbody/tr/td[4]/div/div[3]")
sleep(1)
elem.click()
elem = driver.find_element(By.NAME, "formProvasAluno:selecionaEsquadrao_focus")
elem = driver.find_element(By.ID, "formProvasAluno:selecionaEsquadrao_1")
elem.send_keys("1GTT")
elem.click()
elem = driver.find_element(By.NAME, "formProvasAluno:dataTableProvasEmergencia:0:btnRealizarProva")
sleep(1)
elem.click()

elem = driver.find_element(By.ID, "formRealizarProva:tableItensEmergencia:0:inputResposta")
elem.clear()
sleep(1)
elem.send_keys("LIGHT ON")
pyautogui.click(100, 200) 

items=["PUSH"]

def loop(a,items):
    str(a)
    for index,item in enumerate(items):
        try:
            elem = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[{a}]/td[1]")
            sleep(1)
            elem.click()
            elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
            elem.clear()
            sleep(1)
            elem.send_keys(f"{item}")
            pyautogui.click(100, 200)
        except:
            pass

loop(2,items)

items=["DON, 100%","ESTABLISH","IDLE","FULL","10000 FT OR MEA, WHICHEVER IS HIGHER","MAX APPROPRIATE","ON","7700"]

loop(3,items)

items=["DON,EMER","DON"]

loop(4,items)

items=["MIN 260 KIAS"]

loop(5,items)

items=["IDLE","FULL","MAX APPROPRIATE","10000 FT OR MEA, WHICHEVER IS HIGHER","7700"]

loop(6,items)

items=["DISENGAGE","0","IDLE","STOP","PUSH"]

loop(7,items)

items=["0","STOP"]

loop(8,items)

items=["DISENGAGE","0","IDLE","STOP","PUSH"]

loop(9,items)

items=["DON,EMER","DON"]

loop(10,items)

items=["PUSH (STRIPPED BAR ON)"]

loop(11,items)

items=["0","PRESS","UP","0","UP","ALTERNATE"]

loop(12,items)

items=["LIGHT ON"]

loop(13,items)

items=["PRESS AND HOLD FOR 20 SECONDS"]

loop(14,items)

items=["DON,EMER","DON"]

loop(15,items)

items=["DISARM"]

loop(16,items)

elem = driver.find_element(By.ID, "formRealizarProva:botaoTerminarProva")
sleep(1)
elem.click()




