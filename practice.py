
import requests
from bs4 import BeautifulSoup
import re



def retrieve_parse_and_print_doc(docURL):
    response = requests.get(docURL)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    grouped_data = []
    for row in rows[1:]:
        parsed_row = re.match(r'(\d+)(\W)(\d+)', row.text)
        x = int(parsed_row.group(1))
        y = int(parsed_row.group(3))
        character = parsed_row.group(2)

        result = [y, x, character]
        grouped_data.append(result)
    
    max_y_coord = max(y for y, x, char in grouped_data)
    max_x_coord = max(x for y, x, char in grouped_data)
    
    grid = [[' ' for _ in range(max_x_coord + 1)] for _ in range(max_y_coord + 1)]

    for y, x, char in grouped_data:
        grid[max_y_coord - y][x] = char

    for row in grid:
        print(''.join(row))



retrieve_parse_and_print_doc("https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub")
retrieve_parse_and_print_doc("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")