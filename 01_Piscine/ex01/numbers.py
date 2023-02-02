# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/31 15:32:15 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/01 15:29:17 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	numbers():
	file = open("numbers.txt", "r")
	txt = file.read()
	splitted_text = txt.split(",")
	for eachnumber in splitted_text:
		print(eachnumber.strip())
	file.close()

if __name__ == '__main__':
	numbers()
