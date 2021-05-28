import requests
from colorama import Fore, Back, Style
import re




def sat():



	print("""

		#############################################
		#              SHELL CHECKER                #
		#                                           #
		#                                           #
		#                Thanks to :                #
		#   Family Attacy Cyber ~ Tatsumi Crew      #
		#############################################

	""") #Coded by SinonX

	print('\n')


	tol = input('Your list shell here => ')
	yee = open(tol, 'r').readlines()

	for i in yee:
		ga = i.strip()
		r = requests.get(ga, verify=False)
		sat = re.findall('<title>(.*?)</title>', r.text)
		try:
			if r.status_code == 200:
				print(f'{Fore.GREEN}[+]LIVE => ', ga)
				open('live.txt', 'a').write(ga+'\n')
				for z in sat:
					print('Title : ', z)
			elif r.status_code == 403:
				print(f'{Fore.CYAN}[-]FORBIDDEN => ', ga)
			elif r.status_code == 404:
				print(f'{Fore.RED}[-]NOT FOUND => ', ga)
			else:
				print(f'{Fore.WHITE}[?]UNKNOWN => ', ga)
		except Exception:
				print(f'{Fore.WHITE}[?]UNKNOWN => ', ga)


if __name__ == "__main__":
	sat()
	
