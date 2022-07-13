from contextlib import closing
from urllib.request import urlopen

print("starting emonpi backup")
url = "http://dromotherm.ddns.net/backup/start?apikey=9664269b8d334ec24d4b686998a8ec86"
with closing(urlopen(url)) :
    pass
