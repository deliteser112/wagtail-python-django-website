
server {
	listen 80;

	access_log /var/www/hg-budva/logs/access.log;
	error_log /var/www/hg-budva/logs/error.log;

	server_name hgbudvanskarivijera.com www.hgbudvanskarivijera.com localhost;

	location / {
            client_max_body_size 100M;
            include uwsgi_params;
            uwsgi_pass unix:/var/www/hg-budva/.venv/var/run/uwsgi.sock;
        }

	location /static/ {
	    root /var/www/hg-budva/hgbudva;
	}
	location /media/ {
	    root /var/www/hg-budva/hgbudva;
	}
	location /favicon.ico {
	    root /var/www/hg-budva/hgbudva/static/assets/images;
	}
        location = /robots.txt {
            alias /var/www/hg-budva/robots.txt;
        }
        location /sitemap.xml {
            alias /var/www/hg-budva/sitemap.xml;
        }
	location /index.php {
	    return 301 https://hgbudvanskarivijera.com;
	}
}
