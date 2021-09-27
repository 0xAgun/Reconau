import os
import sys


resolvers = 'here the path of resolvers'
subdomain_wordlist = 'subdomain brute wordlist'
root_domain = sys.argv[1]
making_dir = os.system(f'mkdir {root_domain}')

def passive_tools(url):
    os.system(f'subfinder -d {url} | tee {url}/subfinder{url}.txt')
    os.system(f'amass enum -d {url} -o {url}/amass_{url}.txt')
    os.system(f'assetfinder -subs-only {url} | tee {url}/asset_{url}.txt')
    os.system(f'findomain -t {url} -o')

def active_tools(url):
    os.system(f'shuffledns -d {url} -w {subdomain_wordlist} -r {resolvers} | tee {url}/shuffle_{url}.txt')
    os.system(f'$ aiodnsbrute -w {subdomain_wordlist} -vv -t 1024 {url} | tee {url}/aiodns_{url}.txt')
    

def assetfinder(url):
	with open(f'{url}/asset_{url}.txt','r') as file1:
		with open('all.txt', 'w') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close()    

def amass(url):
	with open(f'{url}/amass_{url}.txt','r') as file1:
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

def shuffledns(url):
	with open(f'{url}/shuffle_{url}.txt','r') as file1:
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
    active_tools(root_domain)
    findomain(root_domain)
    subfinder(root_domain)
    amass(root_domain)
    assetfinder(root_domain)
    shuffledns(root_domain)
    sorting_urls()

