#!/usr/bin/python3

# Written with passion by @hatedabamboo

import vk
import sys
import getid_config


session = vk.Session()
api = vk.API(session, v = 5.103)
token = getid_config.token


if len(sys.argv) == 1:
    print('Error: missing short name.')
else:
    link = sys.argv[1]
    if 'vk.com' in link:
        userid = link.split('/')[-1]
    else:
        userid = link
    r = api.users.get(access_token = token, user_ids = userid)
    id = r[0]['id']
    print(id)
