import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'?')

driver.get("?")

elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "form_id:cpf_id")))
elem.clear()
elem.send_keys("?")
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "form_id:senha_id")))
elem.clear()
elem.send_keys("?")
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "form_id:acessar_id")))
elem.click()
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/form/ul[1]/li[1]/a/i")))
elem.click()
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[1]/div[1]/form/ul[2]/li/div/ul/li[10]/a/span[2]")))
elem.click()
WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,"j_idt10_modal")))
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[1]/td/div/div/table/tbody/tr/td/table/tbody/tr/td[4]/div/div[3]")))
elem.click()
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "formProvasAluno:selecionaEsquadrao_1")))
elem.click()
WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,"j_idt10_modal")))
elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "formProvasAluno:dataTableProvasEmergencia:0:btnRealizarProva")))
elem.click()

def loop(a,items):
    str(a)
    for index,item in enumerate(items):
        try:
            #sleep(0.5)
            elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[{a}]/td[1]"))) 
            elem.click()
            #sleep(0.5)
            WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.ID,"j_idt10_modal")))
            elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")))
            elem.click()
            #sleep(0.5)
            elem.send_keys(f"{item}")
            pyautogui.click(100, 200)   
        except:
            pass

items=["LIGHT ON"]

loop(1,items)

items=["PUSH"]

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

elem = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "formRealizarProva:botaoTerminarProva")))
elem.click()




