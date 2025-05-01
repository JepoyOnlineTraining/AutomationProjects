
import time
from playwright.sync_api import sync_playwright

URL = 'https://google.com'
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False)


page = browser.new_page(
    java_script_enabled=True,
    viewport={'width':200, 'height':100}

)

page.goto(URL, wait_until='load')

time.sleep(10)

page.close()
browser.close()
playwright.stop()