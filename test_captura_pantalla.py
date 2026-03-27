from selenium import webdriver

driver = webdriver.Chrome()
driver.get(" http://localhost:4322/")

# Ajusta altura total
total_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(1920, total_height)

driver.save_screenshot("pagina_completa.png")

driver.quit()