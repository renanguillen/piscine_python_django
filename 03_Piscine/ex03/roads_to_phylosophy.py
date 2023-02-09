# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roads_to_phylosophy.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 13:43:09 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/09 17:59:48 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import requests
from bs4 import BeautifulSoup

class DeadEnd(Exception):
    def __init__(self) -> None:
        super().__init__("It leads to a dead end !")

class BadRequest(Exception):
    def __init__(self) -> None:
        super().__init__("Request failed!")

class LoopError(Exception):
    def __init__(self) -> None:
        super().__init__("It leads to an infinite loop !")

def validation():
    if len(sys.argv) != 2:
        raise Exception
    # if (sys.argv[1].tittle()) == 'Philosophy':
    #     print('Seriously?')
    #     sys.exit(0)
    if sys.argv[1]:
        entry = str(sys.argv[1]).replace(' ', '_')
    return entry

def road(entry):
    count = 1
    viewed = []
    while True:
        url = "https://en.wikipedia.org/wiki/" + entry
        response = requests.get(url)
        if response.status_code != 200:
            if response.status_code == 404:
                raise DeadEnd
            else:
                raise BadRequest
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            page = soup.find(id='mw-content-text')
            page = page.select('p > a')
            if not page:
                raise DeadEnd
            first_link = page[0]['href'].split('/')[-1]
            try:
                if soup.find(id='firstHeading').text in viewed:
                    raise LoopError
                else:
                    viewed.append(soup.find(id='firstHeading').text)
            except LoopError as error:
                print(error)
                sys.exit(1)
            if first_link == 'Philosophy':
                viewed.append(first_link)
                break
            count += 1
            entry = first_link
    for each in viewed:
        print(each)
    print(count, 'roads from', viewed[0].title(), 'to philosophy')




if __name__ == "__main__":
    try:
        entry = validation()
    except:
        sys.exit('Invalid entry')
    try:
        road(entry)
    except DeadEnd as error:
        print(error)