import requests
from bs4 import BeautifulSoup

r = requests.get("https://odbrmls.rapmls.com/scripts/mgrqispi.dll?APPNAME=Nyst&PRGNAME=MLSLogin&ARGUMENT=D%2BITRXr5DvB0Ykf95z6XGo41jObIjmrKAeI04j2bqs0%3D&KeyRid=1&Include_Search_Criteria=on&CurrentSID=166525063&MLS_Origin=OTSE&Report_Code_String=&SID=&Report_Format=&Type_Of_Search=&Search_Type=AV")
doc = BeautifulSoup(r.text, 'html.parser')

class CrawledArticle():
	def __init__(self, listing_num, address, price):
		self.listing_num = listing_num
		self.address = address
		self.price = price
		#self.beds = beds
		#self.baths = baths
		
class ListingFetcher():
	def fetch(self):
		listings = []
		
		for b in doc.find_all("b"):
			if "Listing #" in b.text:
				listing_num = b.text
			if "Listing Price" in b.text:
				price = b.text
		
		for s in doc.find_all("strong"):
			address = s.text
		
		crawled = CrawledArticle(listing_num, price, address)
		listings.append(crawled)
		return(listings)
		

import csv 
fetcher = ListingFetcher()

with open('crawler_output.csv', 'w', newline='') as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for listing in fetcher.fetch():
       articlewriter.writerow([listing.listing_num, listing.price, listing.address])
