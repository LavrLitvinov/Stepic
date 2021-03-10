from selenium import webdriver
browser = webdriver.Chrome()
import time
#browser.execute_script("document.title='Script executing';alert('Robots at work');")
try:
   

    browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait2.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:

    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()



