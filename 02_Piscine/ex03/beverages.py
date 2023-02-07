# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/06 10:20:18 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/07 10:55:52 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage:
	price = 0.3
	name = 'hot beverage'

	def description(self):
		return "Just some hot water in a cup."

	def __str__(self) -> str:
		return f'name : {self.name}\nprice : {self.price:,.2f}\ndescription : {self.description()}'

class Coffee(HotBeverage):
	price = 0.4
	name = 'coffee'

	def description(self):
		return 'A coffee, to stay awake.'

class Tea(HotBeverage):
	name = 'tea'

class Chocolate(HotBeverage):
	price = 0.5
	name = 'chocolate'

	def description(self):
		return 'Chocolate, sweet chocolate...'

class Cappuccino(HotBeverage):
	price = 0.45
	name = 'cappuccino'

	def description(self):
		return 'Un po’ di Italia nella sua tazza!'



if __name__ == '__main__':
	beverage = HotBeverage()
	print(str(beverage))
	beverage = Coffee()
	print(str(beverage))
	beverage = Tea()
	print(str(beverage))
	beverage = Chocolate()
	print(str(beverage))
	beverage = Cappuccino()
	print(str(beverage))