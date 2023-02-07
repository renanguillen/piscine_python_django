# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/06 15:31:49 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/07 13:15:23 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
# coding: utf-8

from beverages import *
import random

class CoffeeMachine:

	def __init__(self) -> None:
		self.no_of_servings = 0

	class EmptyCup(HotBeverage):
		name = 'empty cup'
		price = 0.9

		def description(self):
			return 'An empty cup?! Gimme my money back!"'

	class BrokenMachineException(Exception):
		def __init__(self) -> None:
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.no_of_servings = 0

	def serve(self, beverage):
		serving = random.choice([beverage(), self.EmptyCup()])
		if self.no_of_servings < 10:
			self.no_of_servings += 1
			return(str(serving))

		else:
			raise self.BrokenMachineException()


if __name__ == '__main__':
	machine = CoffeeMachine()
	beverage_options = [Coffee, Tea, Cappuccino, Chocolate, HotBeverage]
	machine_breaks = 2
	while machine_breaks > 0:
		drink = random.choice(beverage_options)
		try:
			print(f"{machine.serve(drink)}\n")
		except CoffeeMachine.BrokenMachineException as error:
			print(f"{error}\n")
			machine.repair()
			machine_breaks -= 1
