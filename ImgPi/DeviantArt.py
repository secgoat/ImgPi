import requests
import xml.dom.minidom as minidom

class DeviantArt:

    def __init__(self):
        self.rssFeed = None #use this to holds the xml result from the rss feed

        self.imageList = None #parse the sml and put the image links in here


    def getRSS(self):
        #self.rssFeed = requests.get('http://backend.deviantart.com/rss.xml?q=boost%3Apopular+cyberpunk') #rss by search
        self.rssFeed = requests.get('http://backend.deviantart.com/rss.xml?q=favby%3ATrissa%2F10465612&type=deviation') #rss by user favorites
        xml_dom = minidom.parseString(self.rssFeed.text)

        #need to pull <media:content to get a list of links
        self.imageList = xml_dom.getElementsByTagNameNS('*', 'content')#[0].childNodes[0].nodeValue
        for i in self.imageList:
            print(i.attributes['url'].value)
            #print(i.attributes.keys(), i.attributes.values())
        #for i in self.imageList:
        #    for attr, value in i.attributes.items():
        #        print(attr, value)
            #print(i.Name)





if __name__ == "__main__":
    dev = DeviantArt()
    dev.getRSS()
