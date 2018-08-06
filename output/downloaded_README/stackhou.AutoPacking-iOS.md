# 一、背景

在实际开发中，需要不停的打各种包，开发人员忙于新需求实现，打包时重复而且没有意义的事情。于是造了这个轮子，配置好参数一键上传到内测网站(蒲公英、Fir等)或者APPStore。源码地址：[https://github.com/stackhou/AutoPacking-iOS](https://github.com/stackhou/AutoPacking-iOS)

# 二、预览效果图

## 2.1 执行脚本 和 选项配置

![](https://ws3.sinaimg.cn/large/006tNbRwly1fkfjub1e73j30g60jmmzh.jpg)

## 2.2 开始构建

![](https://ws4.sinaimg.cn/large/006tNbRwly1fkfjve1ztcj30kx0fr0u9.jpg)

## 2.3 构建成功并开始导出ipa

![](https://ws2.sinaimg.cn/large/006tNbRwly1fkfjwg2ey7j30dd044zk9.jpg)

## 2.4 导出ipa成功并上传到内测网站

![](https://ws1.sinaimg.cn/large/006tNbRwly1fkfjximvk6j30le0750u0.jpg)

# 二、脚本环境

基于 Xcode 9 设计，注意Xcode 8和9有所区别，请参考我的另一篇：[http://www.jianshu.com/p/ba179c731e3f](http://www.jianshu.com/p/ba179c731e3f) ,
如有问题，欢迎指正。

# 三、功能

* 支持 xcworkspace 和 xcodeproj 两种类型的工程；
* 可以自动化清理、编译、构建工程导出ipa；
* 支持Debug 和 Release；
* 支持导出app-store, ad-hoc, enterprise, development的包；
* 支持自动上传到蒲公英或者Fir等内测网站

# 四、实现

## 4.1   更新RVM

```bash
curl -L get.rvm.io | bash -s stable
```

## 4.2 所需知识点

```bash

xcodebuild clean 			// 等同于Xcode下点击Product -> Clean
xcodebuild -xcworkspace  	// 等同于xcworkspace工程 command+B
xcodebuild -xcodeproj 		// 等同于xcworkspace工程 command+B
xcodebuild archive 			// 等同于Xcode下点击Product -> Archive
xcodebuild -exportArchive	// 等同于点击 export

```
# 五、脚本

## 配置完项目结构(可以根据自己喜好自由定义)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fng6snbfdsj30yk0bamz6.jpg)

```bash
#!/bin/sh
# 该脚本使用方法
# 源码地址：https://github.com/stackhou
# step 1. 在工程根目录新建Shell文件夹，在该文件夹中新建文件autopacking.sh，将该脚本复制到autopacking.sh文件并保存(或者直接复制该文件);
# step 2. 配置该脚本;
# step 2. cd 该脚本目录，运行chmod +x autopacking.sh;
# step 3. 终端运行 sh autopacking.sh;
# step 4. 选择不同选项....
# step 5. Success  🎉 🎉 🎉!

# ************************* 配置 Start ********************************

# 上传到蒲公英
__PGYER_U_KEY="4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxb"
__PGYER_API_KEY="3xxxxxxxxxxxxxxxxxxxxxxxxxx5"

# 上传到 Fir
__FIR_API_TOKEN="xKKdjdldlodeikK626266skdkkddK"

# 证书
__CODE_SIGN_DISTRIBUTION="iPhone Distribution: xxxxxxxxxxxCo., Ltd."
__CODE_SIGN_DEVELOPMENT="iPhone Developer: xxxx xxxx (5xxxxxxxxxx2V)"

# 换行符
__LINE_BREAK_LEFT="\n\033[32;1m*********"
__LINE_BREAK_RIGHT="***************\033[0m\n"
__SLEEP_TIME=0.3

# 指定Target
echo "\033[36;1m请选择 SCHEME (输入序号, 按回车即可) \033[0m"
echo "\033[33;1m1. APPxxxxDev \033[0m"
echo "\033[33;1m2. APPxxxxTest \033[0m"
echo "\033[33;1m3. APPxxxxRelease \033[0m"
echo "\033[33;1m4. APPxxxxAppStore \033[0m\n"

read parameter
sleep ${__SLEEP_TIME}
__SCHEME_NAME_SELECTED="${parameter}"

# 判读用户是否有输入
if [[ "${__SCHEME_NAME_SELECTED}" == "1" ]]; then
__SCHEME_NAME="APPxxxxDev"
elif [[ "${__SCHEME_NAME_SELECTED}" == "2" ]]; then
__SCHEME_NAME="APPxxxxTest"
elif [[ "${__SCHEME_NAME_SELECTED}" == "3" ]]; then
__SCHEME_NAME="APPxxxxRelease"
elif [[ "${__SCHEME_NAME_SELECTED}" == "4" ]]; then
__SCHEME_NAME="APPxxxxAppStore"
else
echo "${__LINE_BREAK_LEFT} 您输入 SCHEME 参数无效!!! ${__LINE_BREAK_RIGHT}"
exit 1
fi

# ************************* 配置 END ********************************

# 指定打包编译的模式，如：Release, Debug...
echo "\033[36;1m请选择 BUILD_CONFIGURATION (输入序号, 按回车即可) \033[0m"
echo "\033[33;1m1. Debug \033[0m"
echo "\033[33;1m2. Release \033[0m"

read parameter
sleep ${__SLEEP_TIME}
__BUILD_CONFIGURATION_SELECTED="${parameter}"

# 判读用户是否有输入
if [[ "${__BUILD_CONFIGURATION_SELECTED}" == "1" ]]; then
__BUILD_CONFIGURATION="Debug"
elif [[ "${__BUILD_CONFIGURATION_SELECTED}" == "2" ]]; then
__BUILD_CONFIGURATION="Release"
else
echo "${__LINE_BREAK_LEFT} 您输入 BUILD_CONFIGURATION 参数无效!!! ${__LINE_BREAK_RIGHT}"
exit 1
fi

# 工程类型(.xcworkspace项目,赋值true; .xcodeproj项目, 赋值false)
echo "\033[36;1m请选择是否是.xcworkspace项目(输入序号, 按回车即可) \033[0m"
echo "\033[33;1m1. 是 \033[0m"
echo "\033[33;1m2. 否 \033[0m"

read parameter
sleep ${__SLEEP_TIME}
__IS_WORKSPACE_SELECTE="${parameter}"

# 判读用户是否有输入
if [[ "${__IS_WORKSPACE_SELECTE}" == "1" ]]; then
__IS_WORKSPACE=true
elif [[ "${__IS_WORKSPACE_SELECTE}" == "2" ]]; then
__IS_WORKSPACE=false
else
echo "${__LINE_BREAK_LEFT} 您输入是否是.xcworkspace项目 参数无效!!! ${__LINE_BREAK_RIGHT}"
exit 1
fi

# AdHoc, AppStore, Enterprise, Development
echo "\033[36;1m请选择打包方式(输入序号, 按回车即可) \033[0m"
echo "\033[33;1m1. AdHoc \033[0m"
echo "\033[33;1m2. AppStore \033[0m"
echo "\033[33;1m3. Enterprise \033[0m"
echo "\033[33;1m4. Development \033[0m\n"
# 读取用户输入并存到变量里
read parameter
sleep ${__SLEEP_TIME}
__BUILD_METHOD="${parameter}"

# 判读用户是否有输入
if [[ "${__BUILD_METHOD}" == "1" ]]; then
ExportOptionsPlistPath="./Shell/Plist/AdHocExportOptionsPlist.plist"
elif [[ "${__BUILD_METHOD}" == "2" ]]; then
ExportOptionsPlistPath="./Shell/Plist/AppStoreExportOptionsPlist.plist"
elif [[ "${__BUILD_METHOD}" == "3" ]]; then
ExportOptionsPlistPath="./Shell/Plist/EnterpriseExportOptionsPlist.plist"
elif [[ "${__BUILD_METHOD}" == "4" ]]; then
ExportOptionsPlistPath="./Shell/Plist/DevelopmentExportOptionsPlist.plist"
else
echo "${__LINE_BREAK_LEFT} 您输入的打包方式参数无效!!! ${__LINE_BREAK_RIGHT}"
exit 1
fi

# 选择内测网站 用Fir或者pgyer
echo "\033[36;1m请选择ipa内测发布平台 (输入序号, 按回车即可) \033[0m"
echo "\033[33;1m1. None \033[0m"
echo "\033[33;1m2. Pgyer \033[0m"
echo "\033[33;1m3. Fir \033[0m"
echo "\033[33;1m4. Pgyer and Fir \033[0m\n"

# 读取用户输入并存到变量里
read parameter
sleep ${__SLEEP_TIME}
__UPLOAD_TYPE_SELECTED="${parameter}"

# 成功出包后是否自动打开文件夹
echo "\033[36;1m成功出包后是否自动打开文件夹(输入序号, 按回车即可) \033[0m"
echo "\033[33;1m1. 是 \033[0m"
echo "\033[33;1m2. 否 \033[0m"

read parameter
sleep ${__SLEEP_TIME}
__IS_AUTO_OPENT_FILE_SELECTED="${parameter}"

# 判读用户是否有输入
if [[ "${__IS_AUTO_OPENT_FILE_SELECTED}" == "1" ]]; then
__IS_AUTO_OPENT_FILE=true
elif [[ "${__IS_AUTO_OPENT_FILE_SELECTED}" == "2" ]]; then
__IS_AUTO_OPENT_FILE=false
else
echo "${__LINE_BREAK_LEFT} 您输入的成功出包后是否自动打开文件夹 参数错误!!! ${__LINE_BREAK_RIGHT}"
exit 1
fi

echo "${__LINE_BREAK_LEFT} 您选择了 ${__SCHEME_NAME}-${__BUILD_CONFIGURATION} 模式 ${__LINE_BREAK_RIGHT}"

# 配置完毕是否开始打包
echo "\033[36;1m配置完毕是否立即开始打包 (输入序号, 按回车即可) \033[0m"
echo "\033[33;1m1. 是 \033[0m"
echo "\033[33;1m2. 否 \033[0m"

read parameter
sleep ${__SLEEP_TIME}
__IS_START_PACKINF="${parameter}"

# 判读用户是否有输入
if [[ "${__IS_START_PACKINF}" == "1" ]]; then
echo "${__LINE_BREAK_LEFT} 立即开始 ${__LINE_BREAK_RIGHT}"
elif [[ "${__IS_START_PACKINF}" == "2" ]]; then
echo "${__LINE_BREAK_LEFT} 您退出了打包 ${__LINE_BREAK_RIGHT}"
exit 1
else
echo "${__LINE_BREAK_LEFT} 您输入 是否立即开始打包 参数无效!!! ${__LINE_BREAK_RIGHT}"
exit 1
fi

# ===============================自动打包部分=============================

echo "${__LINE_BREAK_LEFT} 使用打包配置文件路径=${ExportOptionsPlistPath} ${__LINE_BREAK_RIGHT}"
# 打包计时
__CONSUME_TIME=0
# 回退到工程目录
cd ../
__PROGECT_PATH=`pwd`
echo "${__LINE_BREAK_LEFT} 进入工程目录=${__PROGECT_PATH} ${__LINE_BREAK_RIGHT}"

# 获取项目名称
__PROJECT_NAME=`find . -name *.xcodeproj | awk -F "[/.]" '{print $(NF-1)}'`

# 已经指定Target的Info.plist文件路径
__CURRENT_INFO_PLIST_NAME="${__SCHEME_NAME}-Info.plist"
# 获取 Info.plist 路径
__CURRENT_INFO_PLIST_PATH="${__PROJECT_NAME}/Configs/${__CURRENT_INFO_PLIST_NAME}"
# 当前的plist文件路径
echo "${__LINE_BREAK_LEFT} 当前Info.plist路径= ${__CURRENT_INFO_PLIST_PATH} ${__LINE_BREAK_RIGHT}"
# 获取版本号
__BUNDLE_VERSION=`/usr/libexec/PlistBuddy -c "Print CFBundleShortVersionString" ${__CURRENT_INFO_PLIST_PATH}`
# 获取编译版本号
__BUNDLE_BUILD_VERSION=`/usr/libexec/PlistBuddy -c "Print CFBundleVersion" ${__CURRENT_INFO_PLIST_PATH}`

# 打印版本信息
echo "${__LINE_BREAK_LEFT} 打包版本=${__BUNDLE_VERSION} 编译版本=${__BUNDLE_BUILD_VERSION} ${__LINE_BREAK_RIGHT}"

# 编译生成文件目录
__EXPORT_PATH="./build"

# 指定输出文件目录不存在则创建
if test -d "${__EXPORT_PATH}" ; then
echo "${__LINE_BREAK_LEFT} 保存归档文件和ipa的路径=${__EXPORT_PATH} ${__LINE_BREAK_RIGHT}"
rm -rf ${__EXPORT_PATH}
else
mkdir -pv ${__EXPORT_PATH}
fi

# 归档文件路径
__EXPORT_ARCHIVE_PATH="${__EXPORT_PATH}/${__SCHEME_NAME}.xcarchive"
# ipa 导出路径
__EXPORT_IPA_PATH="${__EXPORT_PATH}"
# 获取时间 如:201706011145
__CURRENT_DATE="$(date +%Y%m%d_%H%M%S)"
# ipa 名字
__IPA_NAME="${__SCHEME_NAME}_V${__BUNDLE_BUILD_VERSION}_${__CURRENT_DATE}"

echo "${__LINE_BREAK_LEFT} 打包APP名字=${__IPA_NAME} ${__LINE_BREAK_RIGHT}"

# 修改编辑版本
#__SET_BUNDLE_BUILD_VERSION="${__BUNDLE_BUILD_VERSION}.${__CURRENT_DATE}"
#/usr/libexec/PlistBuddy -c "Set :CFBundleVersion ${__SET_BUNDLE_BUILD_VERSION}" "${__CURRENT_INFO_PLIST_PATH}"

echo "${__LINE_BREAK_LEFT} 开始构建项目 ${__LINE_BREAK_RIGHT}"

if ${__IS_WORKSPACE} ; then
#echo "${__LINE_BREAK_LEFT} 开始pod ${__LINE_BREAK_RIGHT}"
#pod install --verbose --no-repo-update
#echo "${__LINE_BREAK_LEFT} pod完成 ${__LINE_BREAK_RIGHT}"

if [[ ${__BUILD_CONFIGURATION} == "Debug" ]]; then
echo "${__LINE_BREAK_LEFT} 您选择了以 xcworkspace-Debug 模式打包 ${__LINE_BREAK_RIGHT}"
# step 1. Clean
xcodebuild clean  -workspace ${__PROJECT_NAME}.xcworkspace \
-scheme ${__SCHEME_NAME} \
-configuration ${__BUILD_CONFIGURATION}

# step 2. Archive
xcodebuild archive  -workspace ${__PROJECT_NAME}.xcworkspace \
-scheme ${__SCHEME_NAME} \
-configuration ${__BUILD_CONFIGURATION} \
-archivePath ${__EXPORT_ARCHIVE_PATH} \
CFBundleVersion=${__BUNDLE_BUILD_VERSION} \
-destination generic/platform=ios \
CODE_SIGN_IDENTITY="${__CODE_SIGN_DEVELOPMENT}"

elif [[ ${__BUILD_CONFIGURATION} == "Release" ]]; then
echo "${__LINE_BREAK_LEFT} 您选择了以 xcworkspace-Release 模式打包 ${__LINE_BREAK_RIGHT}"
# step 1. Clean
xcodebuild clean  -workspace ${__PROJECT_NAME}.xcworkspace \
-scheme ${__SCHEME_NAME} \
-configuration ${__BUILD_CONFIGURATION}

# step 2. Archive
xcodebuild archive  -workspace ${__PROJECT_NAME}.xcworkspace \
-scheme ${__SCHEME_NAME} \
-configuration ${__BUILD_CONFIGURATION} \
-archivePath ${__EXPORT_ARCHIVE_PATH} \
CFBundleVersion=${__BUNDLE_BUILD_VERSION} \
-destination generic/platform=ios \
CODE_SIGN_IDENTITY="${__CODE_SIGN_DISTRIBUTION}"
else
echo "${__LINE_BREAK_LEFT} 您输入的参数不对 😢 😢 😢 ${__LINE_BREAK_RIGHT}"
echo "Usage:\n"
echo "sh autopacking.sh"
echo "sh autopacking.sh"
exit 1
fi
else
if [[ ${__BUILD_CONFIGURATION} == "Debug" ]] ; then
echo "${__LINE_BREAK_LEFT}您选择了以 xcodeproj-Debug 模式打包 ${__LINE_BREAK_RIGHT}"
# step 1. Clean
xcodebuild clean  -project ${__PROJECT_NAME}.xcodeproj \
-scheme ${__SCHEME_NAME} \
-configuration ${__BUILD_CONFIGURATION} \
-alltargets

# step 2. Archive
xcodebuild archive  -project ${__PROJECT_NAME}.xcodeproj \
-scheme ${__SCHEME_NAME} \
-configuration ${__BUILD_CONFIGURATION} \
-archivePath ${__EXPORT_ARCHIVE_PATH} \
CFBundleVersion=${__BUNDLE_BUILD_VERSION} \
-destination generic/platform=ios \
CODE_SIGN_IDENTITY="${__CODE_SIGN_DEVELOPMENT}"


elif [[ ${__BUILD_CONFIGURATION} == "Release" ]]; then
echo "${__LINE_BREAK_LEFT} 您选择了以 xcodeproj-Release 模式打包 ${__LINE_BREAK_RIGHT}"
# step 1. Clean
xcodebuild clean  -project ${__PROJECT_NAME}.xcodeproj \
-scheme ${__SCHEME_NAME} \
-configuration ${__BUILD_CONFIGURATION} \
-alltargets
# step 2. Archive
xcodebuild archive  -project ${__PROJECT_NAME}.xcodeproj \
-scheme ${__SCHEME_NAME} \
-configuration ${__BUILD_CONFIGURATION} \
-archivePath ${__EXPORT_ARCHIVE_PATH} \
CFBundleVersion=${__BUNDLE_BUILD_VERSION} \
-destination generic/platform=ios \
CODE_SIGN_IDENTITY="${__CODE_SIGN_DISTRIBUTION}"

else
echo "${__LINE_BREAK_LEFT} 您输入的参数不对 😢 😢 😢 ${__LINE_BREAK_RIGHT}"
echo "Usage:\n"
echo "sh autopacking.sh"
echo "sh autopacking.sh"
exit 1
fi
fi

# 检查是否构建成功
# xcarchive 实际是一个文件夹不是一个文件所以使用 -d 判断
if test -d "${__EXPORT_ARCHIVE_PATH}" ; then
echo "${__LINE_BREAK_LEFT} 项目构建成功 🚀 🚀 🚀 ${__LINE_BREAK_RIGHT}"
else
echo "${__LINE_BREAK_LEFT} 项目构建失败 😢 😢 😢 ${__LINE_BREAK_RIGHT}"
exit 1
fi

echo "${__LINE_BREAK_LEFT} 开始导出ipa文件 ${__LINE_BREAK_RIGHT}"

xcodebuild -exportArchive -archivePath ${__EXPORT_ARCHIVE_PATH} \
-exportPath ${__EXPORT_IPA_PATH} \
-destination generic/platform=ios \
-exportOptionsPlist ${ExportOptionsPlistPath} \
-allowProvisioningUpdates

# 修改ipa文件名称
mv ${__EXPORT_IPA_PATH}/${__SCHEME_NAME}.ipa ${__EXPORT_IPA_PATH}/${__IPA_NAME}.ipa

# 检查文件是否存在
if test -f "${__EXPORT_IPA_PATH}/${__IPA_NAME}.ipa" ; then
echo "${__LINE_BREAK_LEFT} 导出 ${__IPA_NAME}.ipa 包成功 🎉 🎉 🎉 ${__LINE_BREAK_RIGHT}"

if test -n "${__UPLOAD_TYPE_SELECTED}"
then

if [[ "${__UPLOAD_TYPE_SELECTED}" == "1" ]] ; then
echo "${__LINE_BREAK_LEFT} 您选择了不上传到内测网站 ${__LINE_BREAK_RIGHT}"
elif [[ "${__UPLOAD_TYPE_SELECTED}" == "2" ]]; then

curl -F "file=@${__EXPORT_IPA_PATH}/${__IPA_NAME}.ipa" \
-F "uKey=$__PGYER_U_KEY" \
-F "_api_key=$__PGYER_API_KEY" \
"http://www.pgyer.com/apiv1/app/upload"

echo "${__LINE_BREAK_LEFT} 上传 ${__IPA_NAME}.ipa 包 到 pgyer 成功 🎉 🎉 🎉 ${__LINE_BREAK_RIGHT}"
elif [[ "${__UPLOAD_TYPE_SELECTED}" == "3" ]]; then

fir login -T ${__FIR_API_TOKEN}
fir publish "${__EXPORT_IPA_PATH}/${__IPA_NAME}.ipa"

echo "${__LINE_BREAK_LEFT} 上传 ${__IPA_NAME}.ipa 包 到 fir 成功 🎉 🎉 🎉 ${__LINE_BREAK_RIGHT}"
elif [[ "${__UPLOAD_TYPE_SELECTED}" == "4" ]]; then

fir login -T ${__FIR_API_TOKEN}
fir publish "${__EXPORT_IPA_PATH}/${__IPA_NAME}.ipa"

echo "${__LINE_BREAK_LEFT} 上传 ${__IPA_NAME}.ipa 包 到 fir 成功 🎉 🎉 🎉 ${__LINE_BREAK_RIGHT}"

curl -F "file=@{${__EXPORT_IPA_PATH}/${__IPA_NAME}.ipa}" \
-F "uKey=$__PGYER_U_KEY" \
-F "_api_key=$__PGYER_API_KEY" \
"http://www.pgyer.com/apiv1/app/upload"

echo "${__LINE_BREAK_LEFT} 上传 ${__IPA_NAME}.ipa 包 到 pgyer 成功 🎉 🎉 🎉 ${__LINE_BREAK_RIGHT}"
else
echo "${__LINE_BREAK_LEFT} 您输入 上传内测网站 参数无效!!! ${__LINE_BREAK_RIGHT}"
exit 1
fi

# 自动打开文件夹
if ${__IS_AUTO_OPENT_FILE} ; then
open ${__EXPORT_IPA_PATH}
fi

fi

else
echo "${__LINE_BREAK_LEFT} 导出 ${__IPA_NAME}.ipa 包失败 😢 😢 😢 ${__LINE_BREAK_RIGHT}"
exit 1
fi

# 输出打包总用时
echo "${__LINE_BREAK_LEFT} 使用YJShell脚本打包总耗时: ${SECONDS}s ${__LINE_BREAK_RIGHT}"

```
# 六、注意事项

注意ExportOptions.plist配置，如下所示：

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>compileBitcode</key>
    <false/>
    <key>method</key>
    <string>enterprise</string>
    <key>provisioningProfiles</key>
    <dict>
        <key>com.houmanager.enterprise.test</key>
        <string>com.houmanager.enterprise.test</string>
    </dict>
    <key>signingCertificate</key>
    <string>iPhone Distribution</string>
    <key>signingStyle</key>
    <string>manual</string>
    <key>stripSwiftSymbols</key>
    <true/>
    <key>teamID</key>
    <string>5XXXXXXXXXXXHM</string>
    <key>thinning</key>
    <string><none></string>
</dict>
</plist>
```

如果不知道怎么填写，手动用Xcode9打包，导出文件中会有ExportOptions.plist

![](https://ws3.sinaimg.cn/large/006tKfTcly1fke46g4ppwj305f02maa1.jpg)

直接复制到指定路径或者手动copy即可。

---

源码地址：[https://github.com/stackhou/AutoPacking-iOS](https://github.com/stackhou/AutoPacking-iOS)

---