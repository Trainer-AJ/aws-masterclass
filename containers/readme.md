# Docker setup
```docker
 docker build . -t image-name
```

1. But problem you can't push it
2. Error:
```
docker push oj09/v1
Using default tag: latest
The push refers to repository [docker.io/oj09/v1]
An image does not exist locally with the tag: oj09/v1
```
3. Change existing image
```docker
 docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
v1           latest    bcc76f200c8b   10 minutes ago   188MB
nginx        stable    6a5ee1954d86   8 days ago       188MB

> d > docker tag bcc76f200c8b oj09/simple-webpage:6june
```
4. Push it => dockerhub/reponame:tag
```
docker push oj09/simple-webpage:6june
```
5. log in to Docker hub watch it => https://hub.docker.com/repository/docker/oj09/simple-webpage/tags

# ECS 
[AWS Docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html)
1. Create ECS Cluster => default fargate
2. crate a task from left side => docker image `oj09/simple-webpage:6june` and security group => `port 80`
3. go in cluster => create service => choose task 
4. In the Services tab, under Service name, choose the service you created in Step 3: Create the service.
Choose the Tasks tab, and then choose the task in your service.
On the task page, in the Configuration section, under Public IP, choose Open address.
