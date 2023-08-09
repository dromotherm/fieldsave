from contextlib import closing
from urllib.request import urlopen
import os
APIKEY=os.environ('RWKEY')

print("starting emonpi backup")
url = "http://dromotherm.ddns.net/backup/start?apikey=APIKEY"
with closing(urlopen(url)) :
    pass
