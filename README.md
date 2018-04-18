# GUIPA-PSHWReminder

web部分

## TODO

* [ ] [web](https://github.com/forewing/GUIPA-PSHWReminder/tree/web)
  * [x] 数据库
  * [x] 与爬虫通信
  * [x] API
  * [ ] 与客户端通信
    * [ ] 和GUIPA商讨
	* [ ] 写

## API

| path | args | func |
| :- | :- | :- |
| ```startparse/``` | ```name``` | 开始爬取名为```name```的作业 |
| ```getall/``` | ```name``` | 获取名为```name```的作业的全部次作业 |
| ```getlast/``` | ```name``` | 获取名为```name```的作业的最新一次作业 |