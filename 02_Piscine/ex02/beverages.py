# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/06 10:20:18 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/06 11:52:41 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class HotBeverage:
	def __init__(self, price=0.30, name="hot beverage") -> None:
		self.price = price
		self.name = name

	def description(self, desc="Just some hot water in a cup."):
		return desc

	def __str__(self) -> str:
		return f'{self.price}\n{self.name}\n{self.description()}'

if __name__ == '__main__':
	bev1 = HotBeverage(0.40, 'Coffee')
	bev1.description('oie')
	print(str(bev1))