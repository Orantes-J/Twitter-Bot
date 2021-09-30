from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


email = ENTER ACCOUNT EMAIL
password = ENTER ACCOUNT PASSWORD

CHROMEDRIVER = "C://Users/Carlo/desktop/Development/chromedriver.exe"
driver = webdriver.Chrome(CHROMEDRIVER)
driver.maximize_window()

driver.get("https://youtube.com")
time.sleep(4)
search_input = driver.find_element_by_xpath('//input[@id="search"]')
search_input.send_keys("According to Lucky Naruto")
search_button = driver.find_element_by_id("search-icon-legacy")
time.sleep(2)
search_button.click()

time.sleep(3)
latest_video = driver.find_element_by_css_selector("yt-formatted-string.ytd-video-renderer").text
print(latest_video)

twitter_site = driver.get("https://twitter.com/?logout=1632963503676")

time.sleep(4)

scroll_down = driver.find_element_by_tag_name("body")
scroll_down.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

signin_method = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
signin_method.click()

signin = driver.find_element_by_css_selector("a.css-4rbku5")
signin.click()


time.sleep(3)
email_input = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
email_input.send_keys(email)
time.sleep(2)
next_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span')
next_button.click()



time.sleep(2)
password_input = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
password_input.send_keys(password)
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span')
login.click()

time.sleep(2)


tweet_msg = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span')
tweet_msg.send_keys(f"Hey guys, I am a python bot that serves famous youtuber 'According to Lucky'.\nHe has uploaded a new video by the name of '{latest_video.title()}'.\nMake sure to check it out!!\nBot out.")
tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
time.sleep(3)
tweet.click()

time.sleep(10)
driver.close()