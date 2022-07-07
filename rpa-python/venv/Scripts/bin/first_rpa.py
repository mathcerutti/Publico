import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(executable_path=r'C:\Users\Matheus Cerutti\Documents\GitPublico\Publico\rpa-python\venv\geckodriver.exe')
driver.get("http://10.232.16.14:8080/MentorSagemWeb/index.jsf")

elem = driver.find_element(By.NAME, "form_id:cpf_id")
elem.clear()
elem.send_keys("13650156709")
elem = driver.find_element(By.NAME, "form_id:senha_id")
elem.clear()
elem.send_keys("portal6$A")
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

for index,item in enumerate(items):
    elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[2]/td[1]")
    sleep(1)
    elem.click()
    elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
    elem.clear()
    sleep(1)
    elem.send_keys(f"{item}")
    pyautogui.click(100, 200) 

items=["DON, 100%","ESTABLISH","IDLE","FULL","10000 FT OR MEA, WHICHEVER IS HIGHER","MAX APPROPRIATE","ON","7700"]

for index,item in enumerate(items):
    elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[3]/td[1]")
    sleep(1)
    elem.click()
    elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
    elem.clear()
    sleep(1)
    elem.send_keys(f"{item}")
    pyautogui.click(100, 200)

items=["DON,EMER","DON"]

for index,item in enumerate(items):
    elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[4]/td[1]")
    sleep(1)
    elem.click()
    elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
    elem.clear()                       
    sleep(1)
    elem.send_keys(f"{item}")
    pyautogui.click(100, 200)

items=["MIN 260 KIAS"]

for index,item in enumerate(items):
    elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[5]/td[1]")
    sleep(1)
    elem.click()
    elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
    elem.clear()                       
    sleep(1)
    elem.send_keys(f"{item}")
    pyautogui.click(100, 200)

items=["IDLE","FULL","MAX APPROPRIATE","10000 FT OR MEA, WHICHEVER IS HIGHER","7700"]

for index,item in enumerate(items):
    elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[6]/td[1]")
    sleep(1)
    elem.click()
    elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
    elem.clear()                       
    sleep(1)
    elem.send_keys(f"{item}")
    pyautogui.click(100, 200)

items=["DISENGAGE","0","IDLE","STOP","PUSH"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[7]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["0","STOP"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[8]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["DISENGAGE","0","IDLE","STOP","PUSH"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[9]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["DON,EMER","DON"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[10]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["PUSH (STRIPPED BAR ON)"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[11]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["0","PRESS","UP","0","UP","ALTERNATE"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[12]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["LIGHT ON"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[13]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["PRESS AND HOLD FOR 20 SECONDS"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[14]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["DON,EMER","DON"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[15]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

items=["DISARM"]

for index,item in enumerate(items):
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/form/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div[2]/div/div/div/table/tbody/tr[16]/td[1]")
        sleep(1)
        elem.click()
        elem = driver.find_element(By.ID, f"formRealizarProva:tableItensEmergencia:{index}:inputResposta")
        elem.clear()                       
        sleep(1)
        elem.send_keys(f"{item}")
        pyautogui.click(100, 200)
    except:
        pass

elem = driver.find_element(By.ID, "formRealizarProva:botaoTerminarProva")
sleep(1)
elem.click()




