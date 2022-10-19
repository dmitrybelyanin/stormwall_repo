import json
import os
import pydig

#
def import_cached_l7_config(tmp_file='tmp.json'):
    os.system('curl -XGET -H \"Content-Type: application/json\" -H \"Accept:application/json\" '
              'http://cc-microservices.storm-pro.net:4444/api/l7ProxyManager.getProxyConfigurationsPrivate '
              '-d \'{\"version\": 1}\' > ' + tmp_file)
    return tmp_file


def l7_config_as_a_dict(list_value, input_file):
    current_file = open(input_file)
    data = json.load(current_file)
    current_file.close()
    return data[list_value]


def get_domains_in_a_service(domains_list, service_id):
    list_of_domains = []
    count = 0
    for domain in domains_list:
        if domain['service_id'] == service_id:
            list_of_domains.append(domain)
    return list_of_domains


domains_settings_list = l7_config_as_a_dict('list', import_cached_l7_config())
my_domains = get_domains_in_a_service(domains_settings_list, 24329)

print(my_domains)





print(pydig.query('d-do.ru', 'A'))
print(pydig.query('www.d-do.ru', 'CNAME'))
print(pydig.query('d-do.ru', 'NS'))
print('hello!!!!!!')









# import_cached_l7_config('1.json')
#
# f = open('1.json')
# data = json.load(f)
# #
# # for i in data['list']:
# #     # print(i)
# #     print(i['domain_id'])
#
# for i in data['list']:
#     if i['domain_id'] == 331378:
#         print(i['backend_endpoint_list'])



# f.close()