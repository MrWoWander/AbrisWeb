from django.http import HttpResponse
from django.views.generic import TemplateView

from api.login import Abris


class ProductsView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        abris = Abris()
        print(abris.login('maksim13mezin@yandex.ru', '1234Abcd'))
        abris_req = abris.get_menu_request(
            params='[{"entityName":"product","schemaName":"public","predicate":{"strict":true,"operands":[]},"aggregate":[],"limit":10,"offset":0,"primaryKey":"product_key","currentKey":"","fields":{"product_key":{"table_alias":"t","subfields":null,"hidden":false},"name":{"table_alias":"t"},"description":{"table_alias":"t"},"price":{"table_alias":"t"},"image_key":{"table_alias":"t","subfields":["name"],"subfields_table_alias":"t0","subfields_key":"image_key"},"category":{"table_alias":"t","subfields":["name"],"subfields_table_alias":"t1","subfields_key":"category_key"},"class":{"table_alias":"t","subfields":["name"],"subfields_table_alias":"t2","subfields_key":"class_key"},"drive":{"table_alias":"t","subfields":["name"],"subfields_table_alias":"t3","subfields_key":"drive_key"},"engine_type":{"table_alias":"t","subfields":["name"],"subfields_table_alias":"t4","subfields_key":"engine_type_key"},"image_url":{"table_alias":"t"}},"join":[{"key":"image_key","virtual":false,"schema":"public","entity":"image","table_alias":"t0","parent_table_alias":"t","entityKey":"image_key"},{"key":"category","virtual":false,"schema":"public","entity":"category","table_alias":"t1","parent_table_alias":"t","entityKey":"category_key"},{"key":"class","virtual":false,"schema":"public","entity":"class","table_alias":"t2","parent_table_alias":"t","entityKey":"class_key"},{"key":"drive","virtual":false,"schema":"public","entity":"drive","table_alias":"t3","parent_table_alias":"t","entityKey":"drive_key"},{"key":"engine_type","virtual":false,"schema":"public","entity":"engine_type","table_alias":"t4","parent_table_alias":"t","entityKey":"engine_type_key"}],"order":[],"process":null,"functions":[]}]')
        data = abris_req['result'].get('data')
        context['data'] = data
        return context
