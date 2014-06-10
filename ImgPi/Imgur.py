import requests
import json

class Imgur:

    def __init__(self):
        self.subredditImages = None
        self.CLIENT_ID = "efed10c55d16860"
        self.subredditImageList = []


    def getSubredditGallery(self, subreddit='cyberpunk', sort='time', page=0, window='day'):
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
        #now print what?  fuck if i knwo btu it prints the damn image link
        count = 0
        for image in j[u'data']:
            print(image['link'])
            imgURL = image['link']
            #find the l;ast \ in the url to strip out the image name
            imgIndex = imgURL.rfind('/')
            imgName = imgURL[imgIndex+1:]
            print(imgName)
            self.subredditImageList.append(imgName)
            count += 1

        print("total links returned: " + str(count))




