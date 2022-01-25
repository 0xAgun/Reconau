#!/usr/bin/env python3
import os
import sys


banner = '''

█▀▀█ █░█ ░█▀▀█ █▀▀▀ █░░█ █▀▀▄ 
█▄▀█ ▄▀▄ ▒█▄▄█ █░▀█ █░░█ █░░█ 
█▄▄█ ▀░▀ ▒█░▒█ ▀▀▀▀ ░▀▀▀ ▀░░▀

		Autorecon
'''

print(banner)

resolvers = '/home/agun/resolvers.txt'
subdomain_wordlist = '/home/agun/subli.txt'
root_domain = sys.argv[1]
making_dir = os.system(f'mkdir {root_domain}')

def passive_tools(url):
	os.system(f'python3 sublist3r.py -d {url} -o {url}/sublister{url}.txt')
	os.system(f'subfinder -d {url} | tee {url}/subfinder{url}.txt')
	os.system(f'assetfinder -subs-only {url} | tee {url}/asset_{url}.txt')
	os.system(f'findomain -t {url} -o')

def active_url():
	os.system(f'cat final.txt | httprobe | tee active_probe.txt')
    
def subtake():
	os.system("python3 sub404.py -f active_probe.txt | tee sub404_result.txt")


def live_check(url):
	os.system("python3 test.py")
	os.system(f'massdns -r {resolvers} -t A -o S -w {url}_massdns_results.txt merge.txt')
	os.system(f"cat {url}_massdns_results.txt | sed 's/A.*// ; s/CN.*// ; s/\..$//' | tee sortedmass.txt")


def aditional():
	os.system("naabu -list sortedmass.txt | tee open_port.txt")
	os.system("cf-check -d sortedmass.txt | tee cloudflare.txt")

def assetfinder(url):
	with open(f'{url}/asset_{url}.txt','r') as file1:
		with open('all.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close() 

def subl(url):
	with open(f'{url}/sublister{url}.txt','r') as file1:
		with open('all.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close()      

def subfinder(url):
	with open(f'{url}/subfinder{url}.txt','r') as file1:
		with open('all.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close() 

def findomain(url):
	with open(f'{url}.txt','r') as file1:
		with open('all.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close() 

def sorting_urls():
	os.system('cat all.txt | sort --unique | tee final.txt')
	print("Done Sorting")


if __name__ == "__main__":
	passive_tools(root_domain)
	findomain(root_domain)
	subfinder(root_domain)
	subl(root_domain)
	assetfinder(root_domain)
	sorting_urls()
	active_url()
	subtake()
	live_check(root_domain)
	aditional()

