'''
Laboratorium 5 (przechwycenie danych HTTP)
Napisz program generujący zapytanie HTTP GET do dowolnego serwera i zachowujący odpowiedź w pliku.
'''

import requests
from datetime import date


def send_request_and_save_result(url):
    r = requests.get(url)
    today = date.today()

    with open("result.txt", "a") as file:
        file.write('Request sent to : ' + url + '\n \n')
        file.write('Date: ' + str(today) + '\n \n')
        file.write('Status code: ' + str(r.status_code) + '\n')
        file.write('Headers: ' + str(r.headers) + '\n')
        file.write('Content: ' + str(r.content))
        file.write('\n')
        file.write('----------------------------------\n')


send_request_and_save_result("http://swing.ict.pwr.wroc.pl/~wojtek/about.html")
