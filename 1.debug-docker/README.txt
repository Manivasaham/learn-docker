How to debug the docker container

using docker logs
docker logs <container-id or name> -f
you can jump into the container and see the actually what is execting inside the container
press ctrl + c to come out of the container, but sill the container executes normally

docker logs <container-id or name>
it jsut print out the logs in the container

docker attach <container-id or name>
this also jump into the container, 
here to come out press ctrl + p then ctrl + q to come out (read escape sequence)
if you press ctrl + c container will stop processing

hence always use docker logs <container-id or name> -f 
