import datetime
import json
import requests
import os
import ImgPiDisplay


#Imgur Client ID
CLIENT_ID = "efed10c55d16860"

display = ImgPiDisplay.ImgPiDisplay()

def displayImages():
    pass
   
def imgurDL(imageList):
    """
    param imageList: list of http strings
    used to dowload images locally
    """
    DL_LIMIT = 5
    #get the satetime for today
    #folder = datetime.datetime.today()
    #turn datetime into string
    #str_folder = str(folder)
    #replace illegal characters
    #str_foldername = str_folder.replace(':','.')
    #make folder based on datetime
    #os.mkdir(str(str_foldername))
    #iterator coutn for image list
    currentImage = 0;
    for image in imageList:
        if currentImage < DL_LIMIT:
            #recreate the url we pulled apart in the getImageList() function.
            url = r'http://i.imgur.com/{}'.format(image)
            #debug: let us know what is being downloaded
            print('Current image being downloaded: ', url)
            #use response to get the URL
            response = requests.get(url)
            #set the path in which to save the images
            path = r'./images/{}'.format(image)
            # this one saves the path in a datetiem folder  path = r'./{}/{}'.format(str_foldername,image)
            #open folder in 'wb' write binary mode
            fp = open(path, 'wb')
            #write the binary data to the disk
            fp.write(response.content)
            #close the file
            fp.close()
            #increase iteratoer
            currentImage += 1
    #print('Finished downloading images to {}'.format(str_foldername))

def getImageList(subreddit = 'cyberpunk', sort = 'time', page = 0, window = 'week' ):
    """
    Return an image list from a page on a subreddit gallery.

    param subreddit: string - valid Subreddit name. 'pics', 'wtf' etc.
    param sort: string - Time | Top defautls to time
    param page: integer - page number
    param window: string - change the date range of the request if the sort is "top",
        day | week | month | year | all, defaults to week
    """

    imageList = []

    #send the client id to the imgur API to get anopnymous access to the site.
    header = {"Content-Type": "text", "Authorization": "Client-ID " + CLIENT_ID}
    #compile the request along with ID headers
    #https://api.imgur.com/3/gallery/r/cyberpunk/top/all/0
    r = requests.get('https://api.imgur.com/3/gallery/r/{}/{}/{}/{}'.format(subreddit,sort,window,page), headers=header)
    #read tje text of the
    j = json.loads(r.text)

    #print the keys for the dict that is our resonse
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
        imageList.append(imgName)
        count += 1

    print("total links returned: " + str(count))
    imgurDL(imageList)
    #return imageList
    #print all keys for key data?  iim not even sure what this is im doing?  dicts
    #of dicts?
    #for i in j[u'data'][0]:
        #print(i)
     

if __name__ == "__main__":
    getImageList()
    while display.running:
        display.Update()
        display.Draw()
