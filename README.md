<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">简单漫画下载</h3>

<div align="center">
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Createitv/kanmanSpider.svg)](https://github.com//Createitv/kanmanSpider/issues)

[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com//Createitv/kanmanSpider/pulls)
![License](https://img.shields.io/badge/license-MIT-blue.svg)


## 关于本库 
![看漫画](https://www.kanman.com)漫画下载,下载暂时为图片格式

## 环境准备
`python3`+依赖库

```
pip3 install -r requirements.txt
```

## 使用
访问![看漫画](https://www.kanman.com)搜索自己想看的漫画,108647就是索引`ID`

![image-20210711164320325](https://typora-1300715298.cos.ap-shanghai.myqcloud.com/uPic/image-20210711164320325.png)


```
scrapy crawl comic -a urlId=索引`ID`
```

## 举例

```python
scrapy crawl comic -a urlId=25933
```

### 结果

