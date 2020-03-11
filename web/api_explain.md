# 农产品大数据系统API使用说明

## 系统说明
系统使用端口：8080  
系统使用开发语言：python 3.7  
系统使用数据库：MySQL 8.x  
系统使用后端web框架：Flask  

系统通用数据返回格式：  
{  
    'errcode': '0',     //返回码：0=成功，404=失败  
    'errmsg': '成功',     //返回信息，可无视  
    'data':     //返回数据包，JSON数组每个节点为MySQL查询结果的一行；格式：{字段名称:值}    
    [{'id': 1, 'products_code': 'potato', 'products_name': '马铃薯', 'products_alias': '土豆'}]  
}  



## 目录
- [产品信息](#0)
- [价格分析](#1)
- [技术文章分析](#2)
- [虫害病分析](#3)
- [种植基地分析](#4)
- [网络分析](#5)

## <h2 id="0">零、产品信息</h2>
0.1、产品列表[完成]  
接口：/prdInfo  
请求参数：无  
返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'id': 1, 'products_code': 'potato', 'products_name': '马铃薯', 'products_alias': '土豆'}]}  

返回数据解析：  
products_code：产品编码  
products_name：产品名称  
products_alias：产品别名  





## <h2 id="1">一、价格分析接口设计</h2>
价格变化分析：  
### 1.1、日均价格变化[完成]  
接口：/price/dayAvgPrice  
请求参数：  
startDate：开始日期 YYYY-MM-DD  
stopDate：结束日期 YYYY-MM-DD  

返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'avg_price': '2.50', 'date': '2019-01-01'}, {'avg_price': '2.26', 'date': '2019-01-02'}, {'avg_price': '2.27', 'date': '2019-01-03'}, {'avg_price': '2.29', 'date': '2019-01-04'},


返回数据解析：   
avg_price：全国平均报价  
date：日期  


### 1.2、月均价格变化[完成]  
接口：/price/monAvgPrice  
请求参数：  
startDate：开始日期 YYYY-MM  
stopDate：结束日期 YYYY-MM  

返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'avg_price': '2.31', 'date': '2019-01'}, {'avg_price': '2.52', 'date': '2019-02'}]}

返回数据解析： 
avg_price：全国均价  
date：月份  

### 1.3、年均价格变化[完成]  
接口：/price/yearAvgPrice  
请求参数：  
startDate：开始日期 YYYY  
stopDate：结束日期 YYYY  

返回数据样例：   
{'errcode': '0', 'errmsg': '成功', 'data': [{'avg_price': '2.41', 'date': '2019'}, {'avg_price': '2.95', 'date': '2020'}]}

返回数据解析：   
avg_price：均价  
date：年


### 对比分析：  
#### 1.4、日 `同` 比分析[完成]  
接口：  
请求参数：无    
返回数据样例：    

返回数据解析：   


#### 1.5、日 `环` 比分析[完成]  
接口：  
请求参数：无    
返回数据样例：    

返回数据解析：   


#### 1.6、月 `同` 比分析[完成]  
接口：/price/monCorrespondingPeriod  
请求参数：  
year：YYYY    

返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'m01': 13.24, 'm02': 18.31, 'm03': 18.87, 'm04': 24.88, 'm05': 21.03, 'm06': 9.05, 'm07': 5.07, 'm08': 9.72, 'm09': 1.88, 'm10': -0.47, 'm11': 0.93, 'm12': 6.31}]}

返回数据解析：   
1-12个月对应的同比增长百分比，单位%

#### 1.7、月 `环` 比分析[完成]  
接口：/price/monLinkRelative  
请求参数：  
year：YYYY   
返回数据样例：   
{'errcode': '0', 'errmsg': '成功', 'data': [{'m01': 4.05, 'm02': 9.09, 'm03': 0.0, 'm04': 5.56, 'm05': 6.02, 'm06': -10.28, 'm07': -9.88, 'm08': 3.95, 'm09': -8.44, 'm10': -2.3, 'm11': 2.83, 'm12': 8.26}]}

返回数据解析：   
1-12个月对应的环比增长百分比，单位%  


#### 1.8、年 `环` 比分析[完成]  
接口：/price/yearLinkRelative   
请求参数：无    
返回数据样例：    
{'errcode': '0', 'errmsg': '成功', 'data': [{'2020': 22.41, '2019': 12.09, '2018': 0.47}]}

返回数据解析：  
年份对应环比增长百分比，单位%  


#### 1.9、地区市场报价数量[完成]  
接口：/price/areaCounts   
请求参数：无    
返回数据样例：    
{'errcode': '0', 'errmsg': '成功', 'data': [{'bazaar': '山东', 'counts': 4467}, {'bazaar': '山西', 'counts': 4358}, 

返回数据解析：   
bazaar：地区  
counts：报价数量  



## <h2 id="2">二、技术文章分析接口设计</h2>
### 文章来源分析：  
#### 2.1、文章列表[完成]
接口：article/info  
请求参数：无    
返回数据样例：   
{'errcode': '0', 'errmsg': '成功', 'data': [{'article_title': '马铃薯甘蓝菠菜萝卜高产高效栽培技术', 'article_url': 'http://www.vegnet.com.cn/Tech/4700.html', 'article_source': '本站', 'date': '2002-12-20'}, {'article_title': '秋土豆的主要病虫防治', 'article_url': 'http://www.vegnet.com.cn/Tech/4748.html', 'article_source': '本站', 'date': '2002-12-21'}, {'article_title': '马铃薯脱毒原种栽培技术', 'article_url': 'http://www.vegnet.com.cn/Tech/24485.html', 'article_source': '农博网', 'date': '2009-04-11'}, {'article_title': '土豆做醋的技术方法\u3000', 'article_url': 'http://www.vegnet.com.cn/Tech/25018.html', 'article_source': '本站', 'date': '2009-08-26'}, {'article_title': '如何防治马铃薯青枯病', 'article_url': 'http://www.vegnet.com.cn/Tech/25278.html', 'article_source': '农博网', 'date': '2009-10-10'}, {'article_title': '马铃薯部分虫害的防治措施', 'article_url': 'http://www.vegnet.com.cn/Tech/25479.html', 

返回数据解析：    
article_title：文章标题  
article_url：文章链接  
article_source：文章来源  
date：文章发布时间  

#### 2.2、来源文章数量[完成]
接口：/article/source  
请求参数：无   
返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'article_source': '中国植保网', 'counts': 148}, {'article_source': '互联网', 'counts': 141}, {'article_source': '中国食品科技网', 'counts': 30}, .....

返回数据解析：  
article_source：文章来源  
counts：文章数量

### 文章月份发布数量分析：  
#### 2.3、年份文章数量[完成]
接口：/article/date  
请求参数：无   
返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'date': '2010-11', 'counts': 29}, {'date': '2017-08', 'counts': 25},......

返回数据解析：  
date：月份  
counts：文章数量

### 词频分析：  
#### 2.4、文章标题词频分析[待完成]



## <h2 id="3">三、种植基地分析接口设计</h2>
### 区域分析：  
#### 3.1、省份种植基地数[完成]  
接口：/plantation/provincePlantationCounts
请求参数：无  
返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'province': '山东省', 'counts': 918}, {'province': '河北省', 'counts': 213},  .....

返回数据解析：    
province：省份  
counts：种植基地数量

#### 3.2、城市种植基地数[完成]  
接口：/plantation/cityPlantationCounts  
请求参数：无  
返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'city': '青岛市', 'counts': 229}, {'city': '泰安市', 'counts': 215},.....

返回数据解析：  
city：城市  
counts：种植基地数量  





## <h2 id="4">四、虫害病分析接口设计</h2>
### 虫害病分析：  
#### 4.1、基本种类分析[完成]  
接口：/diseases/info  
请求参数：无   
返回数据样例：  
{'errcode': '0', 'errmsg': '成功', 'data': [{'diseases_name': '菟丝子的防治'}, {'diseases_name': '根腐线虫病的防治'}, {'diseases_name': '叶斑病的防治'}, {'diseases_name': '金线虫病的防治'}, {'diseases_name': '茎线虫病的防治'}, {'diseases_name': '粉痴病的防治'}, {'diseases_name': '卷叶病的防治'}, {'diseases_name': '软腐病的防治'}, .......

返回数据解析：  
diseases_name：虫害病名称  

#### 4.2、基本危害词频分析[待完成]  
