# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridalgo- <ridalgo-@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/02 09:51:39 by ridalgo-          #+#    #+#              #
#    Updated: 2023/02/02 13:45:41 by ridalgo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def insert_header(htmlFile):
	htmlFile.write('''<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		th,
		td {
			border: solid;
			border-collapse: collapse;
			text-align: center;
			padding: 8px;
		}

		ul {
			list-style-type: none;
			padding: 0;
			margin:0;
		}

		td {
			width: 100px;
		}

		 h1.nice {
			text-align: center;
			font-family: Georgia, sans-serif;
			font-size: 5em;
			letter-spacing: -2px;
		}

		h4 {
			margin: 0;
		}

		.header {
			background-color: lightgray;
			font-weight: bold;
		}

		.alkali-metals {
			background-color: darksalmon;
		}

		.alkaline-earth-metals {
			background-color: lightgreen;
		}

		.transition-metals {
			background-color: mistyrose;
		}

		.halogens {
			background-color: antiquewhite;
		}

		.rare-elements {
			background-color: lightyellow;
		}

		.other-metals {
			background-color: lightblue;
		}

		.non-metals {
			background-color: pink;
		}

		.noble-gases {
			background-color: gainsboro;
		}
	</style>
	<title>Periodic Table</title>
</head>

<body>
	<h1 class="nice">Periodic Table</h1>
	<table>
		<tr>''')
	return

def insert_box(htmlFile, element_data):
    htmlFile.write(f'''
        <td class="{element_data['kind']}">
            <h4>{element_data['small']}</h4>
            <ul>
                <li>{element_data['element_name']}</li>
                <li>No {element_data['number']}</li>
                <li>{element_data['molar']}</li>
            </ul>
        </td>
    ''')

def insert_empty_box(htmlFile):
	htmlFile.write('''
			<td style="border: none;">
				<ul>
					<li></li>
					<li></li>
					<li></li>
				</ul>
			</td>''')

def new_line(htmlFile):
	htmlFile.write('''
		</tr>
		<tr>''')
			
def close_body(htmlFile):
	htmlFile.write('''
		</tr>
	</table>

</body>

</html>''')
	return

def parse_element_string(string):
	element_name, data = string.split("=")
	element_data = {}
	for part in data.strip().split(","):
		key, value = part.strip().split(":")
		if key == "number":
			element_data[key] = value
			if value in ['1','5','6','7','8','14','15','16','33','34','52']:
				element_data['kind'] = 'non-metals'
			elif value in ['3','11','19','37','55','87']:
				element_data['kind'] = 'alkali-metals'
			elif value in ['4','12','20','38','56','88']:
				element_data['kind'] = 'alkaline-earth-metals'
			elif value in ['22','23','24','25','26','27','28','29','30','40','41','42','43','44','45','46','47','48','72','73','74','75','76','77','78','79','80','104','105','106','107','108','109','110','111','112']:
				element_data['kind'] = 'transition-metals'
			elif value in ['13','31','32','49','50','51','81','82','83','84','113','114','115','116']:
				element_data['kind'] = 'other-metals'
			elif value in ['9','17','35','53','85','117']:
				element_data['kind'] = 'halogens'
			elif value in ['2','10','18','36','54','86','118']:
				element_data['kind'] = 'noble-gases'
			else:
				element_data['kind'] = 'rare-elements'
		elif key == "molar":
			element_data[key] = value
		else:
			element_data[key] = value.strip()
	#print(element_data['kind'])
	element_data["element_name"] = element_name.strip()
	return element_data

def periodic_table():
	positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,21,22,23,24,25,26,27,28,29,38,39,40,41,42,43,44,45,46,47,92,110]
	# open file to write in
	htmlFile = open("periodic_table.html", "w")
	# getting info from file
	periodicFile = open("periodic_table.txt", "r")
	data = []
	i = 0
	for line in periodicFile:
		data.append(parse_element_string(line))
	insert_header(htmlFile)
	for iterator in range(126):
		if iterator % 18 == 0 and iterator != 0:
			new_line(htmlFile)
		if iterator not in positions:
			insert_box(htmlFile, data[i])
			i += 1
		else:
			insert_empty_box(htmlFile)
	close_body(htmlFile)
	htmlFile.close()

if __name__ == '__main__':
	periodic_table()
