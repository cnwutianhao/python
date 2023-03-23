# 批量下载王者荣耀英雄皮肤图片

import requests
import sys
import json
import re
import os


class Hero:
    def __init__(self):
        self.hero_id = ""
        self.hero_name = ""


hero_data_list = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51',
}


def save_hero_skin(hero_name, skin_name, skin_url, skin_type):
    file = os.path.join('image', hero_name)
    if not os.path.exists(file):
        os.makedirs(file)

    skin_content = requests.get(url=skin_url, headers=headers).content
    file_name = f'{skin_name}({skin_type}).jpg'
    file_path = os.path.join(file, file_name)
    with open(file_path, mode='wb') as f:
        f.write(skin_content)
        print(skin_name, '已下载到本地')


def download_hero_skin(hero_id, hero_name, skin_type):
    if skin_type not in ('手机', '电脑'):
        print('输入的皮肤壁纸类型不正确')
        sys.exit()

    print('开始下载该英雄的所有皮肤')

    url = f'https://pvp.qq.com/web201605/herodetail/{hero_id}.shtml'

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        print('数据获取成功')
        response.encoding = response.apparent_encoding
        hero_skin_list = re.findall('data-imgname="(.*?)">', response.text)[0]
        hero_skin_list = re.sub('&\\d+', '', hero_skin_list).split('|')
        print(hero_name, '皮肤列表', hero_skin_list)
        for num in range(1, len(hero_skin_list) + 1):
            skin_name = hero_skin_list[num - 1]
            if skin_type == '手机':
                skin_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero_id}/{hero_id}-mobileskin-{num}.jpg'
            else:
                skin_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero_id}/{hero_id}-bigskin-{num}.jpg'
            print('皮肤名：', skin_name, '皮肤url：', skin_url)
            save_hero_skin(hero_name, skin_name, skin_url, skin_type)


def prepare_download_hero_skin(hero_name):
    print('输入的英雄名：', hero_name)

    hero = next((h for h in hero_data_list if h.hero_name == hero_name), None)

    if hero:
        print('英雄id：', hero.hero_id)
        skin_type = input("要下载手机皮肤壁纸还是电脑皮肤壁纸（手机/电脑）：")
        download_hero_skin(hero.hero_id, hero_name, skin_type)
    else:
        print('不存在这个英雄')
        sys.exit()


def hero_list():
    url = 'https://pvp.qq.com/web201605/js/herolist.json'

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        print('数据获取成功')
        result = json.loads(response.text)

        for hero in result:
            hero_id = hero['ename']
            hero_name = hero['cname']

            data = Hero()
            data.hero_id = hero_id
            data.hero_name = hero_name
            hero_data_list.append(data)

        input_hero_name = input("请输入你要下载皮肤的英雄名：")
        prepare_download_hero_skin(input_hero_name)
    else:
        print('数据获取失败，失败码: ', response.status_code)
        print('程序结束')
        sys.exit()


attention = input('注意：本程序仅用于学习交流，禁止一切商业行为！！！(yes/no): ')
if attention.lower() != 'yes':
    print('程序终止')
    sys.exit()

hero_list()
