import requests
import json
import prettytable as pt
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
}

def search(key):
    num = 0
    song_info = []

    url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=10&w='+key
    response = requests.get(url)
    json_msg = response.text[9:-1]
    json_dict = json.loads(json_msg)
    song_list = json_dict['data']['song']['list']

    tb = pt.PrettyTable()
    tb.field_names = ['序号','歌名','专辑名','歌手']
    for i in song_list:
        num+=1
        song_info.append([num,i['songname'],i['albumname'],i['singer'][0]['name'],i['media_mid'],i['songmid']])
        tb.add_row([num,i['songname'],i['albumname'],i['singer'][0]['name']])

    print(tb)
    return song_info

def keepit(song_info,sel):
    sel_songmid = song_info[sel-1][-1]
    url1 = 'https://u.y.qq.com/cgi-bin/musicu.fcg'
    params1 = {
        '_': time.time() * 1000,
        'sign': 'zzakgej75pk8w36d82032784bdb9204d99bf6351acb7d',
        "data": '{"req":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7469768631","songmid":["' + sel_songmid + '"],"songtype":[0],"uin":"1164153961","loginflag":1,"platform":"20"}}}'
    }
    response = requests.get(url1, params=params1, headers=headers)
    json_dict = json.loads(response.text)
    purl = json_dict['req']['data']['midurlinfo'][0]['purl']
    if not purl:
        print("vip歌曲，无法下载")
    else:
        url = 'https://dl.stream.qqmusic.qq.com/'+purl
        music_data = requests.get(url).content
        with open('music/'+song_info[sel-1][1]+'.m4a','wb') as f:
            f.write(music_data)
        print("下载成功")

while True:
    name = input("请输入所需要查询的歌手名或歌曲：")
    song_info = search(name)
    select = eval(input("请你输入需下载歌曲编号:"))
    keepit(song_info,select)


