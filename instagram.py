from datetime import datetime
import requests
import json 
import pdb

link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

time = int(datetime.now().timestamp())
response=requests.get('https://www.instagram.com/accounts/login/')
# csrf = response.cookies['csrftoken']

payload = {
    'username': 'username',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:"password"',
    'queryParams': {},
    'optIntoOneTap': 'false'
}

login_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    # "x-csrftoken": 'BzYqTIXaeMVJSm37ytFPZc9JEMx5dOec'
}

login_response = requests.post(login_url, data=payload, headers=login_header)
pdb.set_trace()
# json_data = json.loads(login_response.text)

# if json_data["authenticated"]:

#     print("login successful")
#     cookies = login_response.cookies
#     cookie_jar = cookies.get_dict()
#     csrf_token = cookie_jar['csrftoken']
#     print("csrf_token: ", csrf_token)
#     session_id = cookie_jar['sessionid']
#     print("session_id: ", session_id)
# else:
#     print("login failed ", login_response.text)
