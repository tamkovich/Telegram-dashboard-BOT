import requests

url = 'http://{ip}:{port}/RCS'
ip = '136.243.15.225'
url = url.format(ip=ip, port='8888')


def test_add():
    method_name = '/addAccount/start'
    data = {
        'accountName': 'hensonblanche',
        'description': 'hensonblanche',
        'useProxy': 'true',
        'tag': '100k',
        'username': 'hensonblanche',
        'password': 'Scegbjo756'
    }
    print(url+method_name)
    res = requests.post(url+method_name, data=data)
    print(res)

# def test_verify


if __name__ == '__main__':
    test_add()
