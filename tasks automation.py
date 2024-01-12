import webbrowser as wb


def workauto():
    browser_path ='web_brower_path %s'
    
    URLS = ("sudipniroula.com.np","google.com")
    for url in URLS:
      wb.get(browser_path).open(url)
        
workauto()
    