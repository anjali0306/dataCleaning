import nltk 
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize



def filereading(b):
	file=open(b,"r")
	f=[]
	for line in file:
		c=tolower(line)
		b=remstop(c)
		f.append(b)
	InsideFile=f
	return InsideFile

#wordInputUser=raw_input("enter any words ")
#print(word1)
stop_words = set(stopwords.words('english'))
#print(stop_words)

def tolower(a):
	for i in a :
		word1=a.lower()
	return(word1)

def remstop(p):
	word_token=word_tokenize(p)
	final_words=[]
	for i in word_token:
		if not i in stop_words:
			final_words.append(i)
			str1 = ' '.join(final_words)
	#print(str1)
	return(str1)

filewriting=filereading("/home/anjali/pythonpractice/datacleaning/text.txt")
filewritinginside=', '.join(filewriting)


file=open("/home/anjali/pythonpractice/datacleaning/InsideFile.txt","w")
file.write(filewritinginside)
file.close
