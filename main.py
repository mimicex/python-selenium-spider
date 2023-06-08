from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options  import Options
from time                               import gmtime, strftime
from selenium.webdriver.support.ui      import WebDriverWait


option = webdriver.ChromeOptions()


option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')
gui = False
width = 1024
height = 768
# 無GUI模式，如果打開
if gui:
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument('--no-sandbox')
option.add_argument("--lang=zh-tw")

# 手機模擬模式
#mobile_emulation = {
#    "deviceMetrics": { "width": int(width), "height": int(height), "pixelRatio": 3.0 }
#}
#option.add_experimental_option("mobileEmulation", mobile_emulation)
# 請去 https://chromedriver.chromium.org/downloads 下載你版本的 chromedriver
# 將檔案放置以下路徑或別的位置，記得給他權限
chrome_driver_path = r'/usr/bin/chromedriver'

driver = webdriver.Chrome(
    executable_path      = chrome_driver_path,
    desired_capabilities = DesiredCapabilities.CHROME, 
    chrome_options       = option
)

driver.get('https://tw.yahoo.com')

driver.close()
driver.quit()