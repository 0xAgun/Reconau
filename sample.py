import sys
import os
import time

banner = '''


█████████████████████████████████████████████
█▄─▄▄▀█▄─▄▄─█─▄▄▄─█─▄▄─█▄─▀█▄─▄██▀▄─██▄─██─▄█
██─▄─▄██─▄█▀█─███▀█─██─██─█▄▀─███─▀─███─██─██
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▄▄▄▄▀▀

					by 0〤闩gㄩ𝓝

'''
for char in banner:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.01)
pass

site = sys.argv[1]

wordlist = '/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt'
resolver = '/root/resolvers.txt'

def recon(url):
	os.system('assetfinder '+url+'| tee '+url+'_assetfin.txt')
	os.system('subfinder -d '+url+'| tee '+url+'_subfin.txt')
	os.system('python3 sublist3r.py -v -d '+url+' -o '+url+'_sublister.txt')
	os.system('amass enum --passive -d '+url+' -o '+url+'_amass.txt')



def assetfinder():
	with open(site+'_assetfin.txt','r') as file1:
		with open('new.txt', 'w') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close()



def subfinder():
	with open(site+'_subfin.txt','r') as file1:
		with open('new.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close()


def sublister():
	with open(site+'_sublister.txt','r') as file1:
		with open('new.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
			file2.close()

def amass():
	with open(site+'_amass.txt','r') as file1:
		with open('new.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
			file2.close()

def sorting_urls():
	os.system('cat new.txt | sort --unique | tee final.txt')
	print("Done Sorting")

def altdns():
	os.system('shuffledns -d '+url+' -o data_output -w '+wordlist+' -r '+resolver+' -o shuffle_output.txt')

def http_live():
	os.system('cat results_output.txt | httprobe > live_url.txt')
	print('Live subdoamin saved as live_urls.txt ')

if __name__ == "__main__":
	
	recon(site)
	assetfinder()
	subfinder()
	sublister()
	amass()
	sorting_urls()
	altdns()
	http_live()

	print("Done Subdomain enumeration")
