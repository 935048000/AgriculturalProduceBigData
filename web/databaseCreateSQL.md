# 数据库建表语言
爬虫数据规划

## city_info 表：存放城市信息
CREATE TABLE `city_info` (  
  `id` int NOT NULL AUTO_INCREMENT,  
  `city` varchar(255) COLLATE utf8_bin DEFAULT NULL,  
  `city_code` varchar(255) COLLATE utf8_bin DEFAULT NULL,  
  `begetter_code` varchar(255) COLLATE utf8_bin DEFAULT NULL,  
  PRIMARY KEY (`id`),  
  UNIQUE KEY `code` (`city_code`) USING BTREE,  
  KEY `city` (`city`) USING BTREE  
) ENGINE=InnoDB AUTO_INCREMENT=6837 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='城市编码信息';  


## enterprise_info 表：存放企业信息
CREATE TABLE `enterprise_info` (  
  `id` int NOT NULL AUTO_INCREMENT,  
  `enterprise_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '市场名称',  
  `enterprise_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '市场编码',  
  `province` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '省',  
  `city` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '市',  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='企业信息表';  


## plantation_info表：存放种植基地信息
CREATE TABLE `plantation_info` (  
  `id` int NOT NULL AUTO_INCREMENT,  
  `plantation_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '市场名称',  
  `plantation_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '市场编码',  
  `province` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '省',  
  `city` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '市',  
  `counts` int DEFAULT NULL COMMENT '数量',  
  PRIMARY KEY (`id`),  
  KEY `city` (`city`) USING BTREE  
) ENGINE=InnoDB AUTO_INCREMENT=6837 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='种植基地信息表';  


## 相关技术文章表
CREATE TABLE `prd_article` (  
  `id` int NOT NULL AUTO_INCREMENT,  
  `article_title` varchar(255) COLLATE utf8_bin DEFAULT NULL,  
  `article_url` varchar(255) COLLATE utf8_bin DEFAULT NULL,  
  `article_source` varchar(255) COLLATE utf8_bin DEFAULT NULL,  
  `article_date` datetime DEFAULT NULL,  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=730 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='相关技术文章';  

## 产品疾病信息表
CREATE TABLE `prd_diseases` (  
  `id` int NOT NULL AUTO_INCREMENT,  
  `produce_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '产品名称',  
  `diseases_name` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '疾病名称',  
  `diseases_img` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '疾病图片',  
  `diseases_info` varchar(5000) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL COMMENT '疾病介绍',  
  `diseases_url` varchar(255) COLLATE utf8_bin DEFAULT NULL,  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='产品疾病信息';  

## 产品价格表（主表）
CREATE TABLE `prd_price` (  
  `id` int NOT NULL AUTO_INCREMENT,  
  `date` datetime DEFAULT NULL COMMENT '日期',  
  `products` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '商品名称',  
  `bazaar` varchar(100) COLLATE utf8_bin DEFAULT NULL COMMENT '市场',  
  `mini_price` decimal(4,2) DEFAULT NULL COMMENT '最低价格',  
  `max_price` decimal(4,2) DEFAULT NULL COMMENT '最高价格',  
  `avg_price` decimal(4,2) DEFAULT NULL COMMENT '平均价格',  
  `unit` varchar(5) COLLATE utf8_bin DEFAULT NULL COMMENT '单位',  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=75361 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='产品价格表';  


## prd_products_info：产品数据表
CREATE TABLE `prd_products_info` (  
  `id` int NOT NULL AUTO_INCREMENT,  
  `products_code` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '产品编码',  
  `products_name` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '产品名称',  
  `products_alias` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '别名',  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='产品表';  
  








