from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def formFillBot(form_url, button_xpaths1):
    driver = webdriver.Edge()
    driver.get(form_url)
    time.sleep(1)

    for button_list in button_xpaths1:
        random_index = random.randint(0, len(button_list) - 1)
        selected_button = driver.find_element(By.XPATH, button_list[random_index])
        selected_button.click()
    
    for button_list in button_xpaths2:
        num_clicks = random.randint(1, len(button_list))
        random_indices = random.sample(range(len(button_list)), num_clicks)

        # Click the randomly chosen buttons
        for index in random_indices:
            selected_frequent_btn = driver.find_element(By.XPATH, button_list[index])
            selected_frequent_btn.click()

    #submit button
    submitXpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span'
    submit_btn = driver.find_element(By.XPATH, submitXpath)
    submit_btn.click()
    time.sleep(2)

# Replace url with the actual URL of your Google Form
google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeV775Ye7gS8n6a7Xf_iauIDR2zoH4l4WrLjfg6nopNfn0mQA/viewform'

# Define your list of XPaths
button_xpaths1 = [
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
button_xpaths2 =[
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

#enter number of response needed in limit
limit = 10
for i in range(0,limit):
    formFillBot(google_form_url, button_xpaths1)
