
https://uwsgi-docs-cn.readthedocs.io/zh_CN/latest/WSGIquickstart.html#

配置错误导致的错误

	location / {
	    include uwsgi_params;
	    uwsgi_pass 127.0.0.1:3031; # 上下两个前缀都是 uwsgi
	}

	2018/08/07 15:26:34 [error] 28739#0: *7 upstream prematurely closed connection while reading response header from upstream, client: 127.0.0.1, server: localhost, request: "GET / HTTP/1.0", upstream:     "fastcgi://127.0.0.1:9000", host: "localhost"

nginx try_file
https://www.hi-linux.com/posts/53878.html
