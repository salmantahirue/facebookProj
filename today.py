from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

search_url="https://www.facebook.com/"


driver.get(search_url)


# search_url = [
#     "https://www.facebook.com/photo/?fbid=1964219493751625&set=gm.661521518376525",
#     "https://www.facebook.com/photo/?fbid=10166069210810437&set=a.10151253087180437",
#     "https://www.facebook.com/photo/?fbid=10158609436502043&set=pcb.10158609375502043",
#     "https://www.facebook.com/photo/?fbid=472539254483713&set=gm.955972651727619",
#     "https://www.facebook.com/photo/?fbid=1348724675558020&set=gm.1637107149956702"
# ]


# for search_url in search_url:
#     driver.get(search_url)

