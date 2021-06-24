import requests
import re
requests.packages.urllib3.disable_warnings()




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
		try:
			r = requests.get(ga, verify=False)
			sat = re.findall('<title>(.*?)</title>', r.text)
			if '<title>' in r.text:
				for z in sat:
					print(ga, ' -> ' + z)
				open('livetitle.txt', 'a').write(ga+' -> '+z+'\n')
			else:
				print(ga, ' -> DEAD')
		except requests.exceptions.ConnectionError:
			pass
		except Exception:
			pass

if __name__ == "__main__":
	sat()
	
