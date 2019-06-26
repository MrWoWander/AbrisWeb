from api.request_abris import make_request


def get_menu_request(entity_name='menu', schema_name='meta'):
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
        'params': '[{'
                  '"entityName":"'+entity_name+'",'
                  '"schemaName":"'+schema_name+'",'
                  '"predicate":null,'
                  '"limit":null,'
                  '"offset":0,'
                  '"order":[{"field":"path","desc":false}],'
                  '"where":""'
                  '}]'
    }
    return make_request(data=data)
