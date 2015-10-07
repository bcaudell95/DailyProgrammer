import string

def buildDictionary(strings):
	if len(strings)>0:
		dict = {}
		for c in string.ascii_lowercase:
			startsWithChar = [w for w in strings if w[0]==c]
			if len(startsWithChar)>0:
				suffixes = [tail(w) for w in startsWithChar if len(w)>1]
				dict[c] = buildDictionary(suffixes)
		return dict
	else:
		return []
	
def tail(list):
	return list[1:] if len(list)>1 else []
	
def isValidString(dict, string):
	if len(string)==0:
		return True
	elif not string[0] in dict:
		return False
	else:
		return isValidString(dict[string[0]], string[1:])
		
def insertBreakWhereInvalid(dict, string):
	for i in range(len(string)):
		if not isValidString(dict, string[:i]):
			return string[:i-1] + '>' + string[i-1:]
	return string

f = open('dictionary.txt', 'r')
words = f.read().split('\n')
dict = buildDictionary(words)
print("apple: %s" % insertBreakWhereInvalid(dict, "apple"))
print("applesss: %s" % insertBreakWhereInvalid(dict, "applesss"))
print("zzzzz: %s" % insertBreakWhereInvalid(dict, "zzzzz"))
print("abcdefghijklmnopqrstuvwxyz: %s" % insertBreakWhereInvalid(dict, "abcdefghijklmnopqrstuvwxyz"))