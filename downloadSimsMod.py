#! Python3
# downloadSimsmod.py - Downloads every mod in mod list in .txt file

from sys import argv
import requests, os, bs4, unshortenit, time
import webbrowser
from urllib.request import Request, urlopen

if len(argv) != 3:
	close("Usage: python downloadSimsMod input output")
	
outFile = argv[2]
	
os.makedirs("%s" % outFile, exist_ok=True) # Store the file in the output folder
modList = open(argv[1])

# print ("Downloading from %r % argv[1]...)

result = "Download link not found"

for url in modList.readlines():
	print("Currently downloading from %s" % url)
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	soup = bs4.BeautifulSoup(urlopen(req).read(), "lxml")

	for link in soup.find_all(attrs={"title": 'Wait 5 seconds, then click "Skip Ad"'}):
		result = (link.get("href"))
	
# The above code finds the main download link
	
#	download = "Not found"
	print (result)
#	# webbrowser.open(result)
#	req = Request(result, headers={'User-Agent': 'Mozilla/5.0'})
	soup = bs4.BeautifulSoup(urlopen(req).read(), "lxml")
	
#	for link in soup.find_all(attrs={"id": "skip_button"}):
#		time.sleep(5)
#		download = link.get("href")
		
#	print (download)

# TODO: Implement ad fly bypassing
# TODO: Implement to download automatically without browser
# TODO: Put files into the output file
	
modList.close()