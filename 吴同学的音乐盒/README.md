# 吴同学的音乐盒

1. 模糊查询
   
   ```
   API:
   
   https://songsearch.kugou.com/song_search_v2?keyword=歌曲名或歌手名&page=1&pagesize=10&userid=0&clientver=&platform=WebFilter&filter=2&iscorrection=1&privilege_filter=0
   ```

   > 注：keyword 传入的是你要搜索的歌曲名或者歌手名

   解析 json，拿到 `FileName`、`FileHash`、`AlbumID`

---

2. 歌曲信息
   
   ```
   API:

   https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=上一个json的FileHash&album_id=上一个json的AlbumID&mid=1
   ```

   > 注：hash 的 value 是 FileHash，album_id 的 value 是 AlbumID

   解析 json，拿到 `play_backup_url`，这个 `play_backup_url` 就是歌曲的下载地址。

---

3. 打包成 .exe
   ```
   pyinstaller --onefile music.py
   ```

4. 效果图
   ![吴同学的音乐盒](https://github.com/cnwutianhao/python/assets/13990136/14ce4356-9c6a-4cdf-9bdd-e5a335119bea)
