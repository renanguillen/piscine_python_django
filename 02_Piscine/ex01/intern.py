# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 15:52:21 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/07 13:15:58 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
# coding: utf-8

class Intern:

	def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
		self.name = name

	def __str__(self):
		return self.name

	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")

	def make_coffee(self):
		return self.Coffee()

if __name__ == '__main__':
	person1 = Intern()
	person2 = Intern("Mark")
	print(str(person1))
	print(str(person2))
	print(person2.make_coffee())
	try:
		person1.work()
	except Exception as this:
		print(this)