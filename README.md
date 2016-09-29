# 专为公司开发的自动化测试平台，用于车载娱乐系统的测试
## 介绍
测试工具客户端  
提供界面方便测试人员选择步骤来组织测试场景，并选择要运行的测试场景进行测试，测试结束可直接查看测试报告  

测试工具服务端  
向客户端提供测试用例编写需要的测试步骤信息，保存测试场景到数据库等  

测试脚本工程  
测试场景执行的胶水代码，采用BDD框架

## 采用语言和工具
python3.4  
behave  
pyqt5.5.1  
uiautomator(python版)  
flask  

#QGATP环境部署
##服务端部署
###环境准备
####所需软件
* python3.4+
* flask
* flask-sqlalchemy
* sqlalchemy-migrate
* flask-whooshalchemy

###部署步骤
#### 创建虚拟环境
> mkdir atps
> python -m venv flask

#### 安装环境所需要的库

##### windows用户执行以下命令
> $flask\Scripts\pip.exe install flask
> $flask\Scripts\pip.exe install flask-sqlalchemy
> $flask\Scripts\pip.exe install sqlalchemy-migrate
> $flask\Scripts\pip.exe install flask-whooshalchemy

##### linux用户执行以下命令
> $flask\bin\pip install flask
> $flask\bin\pip install flask-sqlalchemy
> $flask\bin\pip install sqlalchemy-migrate
> $flask\bin\pip install flask-whooshalchemy

##### 启动服务端
1. 复制服务端工程(flask目录不复制)到atps目录下
2. 修改run.py文件中的ip地址配置
3. 在atps目录下运行 $flask\Scripts\python.exe run.py

##客户端部署
###环境准备
* 下载地址： https://pan.baidu.com/s/1o8rndFG  (ahbz)

####所需软件
* python3.4+
* requests
* behave
* pillow
* pyserial
* gitpython
* uiautomator
* pyqt5
* jdk

###部署步骤(以上软件都均已正确安装)
1. 新建文件夹atp
2. 将atpc和autotestproject放在atp目录下
3. 打开cmd窗口并进入atpc目录
4. 执行命令$ python run.py打开客户端应用

##客户端使用
###设置
1. 打开客户端程序进入主界面  
![主界面截图](http://c.hiphotos.baidu.com/image/pic/item/3812b31bb051f819746727cad2b44aed2f73e7f4.jpg)
2. 打开菜单栏 '设置|应用设置'，进入‘应用设置’界面,设置后保存
![应用设置界面](http://e.hiphotos.baidu.com/image/pic/item/91529822720e0cf303d91f5c0246f21fbe09aa6f.jpg)
* 脚本目录: 填写存放测试工程的目录路径
* 服务器Ip:填写服务器的ip地址，默认：10.10.99.87
* 服务器Port:填写服务器的启动端口，默认：5000
3. 打开菜单 '设置|脚本设置'，进入’脚本设置‘界面，设置后保存
![脚本设置界面](http://f.hiphotos.baidu.com/image/pic/item/9922720e0cf3d7caaed86ed1fa1fbe096b63a96f.jpg)
* 音频播放器路径: 本地播放器执行文件的路径。 PS:路径加入到path中，并设置播放一段音频后停止，建议使用foobar2000
* 音频文件路径: 本地音频文件存放路径，用于测试语音场景的录音文件
* 运行日志存放路径: 用例运行过程中产生的失败截图路径
* 车机设备编号: 车机的serialnum，通过命令行adb devices获取
* 手机设备编号: 手机的serialnum，通过命令行adb devices获取
* 手机蓝牙名称: 手机蓝牙的名字， 用于测试蓝牙场景连接蓝牙
* 测试版本编号: 默认即可
* usb音乐名列表: u盘音乐中的音乐名称，英文逗号分隔，用来测试U盘音乐，判断当前播放的音乐是否为U盘音乐

###添加编辑用例
####用例编辑界面介绍
点击主界面的’添加‘按钮，进入’用例编辑‘界面
![用例编辑界面](http://f.hiphotos.baidu.com/image/pic/item/0824ab18972bd407886afa7d73899e510eb30984.jpg)  
* 用例名称: 不为空，并且唯一，有重复会有错误提示
* 用例类型: 必选，选择用例场景类型，如：基本类型等，用于快速筛选用例
* 所属模块：必选，选择用例所测试的模块，如：音乐，视频等，用于快速筛选用例
* 上移，下移，删除是针对用例步骤的操作，选中用例步骤就可以调整步骤顺序或者删除操作
* 左侧列表为所有的用例步骤信息，可以通过上面的下拉框来筛选操作的步骤和验证的步骤，也可以通过搜索框，根据关键字搜索对应的步骤信息
* 中间单列表格为展示用例的步骤信息，步骤按照操作顺序来组合用例
* 右边表格展示步骤的参数信息，包括参数名称，参数值

####添加用例
1. 填写用例名称，用例类型，所属模块等信息
2. 双击要添加的步骤，就会添加步骤到中间的用例表格中
3. 选中要调整的用例步骤，选择相应的操作(上移，下移，删除)
4. 选中用例步骤，如果步骤需要填写参数，在右侧的表格中会出现参数信息，在参数值表格中填写具体值并回车保存
> 如果有的参数名为o_result,意为该步骤会有结果返回，参数值务必用'o_’开头如下图

![有返回值的步骤参数](http://f.hiphotos.baidu.com/image/pic/item/2fdda3cc7cd98d104cbf1cb1293fb80e7aec90c2.jpg)
5. 点击保存按钮保存用例
6. 回到主界面，点击刷新按钮，即可看到新添加的用例信息

####编辑用例
1. 在主界面，双击用例名称即可打开‘用例编辑’界面
2. 编辑用例的用例名称不可更改，如果要更改的话，需要先删除再新建，如果有需要可放开这个限制
3. 用例编辑可参照添加用例操作

###删除用例
1. 在主界面选中要删除用例的复选框，点击‘删除’按钮即可删除所选用例

###执行用例
1. 通过主界面顶部的用例类型和所属模块快速筛选用例，或者用例搜索框来筛选用例
2. 选中要执行的用例前的复选框
3. 设置用例执行次数（默认是一次），点击‘运行’按钮即可执行用例
4. 在主界面下方的执行历史列表可看到当前用例执行状态

###查看用例执行结果
1. 点击主界面中‘执行历史列表’指定任务的查看单元格即可打开执行结果展示界面，如下图:
![结果查看界面](http://f.hiphotos.baidu.com/image/pic/item/6a63f6246b600c335a578f6f124c510fd9f9a16f.jpg)
2. 如果用例执行失败或者用例执行中，界面会提示相应的错误信息，如下图:
![用例执行失败截图](http://e.hiphotos.baidu.com/image/pic/item/9213b07eca80653820f0a5939fdda144ad348213.jpg)
3. 如果用例执行成功，将会看到用例汇总信息，成功的用例(绿色展示)，失败的用例(红色展示)
4. 双击用例名称获取前面的三角图形，会看到具体用例步骤信息和错误信息
5. 点击‘下载报告’按钮，并指定报告存放路径(包含文件名),即可本地查看测试报告信息

###查看自动化测试持续集成
1. 点击主界面右上角的‘持续集成’按钮，即可跳转持续集成界面，如下图:
![持续集成截图](http://b.hiphotos.baidu.com/image/pic/item/d0c8a786c9177f3e56224a8e78cf3bc79f3d561a.jpg)

##QA
1. 在选中用例运行的过程中在客户端终端会报以下错误
>   File "c:\users\shenshun\appdata\local\programs\python\python35\lib\site-packag
es\behave\runner.py", line 303, in exec_file
    code = compile(f.read(), filename2, 'exec')
UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 397: illegal
multibyte sequence
> 解决方法：
> 打开错误中指定的文件runner.py在303行附近修改如下代码
with open(filename) as f:改为 with open(filename, encoding='utf-8') as f:

2. 在执行有输入框的用例，会遇到无法输入内容
> 解决方法：在车机上安装utf7ime.apk输入法并设置为默认输入法即可
> 设置默认输入法命令:
adb shell settings put secure default_input_method jp.jun_nama.test.utf7ime/.Utf7ImeService
> 还原擎感输入法命令:
adb shell settings put secure default_input_method com.android.inputmethod.qingganime/.QingganIME



