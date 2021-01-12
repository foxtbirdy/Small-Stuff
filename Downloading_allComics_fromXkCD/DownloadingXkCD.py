import requests , os , bs4

# Please note that the code can be found on the Al Sweigart's book called
# Automate the boring stuff with python

url = "http://xkcd.com"
os.makedirs("xkcd" , exist_ok = True)

while not url.endswith("#"):
	print("Downloading pages %s..." % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

	comicElem = soup.select("#comic img")
	if comicElem == []:
		print("Couldn't found the image")
	else:
		comicURL = "http:" + comicElem[0].get("src")
		print("Downloading Images %s..." % (comicURL))
		res = requests.get(comicURL)
		res.raise_for_status()

		imageFile = open(os.path.join("xkcd" , os.path.basename(comicURL)) , "wb")
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()


	prevLink = soup.select('a[rel="prev"]')[0]
	url = "http://xkcd.com" + prevLink.get("href")

print("Done.")
