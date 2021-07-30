import sys
import os
import time

banner = '''


█████████████████████████████████████████████
█▄─▄▄▀█▄─▄▄─█─▄▄▄─█─▄▄─█▄─▀█▄─▄██▀▄─██▄─██─▄█
██─▄─▄██─▄█▀█─███▀█─██─██─█▄▀─███─▀─███─██─██
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▄▄▄▄▀▀

					by 0〤闩ㄩ𝓝

'''
for char in banner:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.01)
pass

site = input("Enter your site: ")

def recon(url):
	os.system('assetfinder '+url+'| tee '+url+'_assetfin.txt')
	os.system('subfinder -d '+url+'| tee '+url+'_subfin.txt')
	os.system('python3 sublist3r.py -v -d '+url+' -o '+url+'_sublister.txt')



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
	with open(site+'_subfin.txt','r') as file1:
		with open('new.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
			file2.close()

if __name__ == "__main__":
	
	recon(site)
	assetfinder()
	subfinder()
	sublister()

	print("Done Subdomain enumeration")
