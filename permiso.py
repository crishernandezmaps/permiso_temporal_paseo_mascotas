from selenium import webdriver
import time
from my_data import personal_data
# from your_data import personal_data


def t_sleep():
    return time.sleep(3)


def get_permit():
    chrome_driver = r"/Users/tremen/Downloads/chromedriver"  # Path to Chromedriver in your machine. Download from here: https://chromedriver.chromium.org/downloads
    driver = webdriver.Chrome(executable_path=chrome_driver)

    # Get url for pet walking permit
    driver.get('https://comisariavirtual.cl/tramites/iniciar/67')  # Walk your pet url

    # Clicking RUT
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/fieldset/div[3]/p/a').click()

    # Filling form
    # Name
    driver.find_element_by_xpath('//*[@id="1207"]').send_keys(personal_data()['name'])
    # RUT
    driver.find_element_by_xpath('//*[@id="1209"]').send_keys(personal_data()['rut'])
    # Identifier
    driver.find_element_by_xpath('//*[@id="1301"]').send_keys(personal_data()['serie_carnet'])
    # Region
    driver.find_element_by_xpath('//*[@id="regiones_1210_chosen"]/a').click()
    driver.find_element_by_xpath('//*[@id="regiones_1210_chosen"]/div/div/input').send_keys(personal_data()['region'])
    driver.find_element_by_xpath('//*[@id="regiones_1210_chosen"]/div/ul/li/em').click()
    # Commune
    driver.find_element_by_xpath('//*[@id="comunas_1210_chosen"]/a').click()

    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="comunas_1210_chosen"]/div/div/input').send_keys(personal_data()['comuna'])
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[6]/div/div[2]/div/ul/li/em').click()
    time.sleep(3)

    # Address
    driver.find_element_by_xpath('//*[@id="1211"]').send_keys(personal_data()['direccion'])  # 35 characters

    # Meaning --> Uncomment if needed
    # driver.find_element_by_xpath('//*[@id="1212"]').send_keys('Pasear mascotas')

    # Complete trip
    driver.find_element_by_xpath('//*[@id="Ida - Regreso"]').click()

    # Terms
    driver.find_element_by_xpath('//*[@id="en_caso_de_comprobarse_falsedad_en_la_declaracion_de_la_causal_invocada_para_requerir_el_presente_documento_se_incurrira_en_las_penas_del_art_210_del_codigo_penal"]').click()
    time.sleep(3)

    # Next
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[14]/button').click()
    time.sleep(3)
    window_after = driver.window_handles[0]

    # print(window_after)
    driver.switch_to.window(window_after)

    # PDF
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/fieldset/div[3]/p/a').click()
    time.sleep(10)

    driver.quit()


if __name__ == '__main__':
    get_permit()
