from contextlib import closing
from urllib.request import urlopen
import os
APIKEY=os.environ.get("RWKEY")
print(APIKEY)

print("starting emonpi backup")
url = "http://dromotherm.ddns.net/backup/start?apikey=APIKEY"
with closing(urlopen(url)) :
    pass
