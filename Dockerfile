# start from official python docker image version 3.10.5
FROM python:3.10.5

# set current working directory to /usr/src/app
WORKDIR /usr/src/app

# copy requirements.txt to present working directory
COPY requirements.txt ./

# run pip install for the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy all the present working directory from local machine to docker image
COPY . .

# default command is python script file
CMD [ "python", "./data_2_kc_1.py" ]