# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/01 09:32:29 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/02 13:28:53 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def capital_city(str, states, capital_cities):
	if str in states:
		print(capital_cities[states[str]],'is the capital of', str)
		return True
	return False

def state(str, states, capital_cities):
	capitalKeys = capital_cities.keys()
	stateKeys = states.keys()
	for key1 in capitalKeys:
		if str == capital_cities[key1]:
			for key2 in stateKeys:
				if key1 == states[key2]:
					print(str,'is the capital of', key2)
					return True
	return False

def	all_in():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if len(sys.argv) != 2:
		return
	splitted = sys.argv[1].split(',')
	for each in splitted:
		if each.strip():
			each = " ".join(each.split())
			found = capital_city(each.strip().title(), states, capital_cities)
			if not found:
				found = state(each.strip().title(), states, capital_cities)
				if not found:
					print(each.strip(),'is neither a capital city nor a state')

if __name__ == '__main__':
	all_in()
