#Pig Latin Translator
vowels = ['a','e','i','o','u','y']

def vowelCheck (word):
	for k in range(len(word)):
		for vowel in vowels:
			if word[k] == vowel:
				#print('letter: ', letter, 'vowel: ', vowel)
				return k

def pigLatinTranslator(sentence):
	words  = sentence.split()
	for i in range(len(words)):
		index = vowelCheck(words[i])
		print('word: ',words[i],'index: ', index)
		if index == 0:
			words[i] = words[i] + 'yay'
		else:
			words[i] = words[i][index:] + words[i][:index] + 'ay'
	
	translated = ' '.join(words)
	
	return translated

