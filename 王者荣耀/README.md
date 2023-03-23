# 爬取王者荣耀数据

+ hok_skin.py
  > 批量下载王者荣耀英雄皮肤图片（手机+电脑）
  + 接口
    ```
    英雄列表：https://pvp.qq.com/web201605/js/herolist.json
    英雄主页：https://pvp.qq.com/web201605/herodetail/英雄id.shtml
    手机图片：https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/英雄id/英雄id-mobileskin-编号.jpg
    电脑图片：https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/英雄id/英雄id-bigskin-编号.jpg
    ```
  
  + 演示
    ``` 
    注意：本程序仅用于学习交流，禁止一切商业行为！！！(yes/no): yes

    数据获取成功
    请输入你要下载皮肤的英雄名：赵云
    输入的英雄名： 赵云
    英雄id： 107

    要下载手机皮肤壁纸还是电脑皮肤壁纸（手机/电脑）：电脑
    开始下载该英雄的所有皮肤
    数据获取成功
    赵云 皮肤列表 ['苍天翔龙', '忍●炎影', '未来纪元', '皇家上将', '嘻哈天王', '白执事', '引擎之心', '龙胆', '淬星耀世', '百木心枪']
    皮肤名： 苍天翔龙 皮肤url： https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/107/107-bigskin-1.jpg
    苍天翔龙 已下载到本地
    皮肤名： 忍●炎影 皮肤url： https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/107/107-bigskin-2.jpg
    忍●炎影 已下载到本地
    ...
    ```