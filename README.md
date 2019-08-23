# 快递100 Selenium抓取工具
## 前置要求
- Firefox浏览器
- `geckodrive`
- Python `selenium` lib (`python3` suggested)


## 使用方法
1. 实例化TrackInfo()
2. 使用`query_package`或`query_packages`方法查询
3. 启用后自行销毁

## 接口格式
### query_package
- Param

    package_num, 快递单号，字符串形式　

    sf_phone，顺丰手机号后四位，字符串形式，可选，为`None`或`""`时不进入顺丰逻辑
- Return

    pacakge_num, 快递单号，字符串形式　

    [[date, time, detail],]，快递详情，日期时间过程三个信息为一组，均为字符串格式

### query_packages
- Param

    [[package_num, sf_phone], ]　多组query_package参数
- Return

    [(pacakge_num,[[date, time, detail],]) ,]　多组query_package的回复tuple list

## 其他
- 建议进行仅一次查询时持久化，不会产生内存泄露，但全天轮询时因缓存原因不建议
- 初始化打开浏览器非常耗时
- Windows请自行修改log目录

## 前置安装
### Firefox
`sudo apt install firefox`
### selenium
`pip3 install selenium`
### geckodrive
已经自带`linux_amd_64`于仓库中，请置于与`track_info.py`同一目录下
如遇到版本不兼容问题，请于官方[Github](https://github.com/mozilla/geckodriver/releases)下载
    
    