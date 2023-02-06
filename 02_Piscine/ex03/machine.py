# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/06 15:31:49 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/06 15:57:22 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from beverages import *

class CoffeeMachine:

	def __init__(self) -> None:
		pass

	class EmptyCup(HotBeverage):
		name = 'empty cup'
		price = 0.9

		def description(self):
			return 'An empty cup?! Gimme my money back!"'

	class BrokenMachineException(Exception):
		

if __name__ == '__main__':
	a = 0