import requests
import json
import time
import sys
import os


def show_progress_bar():
    for i in range(1, 51):
        sys.stdout.write(f'\r{i * 2}% |{"■" * i}')
        sys.stdout.flush()
        time.sleep(0.125)
    sys.stdout.write('\n')


def kugou_music_download():
    while True:
        keyword = input('请输入歌曲名或歌手名（输入"exit"退出程序）：')
        keyword = keyword.strip()

        if keyword.lower() == 'exit':
            print('谢谢使用吴同学的音乐盒，程序已退出！')
            sys.exit()

        # 获取搜索结果gequxinxi
        url = f'https://songsearch.kugou.com/song_search_v2?keyword={keyword}&page=1&pagesize=10&userid=0&clientver=&platform=WebFilter&filter=2&iscorrection=1&privilege_filter=0'
        response = requests.get(url)
        search_json_data = json.loads(response.text)
        music_hash = {}
        music_id = {}
        for search_data in search_json_data['data']['lists']:
            music_hash[search_data['FileName']] = search_data['FileHash']
            music_id[search_data['FileName']] = search_data['AlbumID']

        # 歌曲列表
        music_list = list(music_hash.keys())

        # 打印搜索结果
        for i in range(len(music_list)):
            print("{}-:{}".format(i + 1, music_list[i]))

        # 用户选择下载歌曲序号
        music_serial_number = int(input('请输入你想下载的歌曲序号:'))

        # 获取歌曲下载链接
        url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={music_hash[music_list[music_serial_number - 1]]}&album_id={music_id[music_list[music_serial_number - 1]]}&mid=1'
        response = requests.get(url)
        music_json_data = json.loads(response.text)

        try:
            # 获取歌曲备用下载链接
            music_href = music_json_data['data']['play_backup_url']
            music_response = requests.get(music_href)
            music_content = music_response.content

            try:
                # 创建保存文件夹
                os.makedirs('D:/吴同学的音乐盒', exist_ok=True)
            except Exception as e:
                print(e)
            finally:
                # 下载歌曲并保存
                music_path = f'D:/吴同学的音乐盒/{music_list[music_serial_number - 1]}.mp3'
                with open(music_path, 'wb') as f:
                    print('正在下载中...')
                    f.write(music_content)
                    show_progress_bar()
                    print(f'{music_list[music_serial_number - 1]}.mp3 下载成功！')

                # 输出下载路径给用户
                print(f'歌曲下载路径：{music_path}')

        except:
            print('对不起，没有该歌曲的版权！')


if __name__ == '__main__':
    print('欢迎使用吴同学的音乐盒！')
    print('GitHub: https://github.com/cnwutianhao')
    kugou_music_download()
    input()
