# scratch work for crawler
import requests
from bs4 import BeautifulSoup

r = requests.get("https://odbrmls.rapmls.com/scripts/mgrqispi.dll?APPNAME=Nyst&PRGNAME=MLSLogin&ARGUMENT=D%2BITRXr5DvB0Ykf95z6XGo41jObIjmrKAeI04j2bqs0%3D&KeyRid=1&Include_Search_Criteria=on&CurrentSID=166525063&MLS_Origin=OTSE&Report_Code_String=&SID=&Report_Format=&Type_Of_Search=&Search_Type=AV")
doc = BeautifulSoup(r.text, 'html.parser')

title_count = 0
b_count = 0


for h in doc.find_all("h3"):
	title_count += 1

print(title_count)

for b in doc.find_all("b"):
	b_count += 1

print(b_count)

print(b_count/title_count)

class CrawledArticle():
	def __init__(self, listing_num, address, price, beds, baths):
		self.listing = listing_num
		self.address = address
		self.price = price
		self.beds = beds
		self.baths = baths
		
class ListingFetcher():
	def fetch(self):
		listing_nums =  []
		for b in doc.find_all("b"):
			if "Listing #" in b.text:
				listing_nums.append(b.text)
		return listing_nums
		
		
		
		
		
listing_nums = ListingFetcher.fetch(doc)

print(listing_nums)	
				
		
		
