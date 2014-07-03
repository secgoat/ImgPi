from bs4 import BeautifulSoup
import json
import os
import requests
import time

from ImgPiMenu import ImgPiMenu, ImgPiMenuItem

#http://www.nesfiles.com/Games.aspx for easy nes downloads nesfiles.com/{}/{}.nes  where {} = game name
#have to check pages for the ing <a id="ctl00_MainContent_lnkROM" href="/NES/720/720.nes"
#to find if there is a rom or not.

#get 'a' that starts with NES, then goto that page and look got a with id = ctl00_MainContent_lnkROM and catalog that
#href link

class NES:

    def __init__(self):
        self.site_name = 'nesfiles'
        self.link = "http://www.nesfiles.com/Games.aspx"
        self.json_config_file = None # read the json file into this
        self.site_info = {} # read in from json the info about the site, when it was last visited and what pages have links etc.
        self.load_site_info()

        self.menu_items = []
        self.get_menu_items()
        self.menu = NES_Menu(self.menu_items)



        #self.get_url()

    def load_site_info(self):
        if not os.path.isfile("site_infos.json"):
            #write the file with this sites basic info so the file exists
            site_infos = {
                "nesfiles" : {
                    'date_checked' : 'none',
                    'roms' : None
                }
            }
            #write the file so it exists
            with open("site_infos.json", 'w') as f:
                f.write(json.dumps(site_infos))
            self.get_url()
            #now read it into a local variable to make changes as neccescary
            #with open("site_infos.json", 'r') as f:
                #self.json_config_file =json.loads(f.read())
        else:
            with open("site_infos.json", 'r') as f:
                self.json_config_file =json.loads(f.read())

    def update_site_info(self):
        with open("site_infos.json", 'w') as f:
                f.write(json.dumps(self.site_info))

    def get_url(self):

        date = time.strftime("%x")
        roms = {} # add keys with dicts as value {"MArio Borthers" : {'title' : "super Mario Brothers", 'link' : "site_name/mariobrothers/mariobrothers.rom", }}
        r = requests.get(self.link)
        data = r.text
        soup = BeautifulSoup(data)
        #pull only the table that contians the game links
        table = soup.find_all('table', {"id": "ctl00_MainContent_tblGames"})
        for element in table:
            links = element.find_all('a')
            for a in links:
                #print(a.text) gives me just the title
                #print(a.get('href')) #gives me the actuallink
                r2 = requests.get("http://www.nesfiles.com/{}".format(a.get('href')))
                data2 = r2.text
                soup2 = BeautifulSoup(data2)
                for link2 in soup2.find_all('a', {"id": "ctl00_MainContent_lnkROM"}):
                    for title in soup2.find_all('h1', {"id" : "ctl00_MainContent_hdrGame"}):
                        print("     ", title.contents) #key / title
                    print("     ", link2.get('href')) #link
                    roms[title.contents[0]] = link2.get('href')

        self.site_info[self.site_name] = {'date_checked' : date, 'roms' : roms}
        self.update_site_info()

    def get_menu_items(self):
        roms = self.json_config_file[self.site_name]['roms'] #just pull roms thats all we care about for now
        letters = []
        seen = set() #use a set to keep a unique list
        #pull all the keys form the roms dict and get just the first char of it
        for key in roms:
            letters.append(key[0])

        #nwo dig through the letters list and dedupe it into the set, fucking balck magic I tell you what!
        for char in letters:
            deduped = [x for x in char if x not in seen]
            seen.update(deduped)
        self.menu_items = sorted(seen)
        print(sorted(seen))

    def draw(self, screen):
        self.menu.draw(screen)

    def update(self, time, key):
        self.menu.update(time, key)

class NES_Menu(ImgPiMenu):

    def __init__(self, menu_items):
        ImgPiMenu.__init__(self, menu_items)



class NES_Menu_Item(ImgPiMenuItem):

    def __init__(self):
        super.__init__()

if __name__ == "__main__":
    nes = NES()


