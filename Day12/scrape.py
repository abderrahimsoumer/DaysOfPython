import os
import sys
import requests
import datetime
from requests_html import HTML
import pandas as pd

BASE_DIR = os.path.dirname(__file__)

def url_to_file(url, filename='world.html', save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_txt = r.text
        if save:
            with open(filename, 'w') as f:
                f.write(html_txt)
        return html_txt
    return ""



def parse_and_extract(url, name='2020'):
    html_text = url_to_file(url)  
    if not html_text :
        return False
    r_html = HTML(html=html_text)
    table_class = '.imdb-scroll-table'
    table = r_html.find(table_class)
    table_data = []
    header_names = []

    if len(table) == 0:
        return False

    parse_table = table[0]
    rows = parse_table.find('tr')
    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [ x.text for x in header_cols]
    
    for row in rows[1:]:
        row_data = []
        cols = row.find('td')
        for i, col in enumerate(cols):
            row_data.append(col.text)
        table_data.append(row_data)
    df = pd.DataFrame(table_data, columns=header_names)
    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path,exist_ok=True)
    file_path = os.path.join('data', f'{name}.csv')
    df.to_csv(file_path, index=False)
    return True

def run(start_year=None, years_ago=1):
    if start_year is None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    for year in range(start_year - (years_ago - 1 ), start_year + 1):
        print(year)
        url = f"https://www.boxofficemojo.com/year/world/{year}/"
        finished = parse_and_extract(url, name=year)
        if finished:
            print(f"Finished {year}")
        else:
            print(f"{year} not finished")
        


if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 1
    
    run(start, count)