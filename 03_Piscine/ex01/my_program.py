# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_program.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/08 14:40:36 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/08 15:56:22 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from local_lib import path

def hello():
    folder = path.Path('./newfolder')
    folder.mkdir_p()
    file = path.Path('./newfolder/newfile.txt')
    file = file.touch()
    with open(file, 'w') as file:
        file.write('something')

if __name__ == "__main__":
    hello()
