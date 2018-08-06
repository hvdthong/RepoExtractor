
### **CityPicker 城市选择器**

#### **说明**

在实际的项目中一般情况下都需要使用到省市区三级联动地址选择的功能，有的公司是提供接口获取，有的公司则不是，需要自己实现。一开始，我也深受其扰，每次都是要复制一遍，就想能不能打个包出来，供大伙使用。所以自己就封装了一个，不需要自己添加数据源，直接引用即可。这就是CityPicker城市选择器的由来！

#### **功能点**

 1. 支持仿iOS滚轮实现、一级城市列表、三级城市列表
 2. 支持多种自定义属性来满足你的需求
 3. 简单的几行代码即可实现城市选择器功能

#### **数据来源**
[《中华人民共和国国家统计局-最新县及县以上行政区划代码（截止2016年7月31日）》](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html)

#### **CityPicker 城市选择器专属QQ群，欢迎加入！**


点击此处进入---------> [qq群问答](https://github.com/crazyandcoder/citypicker/issues/95)

### **效果展示**


![](http://img.blog.csdn.net/20171217104511214?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  

#### **仿iOS滚轮实现**

![](http://img.blog.csdn.net/20171217113122669?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) ![](http://img.blog.csdn.net/20171217113133546?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

#### **城市一级列表展示效果图**

 ![](http://img.blog.csdn.net/20171217110803599?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)     ![](http://img.blog.csdn.net/20171217112213023?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

#### **省市区三级列表展示效果图**

![](http://img.blog.csdn.net/20171217112838613?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) ![](http://img.blog.csdn.net/20171217112850749?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) ![](http://img.blog.csdn.net/20171217112902207?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


### **使用方法**

#### **gradle引用**

```
compile 'liji.library.dev:citypickerview:3.1.8'
```

#### **代码混淆**

```
#地区3级联动选择器

-keep class com.lljjcoder.**{
	*;
}

-dontwarn demo.**
-keep class demo.**{*;}
-dontwarn net.sourceforge.pinyin4j.**
-keep class net.sourceforge.pinyin4j.**{*;}
-keep class net.sourceforge.pinyin4j.format.**{*;}
-keep class net.sourceforge.pinyin4j.format.exception.**{*;}

```
#### **列表样式使用代码**

 1. [城市一级列表样式使用方法及demo](https://github.com/crazyandcoder/citypicker/wiki/%E6%A0%B7%E5%BC%8F%E4%BA%8C%EF%BC%88%E5%9F%8E%E5%B8%82%E4%B8%80%E7%BA%A7%E5%88%97%E8%A1%A8%E5%B1%95%E7%A4%BA%EF%BC%89)
 2. [省市区三级列表使用方法及demo](https://github.com/crazyandcoder/citypicker/wiki/%E6%A0%B7%E5%BC%8F%E4%B8%89%EF%BC%88%E7%9C%81%E5%B8%82%E5%8C%BA%E4%B8%89%E7%BA%A7%E5%88%97%E8%A1%A8%EF%BC%89)

### **仿iOS滚轮样式使用代码**

#### **注意点**

**一定要提前在Activity的onCreate里面预先加载本地城市数据，重要的事情说三遍！！！**

**一定要提前在Activity的onCreate里面预先加载本地城市数据，重要的事情说三遍！！！**

**一定要提前在Activity的onCreate里面预先加载本地城市数据，重要的事情说三遍！！！**

**3.1.0以后的版本跟以前版本有点区别，默认加载数据放在需要使用到该选择器的Activity中的onCreate方法中！！！**

**3.1.0以后的版本跟以前版本有点区别，默认加载数据放在需要使用到该选择器的Activity中的onCreate方法中！！！**

**3.1.0以后的版本跟以前版本有点区别，默认加载数据放在需要使用到该选择器的Activity中的onCreate方法中！！！**


#### **举个栗子：**

首先需要预加载数据，如我们在AddNewAddressActivity中使用到省市区选择器的话，那么我们需要提前解析本地数据，这样在弹出来的时候不会卡顿，因为本地城市数据很多。


```

public class AddNewAddressActivity extends Activity {

	//申明对象
	CityPickerView mPicker=new CityPickerView();

    @Override
    public void onCreate() {
        super.onCreate();
        /**
         * 预先加载仿iOS滚轮实现的全部数据
         */
        mPicker.init(this);
        
        //其他初始化操作...
        
    }
}

```

然后在需要弹出的地方如点击地区选择button时弹出它，

```

//添加默认的配置，不需要自己定义
CityConfig cityConfig = new CityConfig.Builder().build();
mPicker.setConfig(cityConfig);

//监听选择点击事件及返回结果
mPicker.setOnCityItemClickListener(new OnCityItemClickListener() {
            @Override
            public void onSelected(ProvinceBean province, CityBean city, DistrictBean district) {
                 
                //省份
                if (province != null) {
                    
                }
                
                //城市
                if (city != null) {
                    
                }
                
                //地区
                if (district != null) {
                    
                }
        
            }
            
            @Override
            public void onCancel() {
                ToastUtils.showLongToast(this, "已取消");
            }
        });

		//显示
        mPicker.showCityPicker( );
```

以上加载是默认属性设置下的选择器，当然我们也可以设置我们自己的样式，详细的属性设置，请看

[《详细样式设置属性大全》](https://github.com/crazyandcoder/citypicker/wiki/%E6%A0%B7%E5%BC%8F%E4%B8%80%EF%BC%88%E4%BB%BFiOS%E6%BB%9A%E8%BD%AE%E5%AE%9E%E7%8E%B0%EF%BC%89)
        
#### **返回结果的数据接口**

ProvinceBean province, CityBean city, DistrictBean district都是一样的数据结构。
```
id  //城市code
name //城市名称

```

### **下个版本要做的**

 1. 完成仿京东格式的选择器样式

### **更新说明**

#### **V3.1.8版本更新内容（2018.06.03）**

1. 发布3.1.8版本，修复三级城市列表市返回省出现的崩溃的问题


[历史更新说明](https://github.com/crazyandcoder/citypicker/wiki/%E5%8E%86%E5%8F%B2%E6%9B%B4%E6%96%B0%E8%AE%B0%E5%BD%95)

### **赞赏**

如果你喜欢 citypicker 这个开源库，感觉 citypicker 帮助到了你，可以点右上角 "Star" 支持一下 谢谢！,你也还可以扫描下面的二维码~ 请作者喝一杯牛奶，让作者更有动力写出更好的开源库服务大家。^_^ 


 ![](http://img.blog.csdn.net/20180102115819490?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)              ![](http://img.blog.csdn.net/20180102115834628?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGlqaV94Yw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 
 
 
**赞赏的伙计，请注明你们的昵称，请留下你们的联系方式(最好是GitHub地址)，谢谢合作 ^_^ 。**
 
 
### **赞赏人员列表**
[赞赏的人](https://github.com/crazyandcoder/citypicker/wiki/%E8%B5%9E%E8%B5%8F%E7%9A%84%E4%BA%BA)



 
