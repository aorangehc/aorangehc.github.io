---
title: Protobuf
date: 2025-01-16 21:15:06  +0800
categories: [golang, 微服务, Protobuf]
---

<img src="../assets/images/protobuf/image.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

Protobuf(Protocal Buffer)，是谷歌开源的一种和语言、平台无关的，能进行扩展的，用于序列化结构化数据的协议

可用于数据的通信、数据存储，只需要定义一次数据结构，就可以使用生成的源代码，从各种数据流或者语言中写入和读取结构化数据。

Protobuf用于微服务的通信协议

## 基本语法

### 基本框架

```protobuf
syntax = "proto3";

package xxx.xxx;

option gp_package = "./xxx/xxx/xxx; xxx";

// 一共有三个部分
// 第一行是版本声明
// 第二个是包的声明，防止不同项目同名消息的冲突
// 第三个手生成文件路径和生成的Go的包名
```

### 定义服务

说明

* service表示这是一个服务（接口），关于他的命名规则，考虑到golang中通过首字母的大小写来进行区别私有和公共，所以必须大写，让其他文件能够调用，同时以后缀Service结尾，表示这是一个服务

* rpc，必须写，只能有这一个，表示使用rpc远程过程调用

* stream，流式，用于大文件传输，聊天场景或者打字机效果等等

  * 一问多答，问完之后，回答按照严格顺序返回

  * 多问一答，严格顺序输入请求，等待一个响应

  * 多问多答，完全异步的两根管子，互补阻塞

    * 模式1，一问一答，像打乒乓球一样

    * 模式2，像你和你暧昧对象聊天一样，你发10条，ta会一条，或者反过来都有可能，请求和响应走不通的通道

    * 这样的话，在golang中需要通过goroutine进行实现

```protobuf
service TestService {
        rpc IndexDocument (IndexRequest) returns (IndexResponse)
        rpc Chat (ChatRequest) returns (stream ChatReponse) // 一问多答
        rpc UploadFile (stream FileChunk) returns (UploadStatus) // 多问一答
        rpc LiveChat (stream VoiceData) returns (stream VoiceData) // 变问边答
}
```

### 定义消息

message 相当于 golang中的struct

基本语法格式：类型 字段名 = 唯一编号;

下面是一个demo

```protobuf
message IndexRequest {
        string library_id = 1; // 字符串
        int32 file_size = 2; // 整数类型int32
        bytes file_content = 3; // 文件内容使用二进制
        bool is_public = 4; // 布尔值
}
```

注意事项，唯一编号的的问题，它相当于字段的一个身份认证，在进行RPC的时候为了省流量，不传输原本的变量名，直接传输编号，为了防止编号混乱，上线之后就不要修改已有的编号，正确做法，如果编号废弃之后就空着不要用了，用新的字段值

message和Go类型对比

#### 消息中比较高级的数据结构

##### 数组(slice)

使用repeated关键字

```protobuf
message ChatResponse {
        repeated string sources = 1;
}
```

##### 字典(map)

map也就是键值对

使用map作为关键字

```protobuf
message IndexRequest {
        // Metadata map[string]string
        map<string, string> metasata = 2;
}
```

##### 枚举(enum)

使用enum作为关键字，枚举必须从0开始，通常是默认值或者是未知值

enum只能作为message一部分使用，不能进行单独传输

```protobuf
// 定义枚举 (必须从 0 开始)
enum DocType {
  UNKNOWN = 0; // 规范：第一个必须是 0，通常作为默认/未知值
  PDF = 1;
  IMAGE = 2;
  WORD = 3;
}

message Document {
  string name = 1;
  DocType type = 2; // 使用上面定义的枚举
}
```

##### 嵌套消息(nested)

```protobuf
message Author {
        string name = 1;
}

message Book {
        string title = 1;
        Author author = 2;
}
```

### 语法规范

* 消息名 (Message Name)：使用 大驼峰 (ChatRequest)。

* 字段名 (Field Name)：使用 下划线蛇形 (library\_id, file\_name)。

  * 为什么？ 因为生成的 Go 代码会自动帮你转成驼峰 (LibraryId, FileName)，但在 Proto 文件里看下划线更清晰。

* 服务名 (Service Name)：使用 大驼峰 (OmniRAGService)。

## 安装protobuf

### Mac安装

直接通过下面的指令进行安装即可

```bash
brew install protobuf

protoc --version

# 1. 安装生成数据结构的插件
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest

# 2. 安装生成 gRPC 服务的插件
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

### Win安装

在 Windows 上安装 Protobuf 和 Go 插件，主要分为 安装编译器核心 (protoc) 和 安装 Go 语言插件 两步。

由于 Windows 没有像 Homebrew 那样统一的默认包管理器，我们需要手动下载并配置环境变量。请按照以下步骤操作：

**第一步：安装编译器核心 (protoc)**

这是 Google 提供的核心工具，负责读取 .proto 文件。

1. 下载压缩包：

   * 访问 GitHub 发布页：[Protocol Buffers Releases](https://github.com/protocolbuffers/protobuf/releases)

   * 找到最新版本（例如 v25.x 或更高）。

   * 在 "Assets" 列表中，下载 protoc-xx.x-win64.zip (注意选 win64)。

2. 解压：

   * 将压缩包解压到一个你不会删除的地方，建议放在 C:\protoc。

   * 解压后，你应该能看到 bin 文件夹，里面有一个 protoc.exe。

3. 配置环境变量 (Path) —— 最关键的一步：

   * 按 Win 键，搜索 "编辑系统环境变量" 并打开。

   * 点击右下角的 "环境变量" 按钮。

   * 在下方的 "系统变量" 区域，找到 Path​，选中它，点击 "编辑"。

   * 点击右侧的 "新建"。

   * 输入你刚才解压的 bin 目录路径，例如：C:\protoc\bin。

   * 一路点击 "确定" 保存。

4. 验证：

   * 打开一个新的 CMD 或 PowerShell 窗口。

   * 输入：protoc --version

   * 如果显示版本号（如 libprotoc 25.1​），说明核心安装成功！

**第二步：安装 Go 语言插件**

你需要安装两个 Go 插件，这样 protoc 才能生成 Go 代码。

1. 打开 PowerShell 或 CMD，执行以下两条命令：

```powershell
# 1. 安装生成数据结构的插件
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest

# 2. 安装生成 gRPC 服务的插件
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

1. 检查 Go 的环境变量：

   * go install 会把插件下载到你的 $GOPATH/bin 目录下（通常是 C:\Users\你的用户名\go\bin​）。

   * 你需要确保这个路径也在你的 系统环境变量 Path 里。

   * 验证方法：在终端输入 protoc-gen-go --version。

     * 如果报错“不是内部或外部命令”，请重复“第一步”中的配置环境变量步骤，把 %USERPROFILE%\go\bin (即你的 go bin 目录) 加到 Path 里。

## protobuf使用

### 使用示例

```bash
protoc --proto_path=. \
       --go_out=paths=source_relative:. \
       --go-grpc_out=paths=source_relative:. \
       api/omnirag/v1/omnirag.proto
```

### 使用说明

* \--proto\_path=.: 告诉编译器，从当前目录（根目录）开始寻找 import 的文件。

* \--go\_out=paths=source\_relative:.:

  * 生成 .pb.go 文件（数据结构）。

  * paths=source\_relative: 表示生成的文件路径与 proto 文件同级（即生成在 api/omnirag/v1/ 下），而不是按照包名乱跑。

  * :.: 输出到当前目录。

* \--go-grpc\_out=paths=source\_relative:.:

  * 生成 \_grpc.pb.go 文件（服务接口）。

  * 配置同上。

* api/omnirag/v1/omnirag.proto: 目标文件的路径。
