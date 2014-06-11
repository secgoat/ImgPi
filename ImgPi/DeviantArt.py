import requests
import xml.dom.minidom as minidom


class DeviantArt:

    def __init__(self):
        self.rssFeed = None #use this to holds the xml result from the rss feed

        self.imageList = [] #parse the sml and put the image links in here


    def getRSS(self):
        #self.rssFeed = requests.get('http://backend.deviantart.com/rss.xml?q=boost%3Apopular+cyberpunk') #rss by search
        self.rssFeed = requests.get('http://backend.deviantart.com/rss.xml?q=favby%3ATrissa%2F10465612&type=deviation') #rss by user favorites
        xml_dom = minidom.parseString(self.rssFeed.text)

        #need to pull <media:content to get a list of links
        #self.imageList = xml_dom.getElementsByTagNameNS('*', 'content')#[0].childNodes[0].nodeValue
        rssNodes = xml_dom.getElementsByTagNameNS('*', 'content')
        for i in rssNodes:
            #img = i.attributes['url'].value
            #self.imageList.append(img)
            print(i.attributes['url'].value)
            #print(i.attributes['url'].value)
            self.imageList.append(i.attributes['url'].value)
            #print(i.attributes.keys(), i.attributes.values())
        #for i in self.imageList:
        #    for attr, value in i.attributes.items():
        #        print(attr, value)
            #print(i.Name)


    def downloadRSSContent(self):
        """
        param imageList: list of http strings
        used to download images locally
        """
        DL_LIMIT = 5 #change or remove this when goign live to get max number of pics

        #there has to be a better way than manual iterators
        currentImage = 0;

        for image in self.imageList:
            if currentImage < DL_LIMIT:
                #recreate the url we pulled apart in the getImageList() function.
                #url = r'http://i.imgur.com/{}'.format(image) #don't need this as we are doig it a tad different now
                url = image #to make it easier to read down below image should be the full http of the image
                #debug: let us know what is being downloaded
                print('Current image being downloaded: ', url)
                #use response to get the URL
                response = requests.get(url)
                #set the path in which to save the images
                imgName = self.parseImageURL(url)
                path = r'./images/{}'.format(imgName)
                #open folder in 'wb' write binary mode
                fp = open(path, 'wb')
                #write the binary data to the disk
                fp.write(response.content)
                #close the file
                fp.close()
                #increase iteratoer
                currentImage += 1


    def parseImageURL(self, imgURL):
        #find the l;ast \ in the url to strip out the image name
        imgIndex = imgURL.rfind('/')
        imgName = imgURL[imgIndex+1:]
        print(imgName)

        return imgName #return just the file name

if __name__ == "__main__":
    dev = DeviantArt()
    dev.getRSS()
