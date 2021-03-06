from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def main():
    with sync_playwright() as p:
            word = []
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://www.livechat.com/typing-speed-test/#/')
            while True:
                html = page.inner_html('#app')
                soup = BeautifulSoup(html, 'html.parser')
                data = soup.find('div', {'class': 'tst-input'}) 
                text = data.find_all('div', {'class': 'tst-input-wrapper'}) 
                sec = soup.find('div',{'class': 'u-text-p3'})

                for items in text:
                    span = items.find_all('span')
                for words in span:
                    word.append(words.text)

                if sec.text != '00' and word:
                    for characters in word:          
                            page.fill('div#test-input', characters)
                            page.keyboard.press(' ')
                            #time.sleep(0.1)
                            
                word = []
                    
                    

main()
