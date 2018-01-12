import json
import requests


def isSet(next_url):
    if next_url == '':
        return False
    else:
        return True


def setAccessToken():
    global access_token
    access_token = input("Enter your Instagram access token: ")


def core():
    '''
    Setting up data
    '''
    global unfollow_count
    unfollow_count = 0
    url = 'https://api.instagram.com/v1/users/self/follows?access_token=' + str(access_token) + '&count=20'
    response = requests.get(url)
    json_data = json.loads(response.text)
    json_length = len(json_data['data'])
    '''
    Looping through the fetched users to unfollow
    '''
    for itr in range(0, json_length, 1):
            user_id = (json_data['data'][itr]['id'])
            # print user_id
            user_name = (json_data['data'][itr]['username'])
            print(user_name)
            unfollow_url = 'https://api.instagram.com/v1/users/%s/relationship?access_token=%s' % (user_id, access_token)
            r = requests.post(unfollow_url, data={"action": "unfollow"})
            if r.status_code == 200:
                print('Unfollowed %s' % user_name)
                unfollow_count += 1



setAccessToken()
core()
