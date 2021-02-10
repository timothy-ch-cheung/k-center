FROM ubuntu:20.04
MAINTAINER Tim Cheung "tcc746@student.bham.ac.uk"
RUN apt-get update && apt-get install -y python3-pip python-dev && apt-get -y install curl
RUN apt-get install -y glpk-utils
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
ENV NODE_ENV=PRODUCTION
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]