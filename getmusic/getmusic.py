# -*- coding: utf-8 -*-
# @Time     :  10:55
# @Author   : XiaoKai
# @Email    : xk_1994@163.com
# @File     : getmusic.py
# @Software: PyCharm

import requests
import json
import os

def getRawMusic(id,folder_name,name):
    url = 'http://music.163.com/song/media/outer/url?id=%s' % id
    headers = {
                "Upgrade-Insecure-Requests" : "1",
                "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding" : "gzip, deflate",
                "Accept-Language" : "zh-CN,zh;q=0.9",
                "Cookie" : "_ntes_nuid=e3d1f97de0c39dc2a3938e1e64b47f58; vjuids=-8b29d28da.15d3fbf7c6a.0.1b9b98658770c; mail_psc_fingerprint=16caaa786ae881b593ba34316ef2e759; _ga=GA1.2.1885426920.1498817450; _iuqxldmzr_=32; _ngd_tid=iY09uV1thaxSAXpQuIdMz5rzRFbIJWwj; nts_mail_user=xk_1994@163.com:-1:1; __oc_uuid=f10023c0-3736-11e8-b83f-21cbc6608eeb; NTES_CMT_USER_INFO=98146175%7Cxk_1994%7C%7Cfalse%7CeGtfMTk5NEAxNjMuY29t; __utma=187553192.1885426920.1498817450.1523098007.1523608056.3; vjlast=1500013100.1528266374.21; _ntes_nnid=e3d1f97de0c39dc2a3938e1e64b47f58,1536312091118; __utmz=94650624.1536312092.4.3.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; WM_TID=zNqCGszUt6DgzOiYHFlDXL0A0jA4m4mo; mp_MA-9ADA-91BF1A6C9E06_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fcampus.163.com%2Fapp%2FjobDetail%2Findex%3Fid%3D126%22%2C%22updatedTime%22%3A%201537272384164%2C%22sessionStartTime%22%3A%201537271794964%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%203%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%2238a76008-4e2e-4bba-803b-929a18e9ac64%22%2C%22persistedTime%22%3A%201536219227058%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201537272384164%7D%2C%22sessionUuid%22%3A%20%22e1e9df6b-df1d-4d48-9820-529e0e958e0d%22%7D; usertrack=CrH7M1ukw6EZ/XMRAwNFAg==; vinfo_n_f_l_n3=6cc4d48a4215420c.1.7.1500013100149.1528266545382.1541944647296; __f_=1544448870046; P_INFO=xk_1994@163.com|1545814893|0|mail163|00&11|sic&1545630549&mail163#sic&510100#10#0#0|&0|kaola&mail163|xk_1994@163.com; starttime=; __utmc=94650624; WM_NI=wWEVQTjBpAftZSXgGOA3zWK7nTY1C4JdqXcuwIBV6ZMQaVNjLffMgU1WHC6JmKu7F%2BDXBT76pn6N9JxXcFEM0%2FUv%2F8B0zlrxCBdoK%2BNZeGNrl0Ivn%2BO3qrQXbijgaJB0Q04%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeace75df3b7c092ef74aceb8fb2c85b829a9faabb748894f8d5b554a99b87a3f02af0fea7c3b92ab5898bb7d460aa9ec0a2e5809a8d9888c64583edb6b8ca3dae8c97d2c2408abcbfb9e27fb5978eb7b5528f8fafb7cd6290baaaaee65ff38988a4b542af95bbd8c52188888eb5b63eb4b2faafbc42bc88ada7c847f4f19b97ae3482f0b68df174819eac90ca218e86aba8cd7ab0f08797ed218dedbf93d454a2b7a688e44282f09fd1b737e2a3; __remember_me=true; __utma=94650624.1885426920.1498817450.1547779756.1547781722.13; MUSIC_U=a32511f0c0af8d8c8177af8c53e06059ed93e616a727405545388ad753bd94ed1fa1d5cac39ae7a5edd1347294278b4931b299d667364ed3; __csrf=2930bf39618101a68b64f785bb80d201; JSESSIONID-WYYY=BVTMtDwRV1HYdyfQK%2FUoSfheSWTimEHyXC6g%2FqnnrZWYuWDO83Wf4YrTdOlb24mrgsaoSy3RxK7gTDAOUNIgx%2FA3FBWM03q3tujiYdWX8fGZq92POolEwC%2F5JcmEdk23BYc2yqRv22Znkn4Byx8P2HlPpehgFve3o4FjjvFQw2tvbIfN%3A1547790260616"
    }

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    fpath = os.path.join(folder_name, '%s.mp3' % name)
    if  os.path.exists(fpath):
        print('song exist!')
    else:
        r = requests.get(url, headers=headers).content
        f = open(fpath,'wb')
        f.write(r)
        f.close()


def getRM(id):

    url = 'http://music.163.com/api/playlist/detail?id=%s' % id
    headers = {
        "Cache-Control" : "max-age=0",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "zh-CN,zh;q=0.9",
        "Cookie" : "_ntes_nuid=e3d1f97de0c39dc2a3938e1e64b47f58; vjuids=-8b29d28da.15d3fbf7c6a.0.1b9b98658770c; mail_psc_fingerprint=16caaa786ae881b593ba34316ef2e759; _ga=GA1.2.1885426920.1498817450; _iuqxldmzr_=32; _ngd_tid=iY09uV1thaxSAXpQuIdMz5rzRFbIJWwj; nts_mail_user=xk_1994@163.com:-1:1; __oc_uuid=f10023c0-3736-11e8-b83f-21cbc6608eeb; NTES_CMT_USER_INFO=98146175%7Cxk_1994%7C%7Cfalse%7CeGtfMTk5NEAxNjMuY29t; __utma=187553192.1885426920.1498817450.1523098007.1523608056.3; vjlast=1500013100.1528266374.21; _ntes_nnid=e3d1f97de0c39dc2a3938e1e64b47f58,1536312091118; __utmz=94650624.1536312092.4.3.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; WM_TID=zNqCGszUt6DgzOiYHFlDXL0A0jA4m4mo; mp_MA-9ADA-91BF1A6C9E06_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fcampus.163.com%2Fapp%2FjobDetail%2Findex%3Fid%3D126%22%2C%22updatedTime%22%3A%201537272384164%2C%22sessionStartTime%22%3A%201537271794964%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%203%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%2238a76008-4e2e-4bba-803b-929a18e9ac64%22%2C%22persistedTime%22%3A%201536219227058%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201537272384164%7D%2C%22sessionUuid%22%3A%20%22e1e9df6b-df1d-4d48-9820-529e0e958e0d%22%7D; usertrack=CrH7M1ukw6EZ/XMRAwNFAg==; vinfo_n_f_l_n3=6cc4d48a4215420c.1.7.1500013100149.1528266545382.1541944647296; __f_=1544448870046; P_INFO=xk_1994@163.com|1545814893|0|mail163|00&11|sic&1545630549&mail163#sic&510100#10#0#0|&0|kaola&mail163|xk_1994@163.com; starttime=; __utmc=94650624; WM_NI=wWEVQTjBpAftZSXgGOA3zWK7nTY1C4JdqXcuwIBV6ZMQaVNjLffMgU1WHC6JmKu7F%2BDXBT76pn6N9JxXcFEM0%2FUv%2F8B0zlrxCBdoK%2BNZeGNrl0Ivn%2BO3qrQXbijgaJB0Q04%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeace75df3b7c092ef74aceb8fb2c85b829a9faabb748894f8d5b554a99b87a3f02af0fea7c3b92ab5898bb7d460aa9ec0a2e5809a8d9888c64583edb6b8ca3dae8c97d2c2408abcbfb9e27fb5978eb7b5528f8fafb7cd6290baaaaee65ff38988a4b542af95bbd8c52188888eb5b63eb4b2faafbc42bc88ada7c847f4f19b97ae3482f0b68df174819eac90ca218e86aba8cd7ab0f08797ed218dedbf93d454a2b7a688e44282f09fd1b737e2a3; __remember_me=true; __utma=94650624.1885426920.1498817450.1547779756.1547781722.13; MUSIC_U=a32511f0c0af8d8c8177af8c53e06059ed93e616a727405545388ad753bd94ed1fa1d5cac39ae7a5edd1347294278b4931b299d667364ed3; __csrf=2930bf39618101a68b64f785bb80d201; JSESSIONID-WYYY=Pjl5zEJbrAMell%5CY16Cascja8MmbehFqDP28TGdKRZ%5CeTsUTiam8dAjCC4gikBJmncr6pb4bHWuD%2BsT9jNcoExjqkTZaRgNeD9O32Ptm17jWFR85K9Qzdjz9huFRM%5CBrIG5UByMPMUMV%5CO1wqOQrPTU%2Fj32%2FNaoXEiSonwiqHpvUyea9%3A1547798964764"
    }

    r = requests.get(url, headers=headers).content
    try:
        data = json.loads(r)
        print(data)
        music_data = data['result']
        folder_name = music_data['name']
        music_list = music_data['tracks']
        for music in music_list:
            print(music['name'],music['id'])
            music_name = music['name']
            music_id = music['id']
            getRawMusic(music_id,folder_name,music_name)
    except RuntimeError:
        print('解析出错！')
if __name__ == '__main__':
    id = input('Please input songList id:')
    getRM(id)


