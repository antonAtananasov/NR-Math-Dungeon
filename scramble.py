from pprint import pprint as print
from random import sample
import re

def scramble(text):
	words = re.split('[\s,\.\/<>?;\'\\:"\|\[\]\{\}~\`!@#\$%\^&*\(\)-=_+]|[0-9]', text)
	for word in words:
		if len(word) <= 2:
			continue
		shuffledword = word		
		i=0
		while shuffledword == word and i < 25:
			i+=1
			middle = word[1:-1]
			shuffledmiddle = ''.join(sample(middle, len(middle)))
			shuffledword = word[0]+shuffledmiddle+word[-1]
		text=text.replace(word, shuffledword, len(word))
	return text
