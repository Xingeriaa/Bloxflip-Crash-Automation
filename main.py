from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import json

with open("config.json", "r") as openfile:
    json_object = json.load(openfile)

UserName = json_object["name"]
Password = json_object["pass"]
OriBetAmmount = json_object["bet"]
Multiplier = json_object["multiplier"]

driver = webdriver.Chrome()
driver.get("https://bloxflip.com")
WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)
time.sleep(5)
try:
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Understood! 🕹️')]")
        )
    ).click()
except:
    pass
driver.find_element(
    By.XPATH, "//button[@id='onesignal-slidedown-cancel-button']"
).click()
driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
driver.find_element(
    By.XPATH, '//input[@placeholder="What\'s your Roblox username? Type it here!"]'
).send_keys(UserName)
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@aria-label='Sign-in modal']//div[3]//div[1]//div[1]//div[1]")
    )
).click()
driver.implicitly_wait(1)

parent_window_handler = driver.window_handles[0]


def PressDownArrow():
    ActionChains(driver).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()


for x in range(19):
    driver.implicitly_wait(0.25)
    PressDownArrow()
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
driver.find_element(By.XPATH, "(//button[normalize-space()='Continue'])[1]").click()
time.sleep(4)
driver.find_element(By.XPATH, "(//button[normalize-space()='Yes'])[1]").click()

time.sleep(5)

sub_window_handler = driver.window_handles[-1]
driver.switch_to.window(sub_window_handler)

WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)

driver.find_element(By.XPATH, "(//input[@id='login-username'])[1]").send_keys(UserName)
driver.find_element(By.XPATH, "(//input[@id='login-password'])[1]").send_keys(Password)
driver.find_element(
    By.XPATH,
    "/html[1]/body[1]/div[3]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]",
).click()
time.sleep(2)
WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)
time.sleep(2)
WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/button[2]")
    )
).click()
time.sleep(2)
WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)
time.sleep(2)
WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)
driver.get("https://bloxflip.com/crash")
time.sleep(2)
WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)
driver.switch_to.window(parent_window_handler)
driver.close()
driver.switch_to.window(sub_window_handler)
CurrentBalance = float(
    driver.find_element(
        By.XPATH, "//span[@class='text_text__fMaR4 text_regular16__7x_ra']//span"
    ).get_attribute("innerHTML")
)
MainText = driver.find_element(By.XPATH, "(//button)[14]").get_attribute("innerHTML")
while driver.find_element(
    By.XPATH,
    "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
).get_attribute("value") != str(OriBetAmmount):
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
    ).clear()
    time.sleep(0.5)
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
    ).send_keys(OriBetAmmount)
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]",
    ).clear()
    time.sleep(0.5)
    driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]",
    ).send_keys(Multiplier)
driver.find_element(By.XPATH, "(//button)[14]").click()
BeforeBalance = CurrentBalance - OriBetAmmount

BeforeBet = datetime.timestamp(datetime.now())
Result = "Nah"

BetAmmount = OriBetAmmount

while True:
    CurrentBalance = float(
        driver.find_element(
            By.XPATH, "//span[@class='text_text__fMaR4 text_regular16__7x_ra']//span"
        ).get_attribute("innerHTML")
    )
    MainText = driver.find_element(By.XPATH, "(//button)[14]").get_attribute(
        "innerHTML"
    )
    if float(CurrentBalance) > BetAmmount:
        if MainText == "Join game" or MainText == "Join next game":
            if Result == "Won":
                while driver.find_element(
                    By.XPATH,
                    "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
                ).get_attribute("value") != str(OriBetAmmount):
                    driver.find_element(
                        By.XPATH,
                        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
                    ).clear()
                    time.sleep(0.5)
                    driver.find_element(
                        By.XPATH,
                        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
                    ).send_keys(OriBetAmmount)
                    driver.find_element(
                        By.XPATH,
                        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]",
                    ).clear()
                    time.sleep(0.5)
                    driver.find_element(
                        By.XPATH,
                        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]",
                    ).send_keys(Multiplier)
                driver.find_element(By.XPATH, "(//button)[14]").click()
                BeforeBalance = CurrentBalance
                Result = "Nah"
                print("Did a new won bet")
            elif Result == "Lost":
                while driver.find_element(
                    By.XPATH,
                    "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
                ).get_attribute("value") != str(BetAmmount):
                    driver.find_element(
                        By.XPATH,
                        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
                    ).clear()
                    time.sleep(0.5)
                    driver.find_element(
                        By.XPATH,
                        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]",
                    ).send_keys(BetAmmount)
                    driver.find_element(
                        By.XPATH,
                        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]",
                    ).clear()
                    time.sleep(0.5)
                    driver.find_element(
                        By.XPATH,
                        "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]",
                    ).send_keys(Multiplier)
                driver.find_element(By.XPATH, "(//button)[14]").click()
                BeforeBalance = CurrentBalance
                Result = "Nah"
                print("Did a new lost bet")
            elif Result == "Nah":
                if CurrentBalance < BeforeBalance:
                    BetAmmount *= 2
                    Result = "Lost"
                elif CurrentBalance > BeforeBalance:
                    BetAmmount = OriBetAmmount
                    Result = "Won"

        elif MainText == "Cashout" or MainText == "CancelBet":
            pass
    time.sleep(1)
