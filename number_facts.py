import requests
import random
from bs4 import BeautifulSoup as bs
import re
from pprint import pprint as print

def getFacts(number):
	url = f"https://en.wikipedia.org/wiki/{number}_(number)"#input('number: ')
	print(url)
	res = requests.get(url)
	soup = bs(res.content, 'html.parser')
	facts1=soup.select('h2:has([id*="math"]) ~ ul li, h2:has([id*="math"]) ~ p, h2:has([id^="Math"]) ~ ul li, h2:has([id^="Math"]) ~ p, h2:has([id^="Properties"]) ~ ul li')
	nonfacts=soup.select('h2:has([id*="math"]) + * ~ *:has(span[id]) ~ ul li, h2:has([id*="math"]) + * ~ *:has(span[id]) ~ p, h2:has([id^="Math"]) + * ~ *:has(span[id]) ~ ul li, h2:has([id^="Math"]) + * ~ *:has(span[id]) ~ p, h2:has([id^="Properties"]) + * ~ *:has(span[id]) ~ ul li')
	facts2=soup.select(':has([id^="Integers"]) ~ :has([id$="0s"]) ~ ul li, :has([id^="Integers"]) ~ :has([id$="0s"]) ~ p, :has([id*="in_the_range"]) ~ dl dd')

	facts=[]
	skipper=0
	for i in range(len(facts1)):
		if skipper > 0:
			skipper-=1
			continue
		# fact=fact.select('li')
		fact=facts1[i]
		if fact in nonfacts:
			break
		fact=fact.getText()
		if 'is:' in fact:
			try:
				for j in range(100):
					nextfact=facts1[i+j+1].getText()
					skipper+=1
					if 'is:' in nextfact or facts1[i+j+1] in nonfacts:
						break
					fact+= '\n    '+nextfact
			except:
				pass
		facts.append(re.sub('(<img.*>)|(\[*..\])','',fact))

	skipper=0
	for i in range(len(facts2)):
		if skipper > 0:
			skipper-=1
			continue
		fact = facts2[i].get_text()
		if 'is:' in fact:
			skipper-=1
			try:
				for j in range(100):
					nextfact=facts2[i+j+1].getText()
					skipper+=1
					if 'is:' in nextfact:
						break
					fact+= '\n    '+nextfact
			except:
				pass
		facts.append(re.sub('(<img.*>)|(\[*..\])','',fact))

	return facts


def getRandomFact():
		fact=''
		r=0
		while len(fact) <= 0:
			try:
				r=random.randint(0,2000)
				fact = random.choice(getFacts(r))
			except:
				pass
		return f'Random fact from {r}: ...{fact}'
	


print(getRandomFact())
