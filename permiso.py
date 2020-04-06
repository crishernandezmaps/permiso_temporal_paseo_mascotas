from my_data import personal_data
# from your_data import personal_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time
import os
import datetime

# Settings
chrome_options = Options()
ua = UserAgent()
userAgent = ua.random
chrome_options.add_argument(f'user-agent={userAgent}')
chrome_options.add_argument('--window-size=640,1080')

# Path to Chromedriver in your machine (https://chromedriver.chromium.org/downloads)
chrome_driver = r"/Users/tremen/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)

# Get url for pet walking permit
driver.get('https://comisariavirtual.cl/tramites/iniciar/67')


def t_sleep():
    return time.sleep(5)


def hour_to_go_out():
    d = str(datetime.datetime.now()).split(' ')[-1].split(':')[0]
    return str(int(d) + 1)


def to_wait(xpath_string):
    click_on = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_string)))
    click_on.click()
    t_sleep()


def get_permit():
    try:
        # Clicking RUT
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/fieldset/div[3]/p/a').click()

        # Name
        driver.find_element_by_xpath('//*[@id="1868"]').send_keys(personal_data()['name'])

        # RUT
        driver.find_element_by_xpath('//*[@id="1869"]').send_keys(personal_data()['rut'])

        # Region
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[5]/div/div[1]/a').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[5]/div/div[1]/div/div/input').send_keys(personal_data()['region'])
        t_sleep()
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[5]/div/div[1]/div/ul/li').click()
        t_sleep()

        # Commune
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[5]/div/div[2]/a').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[5]/div/div[2]/div/div/input').send_keys(personal_data()['comuna'])
        t_sleep()
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[5]/div/div[2]/div/ul/li').click()

        # Address
        driver.find_element_by_xpath('//*[@id="1871"]').send_keys(personal_data()['direccion'])

        # Complete trip
        driver.find_element_by_xpath('//*[@id="Ida - Regreso"]').click()
        t_sleep()

        # Time
        to_wait('//*[@id="1876_chosen"]/a/span')
        driver.find_element_by_xpath('//*[@id="1876_chosen"]/div/div/input').send_keys(hour_to_go_out())
        t_sleep()
        driver.find_element_by_xpath('//*[@id="1876_chosen"]/div/ul/li').click()
        t_sleep()

        # Terms
        driver.find_element_by_xpath('//*[@id="en_caso_de_comprobarse_falsedad_en_la_declaracion_de_la_causal_invocada_para_requerir_el_presente_documento_se_incurrira_en_las_penas_del_art_210_del_codigo_penal"]').click()
        t_sleep()

        # Siguiente
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[13]/button').click()
        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)
        t_sleep()

        # PDF
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/fieldset/div[3]/p/a').click()
        t_sleep()

        os.system('cd ~/Downloads && open .')
        print('All done')

        # Finally, quit the browser
        driver.quit()
        
    except Exception as e:
        print(e)
        driver.quit()


if __name__ == '__main__':
    get_permit()
