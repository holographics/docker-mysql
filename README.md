#### MySql Docker Official Images
`https://hub.docker.com/_/mysql`

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
#### Dial to running container bash:
`docker exec -it 7eb19152a84f bash`
#### Login to mysql:
```
mysql -uroot -pnewpassword
mysql -uwpuser -pwpuser@
```
#### Grant root previlegies to wpuser: 
`GRANT ALL PRIVILEGES ON * . * TO 'wpuser'@'%';`

#### Login to mysql running on container in one line:
`docker exec -it 7eb19152a84f mysql -uroot -pnewpassword`
#### Set mysql user permission in one line:
`docker exec -it 4a0b248f06f5  mysql -uroot -pnewpassword -se "GRANT ALL PRIVILEGES ON * . * TO 'wpuser'@'%';"`

#### Drop and create user:
```
DROP User 'golden'@'localhost';
DROP User 'golden'@'%';
CREATE USER 'golden'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'golden'@'%';
```
#### Run mysql in safe mode to change root password:
`mysqld_safe --skip-grant-tables --skip-networking &`

#### Run mysql service:
`systemctl start mysqld.service`

#### List all configuration files:
`mysqld --verbose --help | grep -A 1 "Default options"`

#### For container started without flag retreive the generated password:
```
docker run --expose=3333 -p 3333:3306  -d mysql/mysql-server
docker run --expose=3333 -p 3333:3306  -d mysql/mysql-server
docker logs 74f2c0281066 2>&1 | grep GENERATED
docker exec -it faa2e56fb5ab mysql -uroot -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'newpassword';
```

### Basic git commands

#### Get the pointer of origin
`git remote -v`
#### List branches
`git branch --list`
#### Set the origin
`git remote set-url origin git@github.com:USERNAME/REPOSITORY.git`
#### Update local branch2 with remote branch to which origin points to
`git pull origin branch2`

#### Update the local `branch2` by merging it with the local `master` branch.<br/>After the merge, push the updated local `branch2` to the remote `branch2`:
```
git merge master
git push origin branch2
```
#### To bake requirements.txt from env
`pip freeze > requirements.txt`
#### To install requirements.txt to env
`pip install -r requirements.txt`
