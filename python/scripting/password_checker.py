import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check'
                           'the api and try again!')
    return res


def pwned_api_check(password):
    sha1_pwd = hashlib.sha1(password.encode('utf-8'))
    sha1_pwd = sha1_pwd.hexdigest().upper()
    pwd_first, pwd_tail = sha1_pwd[0:5], sha1_pwd[5:]
    return pwd_first, pwd_tail


def get_pwd_leaks_count(response, hash_to_check):
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    else:
        return 0


def main(args):
    for arg in args:
        pwd = pwned_api_check(arg)
        res = request_api_data(pwd[0])
        count = get_pwd_leaks_count(res, pwd[1])
        if count != 0:
            print(f'{arg} is hacked:\t {count} times!')
        else:
            print(f'{arg} is still save ... carry on!')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
