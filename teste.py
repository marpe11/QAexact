from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


PATH = "/Users/marcus.pereira/Documents/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

driver.firstname_xpath = "//input[@placeholder='First Name']"
driver.lastname_xpath = "//input[@placeholder='Last Name']"
driver.address_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]"
driver.email_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]"
driver.phone_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]"
driver.gender_click_xpath = "//label[1]//input[1]"
driver.hobbies_click_xpath = "//input[@id='checkbox2']"
driver.language_click_xpath = "//div[@id='msdd']"
driver.English_click_xpath = "//a[contains(text(),'English')]"
driver.skills_click_xpath = "//select[@id='Skills']"
driver.country_click_xpath = "// select[ @ id = 'countries']"
driver.year_click_xpath = "// select[ @ id = 'yearbox']"
driver.month_click_xpath = "//select[@placeholder='Month']"
driver.day_click_xpath = "//select[@id='daybox']"
driver.password_click_xpath = "//input[@id='firstpassword']"
driver.confirm_click_xpath = "//input[@id='secondpassword']"
driver.submit_click_xpath = "//button[@id='submitbtn']"

driver.find_element_by_xpath(driver.firstname_xpath).send_keys('Primeiro Nome')
driver.find_element_by_xpath(driver.lastname_xpath).send_keys('Ultimo Nome')
time.sleep(5)
driver.find_element_by_xpath(driver.address_xpath).send_keys('Endereço ficticio floripa 18181818')
driver.find_element_by_xpath(driver.email_xpath).send_keys('novoQA@exact.com.br')
driver.find_element_by_xpath(driver.phone_xpath).send_keys('1234567890')
time.sleep(5)
driver.find_element_by_xpath(driver.gender_click_xpath).click()
driver.find_element_by_xpath(driver.hobbies_click_xpath).click()
time.sleep(5)
driver.find_element_by_xpath( driver.language_click_xpath).click()
driver.find_element_by_xpath(driver.English_click_xpath).click()
time.sleep(5)
skills = driver.find_element_by_xpath(driver.skills_click_xpath)
drp = Select(skills)
drp.select_by_visible_text("Analytics")
driver.implicitly_wait(10)
time.sleep(5)
country = driver.find_element_by_xpath(driver.country_click_xpath)
drp1 = Select(country)
drp1.select_by_visible_text("Brazil")
driver.find_element_by_xpath(driver.submit_click_xpath).click()
driver.implicitly_wait(10)
year = driver.find_element_by_xpath(driver.year_click_xpath)
drp2 = Select(year)
drp2.select_by_visible_text("1982")
driver.implicitly_wait(10)
month = driver.find_element_by_xpath(driver.month_click_xpath)
drp3 = Select(month)
drp3.select_by_visible_text("January")
driver.implicitly_wait(10)
day = driver.find_element_by_xpath(driver.day_click_xpath)
drp4 = Select(day)
drp4.select_by_visible_text("18")
driver.implicitly_wait(10)
driver.find_element_by_xpath(driver.password_click_xpath).send_keys('Password@1')
driver.find_element_by_xpath(driver.confirm_click_xpath).send_keys('Password@1')
time.sleep(5)
driver.find_element_by_xpath(driver.submit_click_xpath).click()








