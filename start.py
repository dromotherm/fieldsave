from contextlib import closing
from urllib.request import urlopen
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", action="store")
p_args = parser.parse_args()

print("starting emonpi backup")
url = "http://dromotherm.ddns.net/backup/start?apikey=p_args.key"
with closing(urlopen(url)) :
    pass
