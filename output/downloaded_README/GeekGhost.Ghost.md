# Ghost

微影，一款纯粹的在线视频App，基于Material Design + MVP + Dagger2 + RxJava + Retrofit + Realm + Glide 

## 更改日志
#### 2017.9.15
* 1.mvp架构调整（移除自定义View层，简化代码，去除无用功）
* 2.代码优化
* 3.接口数据调整

#### 2017.6.7
* 1.调整gradle配置

#### 2016.10.24
* 1.调整mvp结构
* 2.完善设置页面（推荐好友、关于我们、建议反馈）
* 3.增加分享功能（调用系统分享）
* 4.增加美女福利页面（瀑布流）

#### 2016.10.11
* 1.增加意见反馈
* 2.修改影片详情页面（进入自动播放、影片简介展开收回，增加评论列表）
* 3.增加浏览记录页面(历史)

#### 2016.9.29
* 1.增加收藏功能（使用Realm做本地库存储）
* 2.增加播放记录功能
* 3.搜索功能

#### 2016.9.22
* 1.新增图片抽象层，上层调用不管下层具体实现
* 2.增加欢迎页面
* 3.统一签名，集成bug上报
* 4.新增主题设置

#### 2016.9.20
* 1.完成精选、专题、发现界面
* 2.节目详情界面完成
* 3.播放器界面完成


## 去做
* 1.缓存功能

## 效果

[demo下载地址](https://www.pgyer.com/bAQp)

<a href="art/01.png"><img src="art/01.png" width="40%"/></a> <a href="art/02.png"><img src="art/02.png" width="40%"/></a>

<a href="art/03.png"><img src="art/03.png" width="40%"/></a> <a href="art/04.png"><img src="art/04.png" width="40%"/></a>

<a href="art/11.png"><img src="art/11.png" width="40%"/></a> <a href="art/12.png"><img src="art/12.png" width="40%"/></a>

<!--<a href="art/05.png"><img src="art/05.png" width="40%"/></a> <a href="art/06.png"><img src="art/06.png" width="40%"/></a>-->

<a href="art/07.png"><img src="art/07.png" width="40%"/></a> <a href="art/08.png"><img src="art/08.png" width="40%"/></a>

<a href="art/09.png"><img src="art/09.png" width="40%"/></a> <a href="art/10.png"><img src="art/10.png" width="40%"/></a>



# 技术点
* 使用RxJava配合Retrofit2做网络请求
* 使用RxUtil对线程操作和网络请求结果处理做了封装
* 使用RxPresenter对订阅的生命周期做管理
* 使用AndroidEventBus来方便组件间的通信
* 使用Material Design控件和动画
* 使用MVP架构整个项目，对应于model、ui、presenter三个包
* 使用Realm做阅读记录和收藏记录的增、删、查、改
* 使用Glide做图片的处理和加载
* 使用RecyclerView实现下拉刷新、上拉加载、侧滑删除、长按拖曳
* 支持主题设置
* 包含搜索、收藏、历史等功能

### RES:
[iconfont](http://www.iconfont.cn/) 提供了icon素材

[material UP](http://www.material.uplabs.com/) 提供了Material Design风格的素材

[Launcher icons](http://romannurik.github.io/AndroidAssetStudio/icons-launcher.html)

### LIB:
#### UI
* [MaterialSearchView](https://github.com/MiguelCatalan/MaterialSearchView)
* [multiline-collapsingtoolbar](https://github.com/opacapp/multiline-collapsingtoolbar)

#### RX

* [RxJava](https://github.com/ReactiveX/RxJava)
* [RxAndroid](https://github.com/ReactiveX/RxAndroid)
* [RxBinding](https://github.com/JakeWharton/RxBinding)

#### NETWORK

* [Gson](https://github.com/google/gson)
* [Retrofit](https://github.com/square/retrofit)
* [OkHttp](https://github.com/square/okhttp)
* [Glide](https://github.com/bumptech/glide)

#### DI
* [ButterKnife](https://github.com/JakeWharton/butterknife)

#### FRAGMENT

* [Fragmentation](https://github.com/YoKeyword/Fragmentation)

#### LOG

* [Logger](https://github.com/orhanobut/logger)

#### DB

* [Realm](https://github.com/realm/realm-java)

#### CANARY

* [BlockCanary](https://github.com/markzhai/AndroidPerformanceMonitor)
* [LeakCanary](https://github.com/square/leakcanary)

#### THANKS

* [JieCaoVideoPlayer](https://github.com/lipangit/JieCaoVideoPlayer)
* [EasyRecyclerView](https://github.com/Jude95/EasyRecyclerView)
* [GanK](https://github.com/dongjunkun/GanK)
* 美女福利图片接口来[自干货集中营](http://gank.io/api)

## About us

We are developer, We are brothers, We are a group.

caopeng：A adults

[csdn](http://blog.csdn.net/jiankeufo)

[Github](https://github.com/caopeng000)

yxc：A kid

[简书](http://www.jianshu.com/u/2c351e91afa7)

[Github](https://github.com/stevenMieMie)

JJZhang：Like Mom

[csdn](http://blog.sina.com.cn/jiqiren2231856598)

[Github](https://github.com/2231856598)

If you want to make friends with us, You can focus on our blog.


## License

Copyright (c) 2016 codeestX

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 个人练习使用，api和素材均来源网络，如有侵权请告知，立马删除。如果因他人下载使用产生纠纷均与本人无关。
