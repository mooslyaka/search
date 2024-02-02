import requests

def select_size(toponym_longitude, toponym_lattitude):
     delta1, delta2 = input(), input()
     map_api_server = "http://static-maps.yandex.ru/1.x/"
     org_point = ",".join([toponym_longitude, toponym_lattitude])
     map_params = {
          "ll": org_point,
          "spn": ",".join([delta1, delta2]),
          "l": "map",
          "pt": "{0},pm2dgl".format(org_point)}
     response = requests.get(map_api_server, params=map_params)
     return response