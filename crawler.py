import urllib2
from bs4 import BeautifulSoup as BSHTML

def download_file(url,path=None,fileName=None):

    if fileName != None:
        file_name = fileName
    else: 
        file_name = url.split('/')[-1]
    
    link = file_name
    if path != None:
        link=path+file_name

    u = urllib2.urlopen(url)
    f = open(link, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()

def get_img_tags(url):
    # Get all images sorce from page
    print "Getting all src from img tags of " + url
    page = urllib2.urlopen(url)
    soup = BSHTML(page, "html.parser") #u can also use this -> BSHTML(page)
    images = soup.findAll('img')

    return len(images),images

def donwload_all_images_from_url(link,imgTags,qtdImgTags,path=None):

    qtdImages = str(qtdImgTags)

    print "founded "+ qtdImages +" images from "+ link

    print "starting download images..."

    count = 0
    for image in imgTags:

        protocol = image['src'].split('/')[0]

        if protocol != "http:" and protocol != "https:":
            image['src'] = link + image['src']
        
        enumerator = "image "+ str(count+1) + " of "+ qtdImages

        #download img
        print ("\n\n"+enumerator)
        print ('link: '+ image['src'])
        try:
            download_file(image['src'],path) #u can also dont put a path 
            count += 1
        except Exception:
            print "error trying to download file"
            pass
        

    print "\n\nTotal images downloaded from "+link +" "+ str(count)+" of "+qtdImages

link = 'https://youtube.com'
path = 'images/'

qtdImgTags, imgTags = get_img_tags(link)
donwload_all_images_from_url(link,imgTags,qtdImgTags,path) #u can also dont put a path 