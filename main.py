# %%
# Imports
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import autoit
import time

# %%
driver = uc.Chrome()
driver.get("https://business.facebook.com/latest/reels_composer/?asset_id=101039866279077")

# %%
email = 'your_email'
password = 'your_password'

# %%
driver.find_element(By.XPATH, "//input[@type='text']").send_keys(email)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

driver.find_element(By.XPATH, "//button[@name='login']").click()
time.sleep(2)

# %%
def publish(url:str, video:str, captions:str=""):

    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Caption reel')]/../..//div[@role='presentation']/*"))).send_keys(captions)

    driver.find_element(By.XPATH, "//div[@role='button' and @aria-busy='false']").click()

    while True:
        try:
            time.sleep(2)
            autoit.control_send("[CLASS:#32770]","Edit1",video)
            autoit.control_click("[CLASS:#32770]", "Button1")
            time.sleep(0.1)
            break
        except:pass

    wait = WebDriverWait(driver, 25)

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(), 'Next')]/../../../..)[2]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Next')]/../../../.."))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(), 'Share')]/../../../..)[3]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(), 'Share')]/../../../..)[3]"))).click()


# %%
for _ in range(25):
    publish("https://business.facebook.com/latest/reels_composer/?asset_id=101039866279077", r"C:\Users\Hadi-PC\Documents\Bandicam\bandicam 2023-03-18 16-14-57-046.mp4", "test")

time.sleep(15)

