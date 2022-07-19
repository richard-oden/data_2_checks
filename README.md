# Docker
A Dockerfile exists with comments to explain what each line does.

## Install docker
To utilize Docker you will need to [install Docker](https://www.docker.com/products/docker-desktop/).

## Run Container

Next, you can run the docker image

```sh
docker run --rm jmschu02/code_louisville_kc 
```
This will run the docker image as a container.
`--rm` will delete the docker container after it exits.


## Build Image

Want to build the image locally?

```sh
docker build -t jmschu02/code_louisville_kc -f Dockerfile .
```
this will build the docker image and tag it `jmschu02/code_louisville_kc` building the Dockerfile with the pwd (.)

## Learn More?

Want to run this interactively and test?
```sh
docker run --rm -it jmschu02/code_louisville_kc /bin/bash
```

Want to learn more about [docker build](https://docs.docker.com/engine/reference/commandline/build/) and [docker run](https://docs.docker.com/engine/reference/run/)? please click their respective links.