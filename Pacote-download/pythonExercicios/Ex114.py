import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://ge.globo.com/')
except urllib.error.URLError:
    print('O site não está ativo no momento.')
else:
    print('Site está ativo!')

