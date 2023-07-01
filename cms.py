import requests
from multiprocessing.dummy import Pool
import sys, os

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
print("""
 [#] Simple CMS Detector v1.0
 [#] Coded by ]mrhouse998
 [#] https://t.me/the_omerta_store
""")

def Folder(directory):
  if not os.path.exists(directory):
  	os.makedirs(directory)
Folder("CMSs")

def scan(site):
	try:
		if "http://" in site or "https://" in site:
			url = site
		else:
			url = "http://" + site
		r = requests.get(url,timeout=20)
		if "/wp-content/" in r.text:
			print("WordPress ---> " + url)
			with open("CMSs/wordpress.txt","a") as f:
				f.write(url + "\n")
		elif "Joomla!" in r.text or "index.php?option=com_" in r.text:
			print("Joomla ---> " + url)
			with open("CMSs/joomla.txt","a") as f:
				f.write(url + "\n")			
		elif "index.php?route=common/home" in r.text:
			print("OpenCart ---> " + url)
			with open("CMSs/opencart.txt","a") as f:
				f.write(url + "\n")
		elif "sites/default" in r.text:
			print("Drupal ---> " + url)
			with open("CMSs/drupal.txt","a") as f:
				f.write(url + "\n")
		elif "prestashop" in r.text or "PrestaShop" in r.text:
			print("PrestaShop ---> " + url)
			with open("CMSs/prestashop.txt","a") as f:
				f.write(url + "\n")
		elif "osCommerce" in r.text:
			print("osCommerce ---> " + url)
			with open("CMSs/oscommerce.txt","a") as f:
				f.write(url + "\n")
		elif "vBulletin" in r.text:
			print("vBulletin ---> " + url)
			with open("CMSs/vbulletin.txt","a") as f:
				f.write(url + "\n")
		elif "Mage.Cookies" in r.text:
			print("Magento ---> " + url)
			with open("CMSs/magento.txt","a") as f:
				f.write(url + "\n")
		else:
			print("Not found ---> " + url)
			with open("CMSs/othercms.txt","a") as f:
				f.write(url + "\n")
	except:
		print("Not working ---> " + site)



try:
	urls = []
	file = input("[+] Your list ? : ")
	with open(file,"r", encoding="utf8") as sites:
		f = sites.readlines()
		for site in f:
			url = site.strip()
			urls.append(url)
	pp = Pool(100)
	pr = pp.map(scan,urls)
except Exception as e:
	print("Sites not found!")
	print(e)
	sys.exit()