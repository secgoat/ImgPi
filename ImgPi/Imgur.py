import requests
import json


class Imgur:

    def __init__(self):
        self.subredditImages = None
        self.CLIENT_ID = "efed10c55d16860"
        self.subredditImageList = []


    def get_subreddit_gallery(self, subreddit='cyberpunk', sort='time', page=0, window='day'):
        """
        Return an image list from a page on a subreddit gallery.

        param subreddit: string - valid Subreddit name. 'pics', 'wtf' etc.
        param sort: string - Time | Top defautls to time
        param page: integer - page number
        param window: string - change the date range of the request if the sort is "top",
            day | week | month | year | all, defaults to week
        """

        self.subredditImageList = []

        #send the client id to the imgur API to get anopnymous access to the site.
        header = {"Content-Type": "text", "Authorization": "Client-ID " + self.CLIENT_ID}

        #compile the request along with ID headers
        #for reference the url nomenclature is : https://api.imgur.com/3/gallery/r/cyberpunk/top/all/0
        r = requests.get('https://api.imgur.com/3/gallery/r/{}/{}/{}/{}'
                         .format(subreddit,sort,window,page), headers=header)

        #read the text of the respomse
        j = json.loads(r.text)

        #print the keys for the dict that is our response
        for key in j:
            print(key)
        count = 0
        for image in j[u'data']:
            print(image['link'])
            imgURL = image['link']
            #find the l;ast \ in the url to strip out the image name
            #imgIndex = imgURL.rfind('/')
            #imgName = imgURL[imgIndex+1:]
            #print(imgName)
            self.subredditImageList.append(imgURL)
            count += 1
        print("total links returned: " + str(count))

    def download_from_imgur(self):
        """
        param imageList: list of http strings
        used to download images locally
        """
        DL_LIMIT = 5 #change or remove this when goign live to get max number of pics

        #there has to be a better way than manual iterators
        currentImage = 0;

        for image in self.subredditImageList:
            if currentImage < DL_LIMIT:
                #recreate the url we pulled apart in the getImageList() function.
                #url = r'http://i.imgur.com/{}'.format(image) #don't need this as we are doig it a tad different now
                url = image #to make it easier to read down below image should be the full http of the image
                #debug: let us know what is being downloaded
                print('Current image being downloaded: ', url)
                #use response to get the URL
                response = requests.get(url)
                #set the path in which to save the images
                imgName = self.parse_image_url(url)
                path = r'./images/{}'.format(imgName)
                #open folder in 'wb' write binary mode
                fp = open(path, 'wb')
                #write the binary data to the disk
                fp.write(response.content)
                #close the file
                fp.close()
                #increase iteratoer
                currentImage += 1

    def parse_image_url(self, imgURL):
        #find the l;ast \ in the url to strip out the image name
        imgIndex = imgURL.rfind('/')
        imgName = imgURL[imgIndex+1:]
        print(imgName)

        return imgName #return just the file name

if __name__ == "__main__":
    img = Imgur()
    img.get_subreddit_gallery()
    img.download_from_imgur()


