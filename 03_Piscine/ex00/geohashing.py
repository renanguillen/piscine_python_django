# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    geohashing.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/08 09:41:35 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/08 13:56:17 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
# coding: utf-8

import sys
import antigravity


def is_valid_lat_long(latitude, longitude):
    lat_valid = -90 <= latitude <= 90
    lng_valid = -180 <= longitude <= 180
    precision_valid = (
        int(abs(latitude) * 10**4) == abs(latitude) * 10**4
        and int(abs(longitude) * 10**4) == abs(longitude) * 10**4
    )

    return lat_valid and lng_valid and precision_valid


def is_valid_positive_float(value):
    try:
        float_value = float(value)
        if float_value >= 0 and "{:.2f}".format(float_value) == value:
            return True
        else:
            return False
    except ValueError:
        return False


def is_valid_dow(date):
    date = date.split("-")
    if not is_valid_positive_float(date[3]):
        return False
    try:
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        if 1900 <= year <= 2023 and 1 <= month <= 12 and 1 <= day <= 31:
            return True
        else:
            return False
    except ValueError:
        return False


def check_entry(latitude, longitude, dow_opening):
    if len(sys.argv) != 4:
        print("Wrong number of arguments")
        sys.exit(1)
    if not is_valid_lat_long(latitude, longitude):
        print("Wrong latitude or longitude")
        sys.exit(1)
    if not is_valid_dow(dow_opening):
        print("Invalid date-dow, try YYYY-MM-DD-DOWVALUE")
        sys.exit(1)


def geohash(latitude, longitude, dow_opening):
    check_entry(float(latitude), float(longitude), dow_opening)
    dow_opening = dow_opening.encode('UTF-8')
    antigravity.geohash(float(latitude), float(longitude), dow_opening)
    sys.exit(0)


if __name__ == "__main__":
    geohash(sys.argv[1], sys.argv[2], sys.argv[3])
