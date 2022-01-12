import requests
import json
import prettytable as pt
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "cookie": "tvfe_boss_uuid=9838a0d13dd1f67c; pgv_pvid=2417828128; pgv_pvi=2376585216; RK=t4CcTBkWYK; ptcz=c8384fabf9c0f52d4c2e4130d146752460a4541eeb7692fc590c618f93408f4f; o_cookie=1253142184; pac_uid=1_1253142184; fqm_pvqid=52e46afc-7b89-4592-ab67-9fba4ee14d82; fqm_sessionid=fe9e4cda-78fb-4e5a-896f-a06b408837ed; pgv_info=ssid=s4435464587; _qpsvr_localtk=0.25664031239318774; tmeLoginType=2; euin=oK-koi6Pow6F7n**; login_type=1; qqmusic_key=Q_H_L_28YeU760eSz0Eq54bmv6h8Q0bBmjvnlzIUBT5BflqfNdHONAQZHqz1H6zhALST3; psrf_qqrefresh_token=30FF542C7753C8EF1D4B2EFA02415540; uin=1253142184; wxopenid=; psrf_musickey_createtime=1641980450; qm_keyst=Q_H_L_28YeU760eSz0Eq54bmv6h8Q0bBmjvnlzIUBT5BflqfNdHONAQZHqz1H6zhALST3; wxrefresh_token=; psrf_qqaccess_token=330E495DFB438544538EE689B475858F; psrf_qqopenid=48B9103621A56EFD8D4578276E31E69F; psrf_qqunionid=6542C1DA4F562285721D87A58B6B004A; wxunionid=; psrf_access_token_expiresAt=1649756450"
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


