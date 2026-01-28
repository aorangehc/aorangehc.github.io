---
title: go-zero框架下简单微服务实现
date: 2025-01-11 09:58:39  +0800
categories: [golang,  微服务, demo]
---

<img src="../assets/images/gozeroservicedemo/Go-zero demo-image-2.png" alt="daily" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

## 项目设计

### 说明

项目是通过 zo-zero 框架实现一个简单的用户订单系统，包括两个微服务用户服务和订单服务，通过 API 接口能够分别调用两个服务的接口，用户服务暴露 RPC 服务接口供订单服务进行调用。下面截图是我的操作过程

<img src="../assets/images/gozeroservicedemo/Go-zero demo-image.png" alt="daily" style="width: 75%; height: auto; display: block; margin-left: auto; margin-right: auto;">

<img src="../assets/images/gozeroservicedemo/Go-zero demo-image-1.png" alt="daily" style="width: 75%; height: auto; display: block; margin-left: auto; margin-right: auto;">

### API

**goctl指令**

```bash
goctl api go -api user.api -dir . -style goZero  
goctl api go -api order.api -dir . -style goZero
```

**User**

```go
syntax = "v1"

// 进行项目的简单说明
info (
    title:   "实现简单的用户服务"
    author:  "aorangehc"
    date:    "2025年 11 月 11 日"
    version: "v1"
)

// 注册需要用户名、密码、手机号码，要做唯一性检测
type RegisterReq {
    UserName string `json:"username"`
    Password string `json:"password"`
    Mobile   string `json:"mobile"`
    Gender   string `json:"gender"` // male|female|unknown
    NickName string `json:"nickname"`
}

type RegisterResp {
    success bool   `json:"success"` // 注册是否成功
    Message string `json:"message"` // 注册报错信息
    Id      int64  `json:"id"` // 成功注册返回的 id
}

type LoginReq {
    UserName string `json:"username"`
    Password string `json:"password"`
}

type LoginResp {
    Token string `json:"token"`
}

type UserInfoReq {
    Id int64 `json:"id"`
    Id int64 `json:"token"`
}

type UserInfoResp {
    Id       int64  `json:"id"`
    Token    string `json:"token"`
    UserName string `json:"username"`
    Mobile   string `json:"mobile"`
    Gender   string `json:"gender"`
    NickName string `json:"nickname"`
    CreateAt string `json:"createAt"` // 注册时间
    UpdateAt string `json:"updateAt"` // 最后更新时间
}

// 用户信息更新
type UserUpdateReq {
    Id       int64  `json:"id"`
    UserName string `json:"username"`
    Password string `json:"password"`
    Mobile   string `json:"mobile"`
    Gender   string `json:"gender"` // male|female|unknown
    NickName string `json:"nickname"`
}

type UserUpdateResp {
    success bool   `json:"success"`
    Message string `json:"message"` // 更新报错信息
}

// 定义用户服务的 Api
service user-api {
    @handler register
    post /api/user/register (RegisterReq) returns (RegisterResp)

    @handler login
    post /api/user/login (LoginReq) returns (LoginResp)

    @handler userInfo // 获取用户信息
    get /api/user/:id (UserInfoReq) returns (UserInfoResp)
}
```

**Order**

```go
syntax = "v1"

info (
    title:   "订单服务简单 demo"
    author:  "aorangehc"
    date:    "2025年 11 月 11 日"
    version: "v1"
)

// 创建订单
type CreateReq {
    UserId  int64 `json:"userId"`
    GoodsId int64 `json:"goodsId"`
    Num     int64 `json:"num"`
    Amount  int64 `json:"amount"`
}

type CreateResp {
    OrderSn string `json:"orderSn"`
}

// 查看订单详情
type DetailReq {
    OrderSn string `json:"orderSn"`
}

type DetailResp {
    OrderSn  string `json:"orderSn"`
    UserId   int64  `json:"userId"`
    GoodsId  int64  `json:"goodsid"`
    Num      int64  `json:"num"`
    Amount   int64  `json:"amount"`
    Status   int64  `json:"status"`
    CreateAt string `json:"createAt"`
}

// 删除订单
type DeleteReq {
    userId  int64  `json:"userId"`
    OrderSn string `json:"orderSn"`
}

type DeleteResp {
    success bool   `json:"success"`
    Message string `json:"message"`
}

service order-api {
    @handler create
    post /api/order/create (CreateReq) returns (CreateResp)

    @handler detail
    get /api/order/:orderSn (DetailReq) returns (DetailResp)

    @handler delete
    delete /api/order/delete (DeleteReq) returns (DeleteResp)
}
```

### RPC

**goctl指令**

```bash
goctl rpc protoc user.proto --go_out=. --go-grpc_out=. --zrpc_out=.
```

**User**

```protobuf
// 暴露一个 user 服务对外接口，获取用户信息

syntax = "proto3";

option go_package = "./user";

// 定义请求结构体
message GetUserInfoRequest {
    int64 user_id = 1; // 用户ID
}

// 定义响应结构体
message GetUserInfoResponse {
    int64 user_id = 1; // 用户ID
    string user_name = 2; // 用户名
    int64 gender = 3; // 用户性别
}

// 定义 UserService 服务
service UserService {
    // 获取用户信息
    rpc GetUserInfo(GetUserInfoRequest) returns (GetUserInfoResponse); 
}
```

### MySQL

**goctl指令**

```bash
goctl model mysql ddl -src="./user.sql" -dir="./sql/model" -c  
goctl model mysql ddl -src="./order.sql" --dir="./sql/model" -c
```

**User**

```sql
CREATE TABLE user (
    id bigint AUTO_INCREMENT,
    name varchar(255) NULL COMMENT '用户名',
    password varchar(255) NOT NULL DEFAULT '' COMMENT '密码',
    mobile varchar(255) NOT NULL DEFAULT '' COMMENT '手机号码',
    gender char(10) NOT NULL DEFAULT 'male' COMMENT '性别,male|female|unknown',
    nickname varchar(255) NULL DEFAULT '' COMMENT '昵称',
    type tinyint(1) NULL DEFAULT 0 COMMENT '用户类型, 0:普通用户,1:VIP用户,用于测试golang关键字',
    create_at timestamp NULL,
    update_at timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE mobile_index (mobile),
    UNIQUE name_index (name),
    PRIMARY KEY (id)
) ENGINE = InnoDB COLLATE utf8mb4_general_ci COMMENT '用户表';
```

**Order**

```sql
CREATE TABLE `order` (
    `order_sn` VARCHAR(64) NOT NULL COMMENT '订单号',
    `user_id` BIGINT NOT NULL DEFAULT 0 COMMENT '用户ID',
    `goods_id` BIGINT NOT NULL DEFAULT 0 COMMENT '商品ID',
    `num` BIGINT NOT NULL DEFAULT 0 COMMENT '数量',
    `amount` BIGINT NOT NULL DEFAULT 0 COMMENT '金额',
    `status` INT NOT NULL DEFAULT 0 COMMENT '状态',
    `create_at` DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `delete_at` DATETIME DEFAULT NULL COMMENT '删除时间',
    PRIMARY KEY (`order_sn`)
) ENGINE=InnoDB COLLATE utf8mb4_general_ci COMMENT='订单表';

```

## MySQL配置和model操作



## 注册



## 缓存



## 日志



## login 接口



## JWT 鉴权



## 中间件



## RPC服务和调用



## 注册中心-consul



## RPC 拦截器



## 错误处理



## 修改模板生成自定义代码



## 参考资料
