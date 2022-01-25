import os

with open('active_probe.txt', 'r') as file:
    g = file.readlines()
    for x in g:
        k = x.rstrip()
        if k.startswith("http://"):
            kk = k.replace("http://", "")
            print(kk)
            files = open('http.txt', 'a')
            files.write(kk+"\n")
            files.close()

        elif k.startswith("https://"):
            jj = k.replace("https://", "")
            print(jj)
            files2 = open('https.txt', 'a')
            files2.write(jj+"\n")
            files2.close()

def mege1():
	with open(f'http.txt','r') as file1:
		with open('merge.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close() 

def mege2():
	with open(f'https.txt','r') as file1:
		with open('merge.txt', 'a') as file2:
			l = file1.readlines()
			for x in l:
				v = file2.write(x)
		file2.close()

# os.system("rm -rf http.txt") 
# os.system("rm -rf https.txt") 

if __name__ == "__main__":
    mege1()
    mege2()
