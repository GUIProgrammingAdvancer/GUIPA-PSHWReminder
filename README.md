# GUIPA-PSHWReminder

## 1.web部分

### TODO

* [ ] [web](https://github.com/forewing/GUIPA-PSHWReminder/tree/web)
  * [x] 数据库
  * [x] 与爬虫通信
  * [x] API
  * [ ] 与客户端通信
    * [ ] 和GUIPA商讨
    * [x] 写
    * [ ] 改

### API

| path | args | func |
| :- | :- | :- |
| ```startparse/``` | ```name``` | 开始爬取名为```name```的作业 |
| ```getall/``` | ```name``` | 获取名为```name```的作业的全部次作业 |
| ```getlast/``` | ```name``` | 获取名为```name```的作业的最新一次作业 |



## 2.爬虫部分

For standalone version, goto [crawl branch](https://github.com/forewing/GUIPA-PSHWReminder/tree/crawl).

### TODO

* [x] 问求作业解析
  * [x] 网页爬取
  * [x] wiki源码识别
  * [x] 区分出每次作业
  * [x] 对每次作业进行解析
  * [x] 整理数据格式

* [ ] OJ解析
  * [ ] 读取比赛
  * [ ] 识别题目来源
  * [ ] 从搜索引擎爬取博客题解 ~~、源码~~
  * [ ] ~~自动提交~~

