import requests
import json


def make_request(method='POST', data=None):
    url = "http://demo.abris.site/Server/request.php"
    headers = {
        'Cookie': 'PHPSESSID=9ulp9d1o754f31p804qi7shind'
    }
    try:
        response = requests.request(method, url, headers=headers, data=data).json()
        return response
    except requests.HTTPError as e:
        pass
    except ValueError as e:
        pass

