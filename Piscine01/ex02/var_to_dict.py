# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var_to_dict.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/31 16:03:01 by ridalgo-          #+#    #+#              #
#    Updated: 2023/01/31 16:38:43 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')
]

def var_to_dict():
	dictionary = {}
	for couple in d:
		if couple[1] in dictionary:
			dictionary[couple[1]] += ' ' + couple[0]
		else:
			dictionary[couple[1]] = couple[0]
	allKeys = dictionary.keys()
	for key in allKeys:
		print(key, ':', dictionary[key])
	
if __name__ == '__main__':
	var_to_dict()