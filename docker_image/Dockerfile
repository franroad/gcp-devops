#install the desired image 
FROM python:3.8-slim-buster 

#define the working directory you can put whatever you prefer, the copy will copy the files here
WORKDIR /app

# copying files in the container <source> <destination>
COPY requirements.txt requirements.txt

# the image includes python but not the libraty or other dependencies
RUN pip3 install  -r requirements.txt

# Copy what ever is in the directory (local) into the container <source> <destination>, the working directory
COPY . .

#command python and argumetns for the container and flask
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]


