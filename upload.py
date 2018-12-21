//进入到工程文件夹下
1.$ cd 到工程文件夹下

//初始化
2.$ git init

//将所有文件夹添加到仓库
3.$ git add .

4.$ git commit -m"添加代码"

//关联远程仓库 ,https地址就是仓库的地址
5.$ git remote add origin https://gitee.com/chenqiangOSChina/cqweibo.git

//将文件推送到远程仓库
6.$ git pull origin master

执行到第六步以后如果直接执行 git push -u origin master 的话会报错 


需要执行7.拉取READEME.md文件

//这一步是将git仓库的READEME.md文件拉倒本地工程文件下
7.$ git pull --rebase origin master

//推送到远程仓库
8.$ git push -u origin master

执行完上一步后,会出现输入用户名,出入你的git用户名 


输入用户名回车,再输入密码,密码输入是没有反应的,直接输入完密码回车
