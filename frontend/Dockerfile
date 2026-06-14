FROM nginx:1.30-alpine
EXPOSE 80 443
COPY ./nginx/ssl/ /etc/nginx/ssl/
COPY ./src/ /usr/share/nginx/html/
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf