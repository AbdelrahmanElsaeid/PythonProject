
def freq(str):

	str_list = str.split()

	unique_words = set(str_list)
	
	for words in unique_words :
		print('Frequency of ', words , 'is :', str_list.count(words))

	
str ='ahmed abdo Ali abdo abdo abdo ahmed mido mido mido'
	

freq(str)
  
#--------------------------------------------
