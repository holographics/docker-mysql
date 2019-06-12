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
