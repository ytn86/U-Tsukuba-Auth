#!python3

from urllib.request import urlopen
from urllib.parse import urlencode

def auth(id, pw):
    url = "https://webauth03.cc.tsukuba.ac.jp:8443/cgi-bin/adeflogin.cgi"
    params = urlencode({"name" : id , "pass" : pw})
    handler = urlopen(url, params.encode("utf-8"))
    print(handler.read())

def main():
    id = "<Your id>"
    pw = "<Your password>"
    auth(id,pw)


if __name__ == "__main__":
    main()
