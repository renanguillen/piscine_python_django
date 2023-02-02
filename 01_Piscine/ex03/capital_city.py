# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/31 17:15:55 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/01 13:52:37 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def capital_city():
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
	if sys.argv[1] in states:
		print(capital_cities[states[sys.argv[1]]])
	else:
		print('Unknown state')

if __name__ == '__main__':
	capital_city()
