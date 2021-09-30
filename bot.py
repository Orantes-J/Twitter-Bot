from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# TWITTER ACCOUNT INFO
email = ENTER ACCOUNT EMAIL
password = ENTER ACCOUNT PASSWORD

# CHROMEDRIVER EXE FILE PATH
CHROMEDRIVER = "C://Users/Carlo/desktop/Development/chromedriver.exe"
driver = webdriver.Chrome(CHROMEDRIVER)
driver.maximize_window()

# GETTING MOST RECENT VIDEO FROM SPECIFIC YOUTBER
driver.get("https://youtube.com")
time.sleep(4)
search_input = driver.find_element_by_xpath('//input[@id="search"]')
search_input.send_keys("According to Lucky Naruto")
search_button = driver.find_element_by_id("search-icon-legacy")
time.sleep(2)
search_button.click()

# GRABBING TEXT FROM HTML TAG
time.sleep(3)
latest_video = driver.find_element_by_css_selector("yt-formatted-string.ytd-video-renderer").text
print(latest_video)

# NOW GOING TO TWITTER URL
twitter_site = driver.get("https://twitter.com/?logout=1632963503676")

# SCROLLING PAGE TO MAKE SPECIFIC ELEMENT VISIBLE
time.sleep(4)
scroll_down = driver.find_element_by_tag_name("body")
scroll_down.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

# CLICKING ON SIGN-IN BUTTON
signin_method = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
signin_method.click()
signin = driver.find_element_by_css_selector("a.css-4rbku5")
signin.click()

# ENTERING EMAIL INTO INPUT FIELD
time.sleep(3)
email_input = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
email_input.send_keys(email)
time.sleep(2)
next_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span')
next_button.click()

# ENTERING PASSORD INTO PASWORD INTO INPUT FIELD
time.sleep(2)
password_input = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
password_input.send_keys(password)
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span')
login.click()

# MAKING A TWEET WITH A FORMATTED STRING, TITLE METHOD IS OPTIONAL, THIS IS FOR PRESENTATION OF THE THE STRING I GRABBED FORM YOUTUBE
time.sleep(2)
tweet_msg = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span')
tweet_msg.send_keys(f"Hey guys, I am a python bot that serves famous youtuber 'According to Lucky'.\nHe has uploaded a new video by the name of '{latest_video.title()}'.\nMake sure to check it out!!\nBot out.")

# SUBMITTING TWEET
tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
time.sleep(3)
tweet.click()

# CLOSING OUT PROGRAM
time.sleep(10)
driver.close()
