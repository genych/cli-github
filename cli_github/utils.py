# encoding=utf8

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

import os
import urllib.request
from urllib.parse import urlparse

GITHUB_API = 'https://api.github.com/'
API_TOKEN = os.environ.get('GITHUB_TOKEN')


def url_parse(url):
    """ Extract username from link to github profile """
    return urlparse(url).path.strip('/')

def geturl_req(url):
    """ Auth and return redirected url """
    request = urllib.request.Request(url)
    request.add_header('Authorization', 'token %s' % API_TOKEN)
    return urllib.request.urlopen(request).geturl()

def get_req(url):
    """ Auth and get response body """
    return urllib.request.urlopen(geturl_req(url)).read().decode('utf-8')
