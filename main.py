import requests


def get_posts(count, url):
    token = 'c8a9a3dbc8a9a3dbc8a9a3db82c8d1ac77cc8a9c8a9a3dba81d4f21975d685893981a54'
    version = 5.131
    posts = []
    offset = 0;

    while offset < count:
        if url.startswith(('club', 'public')):
            url = url.replace('club', '-')
            url = url.replace('public', '-')
            response = requests.get('https://api.vk.com/method/wall.get',
                                params = {
                                    'access_token': token,
                                    'v': version,
                                    'owner_id': url,
                                    'count': count,
                                }
                                )
        else:
            response = requests.get('https://api.vk.com/method/wall.get',
                                params = {
                                    'access_token': token,
                                    'v': version,
                                    'domain': url,
                                    'count': count,
                                }
                                )
        data = response.json()['response']['items']
        posts.extend(data)
        offset += 100;
    return posts


def parse_to_string(posts):
    line = ''
    for i in range(len(posts)):
        try:
            line += posts[i]['text']
        except:
            pass

    return line


posts = get_posts(1000, 'bugurt_thread')
s = parse_to_string(posts)
print(s)