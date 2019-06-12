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
`docker run --expose=3333 -p 3333:3306 -e MYSQL_ROOT_PASSWORD=newpassword -e MYSQL_USER=wpuser -e MYSQL_PASSWORD=wpuser@ -e MYSQL_DATABASE=wordpress_db --name wordpressdb -d mysql/mysql-server --skip-grant-tables` 
#### List running containers:
`docker ps`
#### Dial to running container bash:
`docker exec -it 7eb19152a84f bash`
# Login to mysql:
`mysql -uroot -pnewpassword`
# Grant root previlegies: 
`GRANT ALL PRIVILEGES ON * . * TO 'wpuser'@'%';`
