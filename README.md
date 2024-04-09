# 使用QQ作为图床的Typora上传服务

### 开始使用

1. 安装 [go-cqhttp](https://docs.go-cqhttp.org/) 添加http通信配置

2. 安装依赖项

   ```shell
   pip install -m requirements.txt
   ```

3. 修改main.py中的QQid，robot_id，ip ，port 分别为自己的QQ号，go-cqhttp登录的机器人QQ号，go-cqhttp服务的ip地址，go-cqhttp服务的端口号

4. 设置Typora上传服务为自定义命令，命令为   <python.exe路径> <main.py路径>

