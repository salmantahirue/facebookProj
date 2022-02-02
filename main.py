# WindowTab.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--disable-notifications')
# options.add_argument('disable-infobars')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.maximize_window()
search_url="https://www.facebook.com/"

driver.get(search_url)
# driver.implicitly_wait(5)

# email = driver.find_element(By.ID, "email")
# password = driver.find_element(By.ID, "pass")
# Login_button = driver.find_element(By.ID, "u_0_d_wM")


driver.find_element_by_id("email").send_keys("salmantahirue@gmail.com")
driver.find_element_by_id("pass").send_keys("$@lm@nF@ceb00k")
driver.implicitly_wait(5)

driver.find_element_by_css_selector('button[name="login"]').click()
# driver.find_element_by_css_selector('body[class="_6s5d _71pn _-kb segoe"]').click()
time.sleep(3)

# previous_height = driver.execute_script('return document.body.scrolHeight')
#
# while True:
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#
#     time.sleep(3)
#
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == previous_height:
#         break
#     previous_height = new_height


# element = driver.find_elements_by_tag_name('body')
#
# while True:
#     element.send_keys(Keys.PAGE_DOWN)
#     time.sleep(3)

time.sleep(5)

print(1)

# make a urls lists then open the urls to the new tap window

search_url = [
    "https://www.facebook.com/photo/?fbid=1964219493751625&set=gm.661521518376525",
    "https://www.facebook.com/photo/?fbid=10166069210810437&set=a.10151253087180437",
    "https://www.facebook.com/photo/?fbid=10158609436502043&set=pcb.10158609375502043",
    "https://www.facebook.com/photo/?fbid=472539254483713&set=gm.955972651727619",
    "https://www.facebook.com/photo/?fbid=1348724675558020&set=gm.1637107149956702"
]

for i in range(len(search_url)):
    driver.execute_script("window.open()")
    # driver.execute_script(f'''window.open("{search_url[i]}","test");''')
    driver.switch_to.window(driver.window_handles[i+1])
    driver.get(search_url[i])
    p_tag=driver.find_elements_by_tag_name("div")
    # time.sleep(2)
    for i in range(len(p_tag)):
        print(p_tag[i].text)

time.sleep(3)

# time.sleep(5)
# email.send_keys("salmantahirue@gmail.com")
# password.send_keys("$@lm@nF@ceb00k")
# Login_button.click()



# driver.quit()