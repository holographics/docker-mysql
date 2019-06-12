`nano`
#### ADD YOUR INFORMATION
`control + X`
`Type: Y`
`enter`

#### Remove all containers:
`docker rm $(docker ps -a -q)`
#### Remove all images:
`docker rmi $(docker images -q)`
#### Run docker in background:
`docker run --expose=3333 -p 3333:3306 -e MYSQL_ROOT_PASSWORD=newpassword -e MYSQL_USER=wpuser -e MYSQL_PASSWORD=wpuser@ -e MYSQL_DATABASE=wordpress_db --name wordpressdb -d mysql/mysql-server` 
#### List running containers:
`docker ps`
#### See the container log:
`docker logs 7eb19152a84f`
`docker logs  0fcba609ce6a 2>&1 | grep GENERATED`
#### Dial to running container bash:
`docker exec -it 7eb19152a84f bash`
#### Login to mysql:
`mysql -uroot -pnewpassword`
#### Grant root previlegies to wpuser: 
`GRANT ALL PRIVILEGES ON * . * TO 'wpuser'@'%';`

#### Login to mysql running on container in one line:
`docker exec -it 7eb19152a84f mysql -uroot -pnewpassword`
#### Set mysql user permission in one line:
`docker exec -it 4a0b248f06f5  mysql -uroot -pnewpassword -se "GRANT ALL PRIVILEGES ON * . * TO 'wpuser'@'%';"`

#### Drop and create user:
`DROP User 'golden'@'localhost';`
`DROP User 'golden'@'%';`
`CREATE USER 'golden'@'%' IDENTIFIED BY 'password';`
`GRANT ALL PRIVILEGES ON * . * TO 'golden'@'%';`

#### Run mysql in safe mode to change root password:
`mysqld_safe --skip-grant-tables --skip-networking &`

#### Run mysql service:
`systemctl start mysqld.service`
