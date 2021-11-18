from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from random import randint, random
import time


def main():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://www.keybr.com/multiplayer')
            time.sleep(2)
            page.click('button[class=CybotCookiebotDialogBodyButton]')
            page.focus('#App')
            pos = 0
            words = []
            players = []
            

            while True:
                html = page.inner_html('#App')
                soup = BeautifulSoup(html, 'html.parser')
                data = soup.find('div', {'class': 'TextInput-fragment'}) 
                span = data.find_all('span')
                start = soup.find('div', {'class': 'Track-ticker'})
                progress = soup.find_all('span', {'class': 'Value'})
                for player in progress:
                    pos += 1
                    for stats in player:
                        players.append(stats)   
                
                for stuff in span:
                    stuff = stuff.text.replace('␣', ' ').replace('↵', ' ')
                    words.append(stuff)


                #Uncomment bellow lines for random mistakes


                # for _ in range(20):
                #     words.insert(randint(0, len(words)), ')')  
            
                
                if start.text == 'GO!' and players[-3].text != '100%':
                    for letter in words:
                        page.keyboard.press(letter)
                    time.sleep(4)

                pos = 0
                players = []
                words = []
                       

main()
