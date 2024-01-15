import webbrowser as wb
import os 


def workauto():
    codepath = "application path"
    os.startfile(codepath)
    browser_path ='web_brower_path %s'
    
    URLS = ("sudipniroula.com.np","google.com")
    for url in URLS:
      wb.get(browser_path).open(url)
        
workauto()
    