---
title: golang学习记录（11）
date: 2024-10-20 13:59:51  +0800
categories: [golang, golang基础学习]
---

# 接口--interface

> go语言中interface是一种非常重要的类型，是非常重要的组成部分

## 1、鸭子类型

> 鸭子类型
>
> 当一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也想鸭子，那这只鸟就是鸭子
>
> 鸭子类型强调的是事物的方法，而不是内部的结构
>
> 也就是说，只要一个对象实现了接口的所有方法，那么这个对象就可以被认为是实现了这个接口，就能将这个对象作为这个接口的实例

## 2、接口的定义

> 接口的定义需要用到type和interface关键字，具体的定义格式如下：

```go
type 接口名 interface{
    方法名1(参数列表) 返回值列表
    方法名2(参数列表) 返回值列表
   ...
}
```

下面是一个例子：

```go
type Duck interface{
    Gaga()
    Walk()
    Swimming()
}

type pskDuck struct{
    legs int
}

func (pd *pskDuck) Gaga(){
    fmt.Println("嘎嘎嘎")
}

func (pd *pskDuck) Walk(){
    fmt.Println("走")
}

func (pd *pskDuck) Swimming(){
    fmt.Println("游泳")
}

func main(){
    var duck Duck = &pskDuck{}
    duck.Gaga()
    duck.Walk()
    duck.Swimming()
}

```

## 3、多接口实现

> 在实际的应用场景中，接口不应该写的太大，一般一个接口只实现一个方法

```go
type Duck interface{
    Gaga()
}

type Duck2 interface{
    Walk()
}

type Duck3 interface{
    Swimming()
}

type pskDuck struct{}
、
func (pd *pskDuck) Gaga(){
    fmt.Println("嘎嘎嘎")
}

func (pd *pskDuck) Walk(){
    fmt.Println("走")
}

func (pd *pskDuck) Swimming(){
    fmt.Println("游泳")
}

func main(){
    var duck Duck = &pskDuck{}
    var duck2 Duck2 = &pskDuck{}
}
```

> 在上面的例子中，pskDuck实现了Duck、Duck2、Duck3三个接口，但是在main函数中，只声明了Duck接口，但是却可以将pskDuck的实例赋值给Duck接口，这是因为pskDuck实现了Duck接口的所有方法，所以可以将pskDuck的实例赋值给Duck接口
>
> 接口也可以作为结构体的参数
>
> 接口的使用非常灵活
>
> 代码的解耦
>
> 一个类型实现多个接口。一个接口实现多个类型
>
> ……

## 4、接口与动态类型传参

> 断言
>

举个例子，做一个加法计算器：

```go
func add(a, b interface{}) interface{}{
    switch a.(type){
    case int:
        ai, _ := a.(int)
        bi, _ := b.(int)
        return ai + bi

    case int32:
        ai, _ := a.(int32)
        bi, _ := b.(int32)
        return ai + bi
    

    case float32:
        ai, _ := a.(float32)
        bi, _ := b.(float32)
        return ai + bi
    
    //……

    default:
        return 0
    }
}


func main(){
    fmt.Println(add(1, 2))
    fmt.Println(add(1, 3))
    fmt.Println(add(1.0, 2.0))
}

```

## 5、接口嵌套

> 接口嵌套达到代码复用的目的

```go
type MyWriter interface{
    Write(string)
}

type MyReader interface{
    Reader() string
}

type MyReaderWriter interface{
    MyReader
    MyWriter
    ReadWriter()
}

type SreadWriter struct{}

func (srw *SreadWriter) Read(){
    fmt.Println("read")
}

func (srw *SreadWriter) Write(){
    fmt.Println("write")
}

func (srw *SreadWriter) ReadWriter(){
    fmt.Println("readWriter")
}

func main(){
    var mrw MyReaderWriter = &SreadWriter{}
    mrw.Read()

}
```

## 6、接口与slice常见的错误

> slice不能作为接口的参数，因为slice是一个引用类型，但是接口是一个值类型，所以不能将slice作为接口的参数，但是可以将slice的指针作为接口的参数
>

```go
func mPrint(data ... interface{}){
    for _, value := range data{
        fmt.Println(value)
    }
}

func main(){
    //这样是支持的
    var data = []interface{}{
        "aaaaa",
        19,
        1800.00,
    }
    mPrint(data...)
}
```