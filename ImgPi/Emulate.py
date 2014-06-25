from bs4 import BeautifulSoup
import re
import requests

#http://www.nesfiles.com/Games.aspx for easy nes downloads nesfiles.com/{}/{}.nes  where {} = game name
#have to check pages for the ing <a id="ctl00_MainContent_lnkROM" href="/NES/720/720.nes"
#to find if there is a rom or not.

#get 'a' that starts with NES, then goto that page and look got a with id = ctl00_MainContent_lnkROM and catalog that
#href link

class NES:

    def __init__(self):
        self.get_url()

    def get_url(self):
        r = requests.get("http://www.nesfiles.com/Games.aspx")
        data = r.text
        soup = BeautifulSoup(data)
        #pull only the table that contians the game links
        table = soup.find_all('table', {"id": "ctl00_MainContent_tblGames"})
        for element in table:
            links = element.find_all('a')
            for a in links:
                print(a.get('href'))
                r2 = requests.get("http://www.nesfiles.com/{}".format(a.get('href')))
                data2 = r2.text
                soup2 = BeautifulSoup(data2)
                for link2 in soup2.find_all('a', {"id": "ctl00_MainContent_lnkROM"}):
                    print("     ", link2.get('href'))


if __name__ == "__main__":
    nes = NES()
