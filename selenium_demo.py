
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://amazon.in')

driver.maximize_window()

driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('iphones')
driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()

lst = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal]")

print(str(len(lst))+ ' products found')

for i in lst:
    print(i.text)
    
driver.quit()
