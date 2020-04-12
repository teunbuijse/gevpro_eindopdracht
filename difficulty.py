with open('woordenlijst.txt', 'r') as infile:
	woorden = infile.read()

woorden =  woorden.split('\n')
uitkomsten_dict = {}
for i in woorden:
	if len(i) > 6 and len(i) < 8:
		woorden_array = []
		letters_array = []
		for j in i:
			letters_array.append(j)
			
			
		for woord in woorden:
			for n, letter in enumerate(woord):
				if letter not in letters_array:
					break
				if n + 1 == len(woord):
					woorden_array.append(woord)
		uitkomsten_dict[i] = woorden_array

				
sorted_uitkomsten_dict = {}
for uitkomst in sorted(uitkomsten_dict, key = uitkomsten_dict.get, reverse = True):
	sorted_uitkomsten_dict[uitkomst] = uitkomsten_dict[uitkomst]
for word in sorted_uitkomsten_dict:
	print(word, sorted_uitkomsten_dict[word])
