# uwsgi 记录
## 配置
生产环境配置
http://www.cnblogs.com/luchuangao/articles/Uwsgi.html

> 配置逻辑
*配置中可以用for if-?? 配合占位符 %(_) 进行逻辑处理*
[点击查看](https://uwsgi-docs.readthedocs.io/en/latest/ConfigLogic.html)

> 配置中的魔术变量 可以用 uwsgi.magic_table 查看
[点击查看](https://uwsgi-docs.readthedocs.io/en/latest/Configuration.html#magic-variables)

> 加载配置文件
	
	uwsgi config.ini # 通过磁盘文件
	uwsgi --ini http://uwsgi.it/configs/myapp.ini # HTTP
	uwsgi --xml - # standard input
	uwsgi --yaml fd://0 # file descriptor
	uwsgi --json 'exec://nc 192.168.11.2:33000' # arbitrary executable
    
     # 通过配置文件启动
        uwsgi --ini uwsgi.ini
        # 会生成两个文件
            PID文件 他是标识这个程序所处的状态
            SOCK文件  他是用来和其他程序通信的
    # 停止uwsgi
        uwsgi --stop uwsgi.pid

    # 重载配置
        uwsgi --reload uwsgi.ini

1. http 直接作为web服务器来使用
2. http-socket 给web服务器upstream做代理用的
3. socket 给web服务器作为解析脚本用的

> 不要用root身份运行uwsgi实例（可以用root启动uwsgi）使用uid 和 gid 选项选择用户(限制权限) 

	id user 会得到 uid 和 gid
    命令举例	uwsgi --uid 1000 --http-socket :80
	
[添加用户/组](https://www.jianshu.com/p/f468e02f38au)

nginx 配置

    server {
        listen       80;
        server_name  localhost;

        location / {
            #root   html;
            #index  index.html index.htm;
            include        uwsgi_params;
            uwsgi_pass   127.0.0.1:9000;
        }
    }

