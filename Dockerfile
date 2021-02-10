FROM ubuntu:20.04
MAINTAINER Tim Cheung "tcc746@student.bham.ac.uk"
RUN apt-get update && apt-get install -y python3-pip python-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]