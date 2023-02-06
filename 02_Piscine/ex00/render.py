# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    render.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 15:16:27 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/03 17:18:37 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from settings import *

def argv_check():

	if len(sys.argv) != 2:
		print('Wrong number of arguments')
		sys.exit(1)

	if not sys.argv[1].endswith('.template'):
		print('Wrong file extension')
		sys.exit(1)

	try:
		template = open(sys.argv[1], "r")
		return template

	except:
		print('Non-existing file')
		sys.exit(1)


def	render():

	template = argv_check()
	htmlname = sys.argv[1].split('.')[0] + '.html'
	newhtml = open(htmlname, "w")
	settings = open("settings.py", "r")
	insert = template.read()

	for line in settings:
		if line.strip():
			var = (line.split('=')[0]).strip()
			new = str(globals()[var])
			var = '{'+ var + '}'
			insert = insert.replace(var, f'''{new}''')

	newhtml.write(f'''{insert}''')
	newhtml.close()
	settings.close()
	template.close()
	sys.exit(0)


if __name__ == '__main__':
	render()
