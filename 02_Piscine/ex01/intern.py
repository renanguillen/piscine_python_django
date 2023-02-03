# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 15:52:21 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/03 17:04:13 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Intern:
	def __init__(self):
		self.name = "My name? I’m nobody, an intern, I have no name."
	def __str__(self):
		return self.name

class Coffee:
	def __str__(self):
		 return "This is the worst coffee you ever tasted."

def work():
	try:
		Coffee
		raise Exception("I’m just an intern, I can’t do that...")
