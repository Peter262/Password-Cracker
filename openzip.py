import  optparse
import zipfile
from threading import Thread

def extract_zip(zfile=, password) :
# trying to extract the password
	try:
		zfie.extractall(pwd=password)
		print('[+]' + password + '\n')
	except:
		pass
		
def main():
	parser = optparse.OptionParser('usage') + '-f <zipfile> -d <dictionary file>'
	parser.add_option()
	
