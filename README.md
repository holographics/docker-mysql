`nano`
#### ADD YOUR INFORMATION
`control + X`
`Type: Y`
`enter`

#### Remove all containers:
`docker rm $(docker ps -a -q)`
#### Remove all images:
`docker rmi $(docker images -q)`

`docker run --expose=3333 -p 3333:3306 -e MYSQL_ROOT_PASSWORD=newpassword -e MYSQL_USER=wpuser -e MYSQL_PASSWORD=wpuser@ -e MYSQL_DATABASE=wordpress_db --name wordpressdb -d mysql/mysql-server` --skip-grant-tables
