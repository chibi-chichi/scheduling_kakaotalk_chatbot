import requests
import sys, os

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = ''
redirect_url = 'https://example.com/oauth'
authorize_code = ''

data = {
    'grant_type':'authorize_code'
    'client_id':rest_api_key
    'redirect_url':redirect_url
    'code':authorize_code
}
