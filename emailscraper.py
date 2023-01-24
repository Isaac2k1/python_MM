# --------------------------------------------------------------------
# -- Python Script File
# -- Created on 2023-01-24 10:25:32
# -- Author: username
# -- Comment: .
# --------------------------------------------------------------------
import sys
if 'DIAdem' in sys.modules:
    from DIAdem import Application as dd

    if dd.AppEnableScriptDebugger:
        import debugpy
        debugpy.configure(python = sys.prefix + '\\python.exe')
        if not debugpy.is_client_connected():
            try:
                debugpy.listen(5678)
            except:
                pass
            debugpy.wait_for_client()

# --------------------------------------------------------------------
# -- Beginning of user code --
from selenium import webdriver
import time
import re

# PATH = 'C:\Users\MM1229\.cache\selenium\chromedriver\win32\109.0.5414.74\chromedriver.exe'
PATH = 'C:\Program Files (x86)\chromedriver.exe'

l=list()
o={}

target_url = "https://hitachipowergrids.sharepoint.com/sites/LABwiki/SitePages/DUG.aspx"
# "https://www.randomlists.com/email-addresses"
driver=webdriver.Chrome(PATH)
driver.get(target_url)
print("sleeping now for 33s")
time.sleep(33)

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
html = driver.page_source
emails = re.findall(email_pattern, html)

time.sleep(5)
print(emails)
driver.close()

print("DONE")