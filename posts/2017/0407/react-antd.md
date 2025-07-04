---
title: 搭建 React+Antd 的前端应用
tags: ["Antd", "JavaScript", "React"]
categories: ["JavaScript"]
date: 2017-04-07 00:07:30 +08:00
description: 文章介绍了如何使用 `create-react-app` 初始化 React 项目，集成 Ant Design UI 组件库，并进行按需加载的优化配置。
articleGPT: 本文介绍了如何使用 `create-react-app` 初始化 React 项目，引入 Ant Design 并进行按需加载等高级配置。
---

使用以下命令之前，请先安装 Node.js，直接去官网下载安装即可：<https://nodejs.org/>  

## 一、使用 create-react-app 初始化 React 项目

[create-react-app](https://github.com/facebookincubator/create-react-app)
是业界最优秀的 React 应用开发工具之一，可以使用简单的命令完成 React 项目的初始化配置。

#### 1. 安装

```shell
npm install -g create-react-app yarn
```

#### 2. 创建项目

```shell
create-react-app ebs-react-demo
```

#### 3. 启动初始化好的 app

```shell
cd ebs-react-demo
yarn start
```

访问 `http://localhost:3000/` 即可访问初始化好的 React 页面了。

## 二、引入 antd

#### 1. 使用 yarn 安装 antd

```shell
yarn add antd
```

#### 2. 体验 Antd

修改 src/App.js 文件如下：

```JavaScript
import React, {Component} from 'react';
import {Steps} from 'antd';
import './App.css';

const Step = Steps.Step;

class App extends Component {
        render() {
        return (
        <div className="App">
        <Steps current={2}>
                <Step status="finish" title="初始化项目" description="使用 create-react-app 初始化 React 项目。"/>
                <Step status="process" title="添加 Antd" description="在 React 项目中添加 Antd 组件。"/>
                <Step status="wait" title="高级配置" description="进行一些高级配置。"/>
                <Step status="wait" title="添加 React-Router" description="添加 React-Router "/>
                <Step status="wait" icon="smile-o" title="自由发挥" description="这一条只是试一下 icon"/>
        </Steps>
        </div>
        );
        }
}
export default App;
```

修改 src/App.css 文件如下：

```less
@import '~antd/dist/antd.css';

.App {
        width: 800px;
        margin: 100px 0 0 100px;
}
```

如果已经使用 yarn start 命令启动过服务器，直接刷新页面即可看到效果。

## 三、高级配置

#### 1. 添加webpack，Babel 插件 和默认配置等

```shell
yarn run eject
```

2. 配置按需加载

Antd组件很多，不是所有的组件我们都要是使用，只加载我们使用到的组件，以减小代码文件的大小

运行命令安装 babel-plugin-import 插件

```shell
yarn add babel-plugin-import --dev
```

修改 webpack 配置文件，在 config 目录下，webpack.config.dev.js
是开发环境配置文件，webpack.config.prod.js 是产品发布配置文件，两份配置文件基本相同，以修改webpack.config.dev.js
为例：

找到 module.exports > module > loaders 数组的第二个元素，在 query 下添加 plugins：

```JavaScript
// Process JS with Babel.
{
test: /\.(js|jsx)$/,
include: paths.appSrc,
loader: 'babel',
query: {
//下面三行代码是新增的
plugins: [
  ['import', [{libraryName: "antd", style: 'css'}]],
],
// This is a feature of `babel-loader` for webpack (not Babel itself).
// It enables caching results in ./node_modules/.cache/babel-loader/
// directory for faster rebuilds.
cacheDirectory: true
}
},
```

接下来删除 src/App.css 文件中的下面代码删除，插件会根据需要按需加载文件。

```JavaScript
`@import '~antd/dist/antd.css';`
```
