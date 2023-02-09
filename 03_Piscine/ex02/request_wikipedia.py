# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    request_wikipedia.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 09:40:27 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/09 13:50:33 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import dewiki
import sys


class ArgvException(Exception):
    def __init__(self) -> None:
        super().__init__(
            'Usage: python3 request_wikipedia.py "What you want to search"'
        )


class RequestException(Exception):
    def __init__(self) -> None:
        super().__init__("There was a problem with you request, page not found")


class ParseException(Exception):
    def __init__(self) -> None:
        super().__init__("There was a problem with you request, couldn't open page")


def check_arguments():
    try:
        if len(sys.argv) != 2:
            raise ArgvException
    except ArgvException as error:
        print(error)
        sys.exit(1)


def check_request(page_id):
    try:
        if page_id == -1:
            raise RequestException
    except RequestException as error:
        print(error)
        sys.exit(1)


def remove_between(text, start_delimiter, end_delimiter):
    while True:
        start = text.find(start_delimiter)
        end = text.find(end_delimiter, start)
        if start == -1 or end == -1:
            return text
        text = text[:start] + text[end + len(end_delimiter) :]


def wiki_request(searchterms):
    params_query = {
        "action": "query",
        "prop": "extracts",
        "redirects": True,
        "titles": searchterms,
        "format": "json",
    }
    req_query = requests.get("http://en.wikipedia.org/w/api.php", params=params_query)
    page_id = list(req_query.json()["query"]["pages"].keys())[0]
    check_request(int(page_id))
    params_parse = {
        "action": "parse",
        "prop": "wikitext",
        "pageid": page_id,
        "format": "json",
    }
    try:
        req_parse = requests.get(
            "http://en.wikipedia.org/w/api.php", params=params_parse
        )
    except ParseException as error:
        print(error)
        sys.exit(1)
    txt = dewiki.from_string((req_parse.json())["parse"]["wikitext"]["*"])
    txt = remove_between(txt, "{", "}")
    txt = remove_between(txt, "<", ">")
    return txt.strip().strip("}".strip())


def search_wikipedia():
    check_arguments()
    results = wiki_request(sys.argv[1])
    filename = sys.argv[1] + ".wiki"
    with open(filename, "w") as file:
        file.write(str(results))


if __name__ == "__main__":
    search_wikipedia()
