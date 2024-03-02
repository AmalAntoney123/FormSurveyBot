from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Constants
LIMIT = 1
GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSeV775Ye7gS8n6a7Xf_iauIDR2zoH4l4WrLjfg6nopNfn0mQA/viewform'
SUBMIT_XPATH = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span'
BUTTON_XPATHS1 = [
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span',
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span',
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[2]/div/span',  
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[2]/div/span',  
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[2]/div/span',  
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span',
    ]
]

BUTTON_XPATHS2 = [
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span'
    ],
    [
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span',
    ]
]


def wait_and_click(driver, xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

def click_random_buttons(driver, button_list):
    random_index = random.randint(0, len(button_list) - 1)
    selected_button = button_list[random_index]
    wait_and_click(driver, selected_button)

def click_multiple_buttons(driver, button_list):
    num_clicks = random.randint(1, len(button_list))
    random_indices = random.sample(range(len(button_list)), num_clicks)

    for index in random_indices:
        selected_button = button_list[index]
        wait_and_click(driver, selected_button)

def form_fill_bot(driver, form_url, button_xpaths1, button_xpaths2):
    driver.get(form_url)

    for button_list in button_xpaths1:
        click_random_buttons(driver, button_list)

    for button_list in button_xpaths2:
        click_multiple_buttons(driver, button_list)

    wait_and_click(driver, SUBMIT_XPATH)

def main():
    driver = webdriver.Edge()

    for _ in range(LIMIT):
        form_fill_bot(driver, GOOGLE_FORM_URL, BUTTON_XPATHS1, BUTTON_XPATHS2)
    driver.quit()

if __name__ == "__main__":
    main()
