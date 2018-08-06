# OuNews 简单的新闻客户端 #

## 一、为什么写这个？ ##

一直想练习MVP模式开发应用，把学习的RxJava、Retrofit等热门的开源库结合起来，于是写了这么一款新闻阅读软件，
有新闻、图片、视频三大模块，使用Retrofit和Okhttp实现无网读缓存，有网根据过期时间重新请求，
还有边缘或整页侧滑、夜间模式切换等小功能，还写了几个自定义小控件，虽然无啥卵用，但是学到了很多东西，很有收获。

## 二、运行截图 ##

![](/pic/1.png) 
![](/pic/2.png) 

![](/pic/3.png) 
![](/pic/4.png) 

![](/pic/5.png) 
![](/pic/6.png) 

![](/pic/7.png) 
![](/pic/8.png) 

![](/pic/9.png) 
![](/pic/10.png) 

![](/pic/11.png) 
![](/pic/12.png)

## 三、用到的开源库 ##
* [Quick-News API来自此项目，特此感谢](https://github.com/tigerguixh/QuickNews)
* [RxJava 响应式编程框架](https://github.com/ReactiveX/RxJava)
* [Retrofit2.0 REST安卓客户端请求库](https://github.com/square/retrofit)
* [OkHttp3 网络请求](https://github.com/square/okhttp)
* [Glide 图片加载](https://github.com/bumptech/glide)
* [GreenDao 数据库操作](https://github.com/greenrobot/greenDAO)
* [PhotoView 图片缩放](https://github.com/chrisbanes/PhotoView)
* [Ijkplayer 视频播放](https://github.com/Bilibili/ijkplayer)
* [AndroidChangeSkin 无需重启换肤](https://github.com/hongyangAndroid/AndroidChangeSkin)
* ......

感谢各位大神无私的开源精神。

## 四、一些零散的知识点 ##

MVP模式代码学习<br>https://github.com/antoniolg/androidmvp</br>

使用Retrofit和Okhttp实现网络缓存。无网读缓存，有网根据过期时间重新请求<br>http://www.jianshu.com/p/9c3b4ea108a7</br>

Retrofit+RxJava实战日志(5)-如何获取缓存<br>http://blog.csdn.net/efan006/article/details/50549107</br>

Drawable 着色的后向兼容方案<br>http://www.cnblogs.com/helloandroid/p/4779061.html</br>

Java基础加强总结(一)——注解(Annotation)<br>http://www.cnblogs.com/xdp-gacl/p/3622275.html</br>

Android实现RecyclerView侧滑删除和长按拖拽-ItemTouchHelper<br>http://blog.csdn.net/u010687392/article/details/47950199</br>

基于RxJava、RxAndroid的EventBus实现<br>http://www.cnblogs.com/tiantianbyconan/p/4578699.html</br>

深入浅出RxJava<br>http://blog.csdn.net/lzyzsd/article/details/41833541</br>

## 五、声明 ##

应用中展示的所有内容均搜集自互联网，若内容有侵权请联系作者进行删除处理。本应用仅用作分享与学习。

## 六、关于作者 ##

微博：http://weibo.com/palfansinheart

CSDN博客：http://blog.csdn.net/oushangfeng123?viewmode=contents























