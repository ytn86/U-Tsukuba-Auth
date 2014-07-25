#!python3

from urllib.request import urlopen
from urllib.parse import urlencode

def auth(id, pw):
    url = 'https://wlan-auth1.cc.tsukuba.ac.jp/login.html'
    params = urlencode({'buttonClicked' : '4' , 'err_flag' : '0' ,'username' :id , 'password' : pw , 'Submit' : 'login'})
    handler = urlopen(url, params.encode('utf-8'))
    print(handler.read())

def main():
    id = "<Your id>"
    pw = "<Your password>"
    auth(id,pw)


if __name__ == "__main__":
    main()
