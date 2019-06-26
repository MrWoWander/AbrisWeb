import re

from api.login import Abris
import requests


def main():
    abris = Abris()
    print(abris.login('maksim13mezin@yandex.ru', '1234Abcd'))
    a = abris.get_menu_request()
    print("{:<8} {:<15} {:<10}".format('Название', 'Описание', 'Цена'))
    # 'Картинка', 'Категоря', 'Класс', 'Привод','Тип двигателя'
    for b in a.get('result').get('data'):
        print("{:<8} {:<15} {:<10}".format(b.get('name'), b.get('description'), b.get('price')))
    # session = requests.Session()
    # data = {
    #     'method': 'authenticate',
    #     'params': '[{"usename":"vart24@gmail.com","passwd":"1234567892q"}]'
    # }
    # session.request('POST', data=data, url='http://abris.site/Server/request.php').json()
    # data = {
    #     'method': 'getTableDataPredicate',
    #     'params': '[{"entityName":"my_db","schemaName":"public","predicate":{"strict":true,"operands":[{"levelup":false,"operand":{"field":"key","op":"EQ","value":"my"}}]},"limit":1,"offset":0,"fields":{"key":{"table_alias":"t","subfields":null,"hidden":true},"info":{"table_alias":"t"},"usename":{"table_alias":"t"}},"join":[],"order":[],"functions":[]}]'
    # }
    # response = session.request('POST', data=data, url='http://abris.site/Server/request.php').json()
    # href = response.get('result').get('data')[0].get('info')
    # referer = re.search('(\?.*\d)', href)
    # session.request('GET', url='http://demo.abris.site/' + referer.group(0))
    # data = {
    #     'jsonrpc': '2.0',
    #     'method': 'authenticate',
    #     'client_version': 'Dev',
    #     'params': '[{"usename":"admin","passwd":"1234567892q"}]'
    # }
    # headers = {
    #     'Cookie': 'PHPSESSID=' + str(dict(session.cookies)["PHPSESSID"]),
    #     'Host': 'demo.abris.site',
    #     'Origin': 'http://demo.abris.site',
    #     'Referer': 'http://demo.abris.site/' + referer.group(0)
    # }
    # response = session.request('POST', data=data, url='http://demo.abris.site/Server/request.php',
    #                            headers=headers).json()
    # print(response)


if __name__ == "__main__":
    main()
