# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_program.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/08 14:40:36 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/08 16:22:00 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from local_lib import path


def hello():
    path.Path("./newfolder").mkdir()
    file = path.Path("./newfolder/newfile.txt")
    file.write_text("something")
    print(file.read_text())


if __name__ == "__main__":
    hello()
