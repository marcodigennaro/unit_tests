import requests

URL = "https://www.mockaroo.com/"


def fetch_net():
    response = requests.get(URL)
    if response.status_code == 200:
        return 'succeeded'
    else:
        return 'failed'


def parse():
    return 'status = ' + fetch_net()


def main():

    result = parse()
    print(result)


if __name__ == "__main__":
    main()
