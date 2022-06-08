from lib2to3.pgen2 import driver
import time
import undetected_chromedriver as UC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys

RUTA_CHROMEDRIVER = ""

def main():
    browser = UC.Chrome(driver_executable_path=RUTA_CHROMEDRIVER, headless=True)
    browser.get('https://accounts.google.com/signin/v2/identifier')
    
    time.sleep(5)
    input_credenciales = browser.find_element(By.NAME, 'identifier')
    input_credenciales.send_keys('alexgallo91y@gmail.com')

    boton_next = browser.find_element(By.ID, 'identifierNext')
    boton_next.click()

    time.sleep(7)
    browser.save_screenshot('./debug.png')
    input_password = browser.find_element(By.NAME, 'password')
    input_password.send_keys('ChainsawmanAWS91')

    boton_next = browser.find_element(By.ID, 'passwordNext')
    boton_next.click()

    time.sleep(7)

if __name__ == "__main__":
    main()