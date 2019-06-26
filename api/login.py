import re

import requests


class Abris:
    URL = "http://demo.abris.site/Server/request.php"

    def __init__(self):
        self.username = None
        self.password = None
        self.session = requests.Session()

    def make_request(self, method='POST', data=None, url=URL):
        try:
            response = self.session.request(method, url, data=data).json()
            return response
        except requests.HTTPError as e:
            pass
        except ValueError as e:
            pass

    def login(self, username, password):
        self.username = username
        self.password = password
        data = {
            'method': 'authenticate',
            'params': '[{"usename":"' + self.username + '","passwd":"' + self.password + '"}]'
        }
        a = self.session.request('POST', data=data, url='http://abris.site/Server/request.php').json()
        print(a)
        data = {
            'method': 'getTableDataPredicate',
            'params': '[{"entityName":"my_db","schemaName":"public","predicate":{"strict":true,"operands":[{"levelup":false,"operand":{"field":"key","op":"EQ","value":"my"}}]},"limit":1,"offset":0,"fields":{"key":{"table_alias":"t","subfields":null,"hidden":true},"info":{"table_alias":"t"},"usename":{"table_alias":"t"}},"join":[],"order":[],"functions":[]}]'
        }
        response = self.session.request('POST', data=data, url='http://abris.site/Server/request.php').json()
        href = response.get('result').get('data')[0].get('info')
        referer = re.search('(\?.*\d)', href)
        self.session.request('GET', url='http://demo.abris.site/' + referer.group(0))
        data = {
            'jsonrpc': '2.0',
            'method': 'authenticate',
            'client_version': 'Dev',
            'params': '[{"usename":"admin","passwd":"' + self.password + '"}]'
        }
        headers = {
            'Cookie': 'PHPSESSID=' + str(dict(self.session.cookies)["PHPSESSID"]),
            'Host': 'demo.abris.site',
            'Origin': 'http://demo.abris.site',
            'Referer': 'http://demo.abris.site/' + referer.group(0)
        }
        response = self.session.request('POST', data=data, url='http://demo.abris.site/Server/request.php',
                                        headers=headers).json()
        return response

    def get_menu_request(self, params = '[{}]'):
        '''
        Запрос меню

        Вместо entityName и schemaName ввести:
        вместо "entityName" - необходимо указать наименование сущности в базе;
        вместо "schemaName" - указать наименование схемы.
        :param entity_name:
        :param schema_name:
        :return:
        '''
        data = {
            'method': 'getTableDataPredicate',
            'params': params
        }
        return self.make_request(data=data)

    def get_metadata_request(self):
        '''
        Запрос метаданных
        :return:
        '''
        data = {
            'method': 'getAllModelMetadata',
            'params': '[{}]'
        }
        return self.make_request(data=data)

    def get_table_data_request(self, entity_name='menu', schema_name='meta'):
        data = {
            'method': 'getTableDataPredicate',
            'params': '[{ "entityName":"' + entity_name + '", "schemaName":"' + schema_name + '", "predicate": {"strict":true, "operands":[]}, "aggregate":[], "limit":"10", "offset":0, "primaryKey":"aircraft_code", "fields": {"aircraft_code": {"table_alias":"t", "subfields":null, "hidden":false}, "model": {"table_alias":"t"}, "range": {"table_alias":"t"} }, "join":[], "order":[], "process":null, "functions":[] }]'
        }
        return self.make_request(data=data)
