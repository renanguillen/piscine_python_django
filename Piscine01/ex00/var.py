# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/31 10:54:17 by ridalgo-          #+#    #+#              #
#    Updated: 2023/01/31 16:02:38 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	my_var():
	a = 42
	print(a,'has a type',type(a))
	a = '42'
	print(a,'has a type',type(a))
	a = 'quarante-deux'
	print(a,'has a type',type(a))
	a = 42.0
	print(a,'has a type',type(a))
	a = True
	print(a,'has a type',type(a))
	a = [42]
	print(a,'has a type',type(a))
	a = {42: 42}
	print(a,'has a type',type(a))
	a = (42,)
	print(a,'has a type',type(a))
	a = set()
	print(a,'has a type',type(a))

if __name__ == '__main__':
	my_var()
