# CUMT_login
中国矿业大学 校园网自动登录
# 用户信息
在每次打开时都会检测C:\Users\用户名\Documents\login路径是否存在存放用户信息的account_info.txt
如果没有会自动创建文件及路径
# 开机自启
如果需要开机自登录，请将校园网登录.exe或者它的快捷方式放入windows启动文件夹内，路径为 C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
# 编译
已经使用pyinstaller打包成了exe文件，右边realese自取
# 全平台
后续会更新全平台的版本，目前使用beeware框架只实现了Windows版本，完善后会在github上架
