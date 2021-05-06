FROM ubuntu:20.04
MAINTAINER Tim Cheung "tcc746@student.bham.ac.uk"
RUN apt-get update && apt-get install -y python3-pip python-dev && apt-get -y install curl
RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash -
RUN apt-get -y install nodejs
RUN npm install --global yarn
RUN apt-get install -y glpk-utils
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
RUN yarn --cwd ./webapp install
RUN yarn --cwd ./webapp build
ENV NODE_ENV=PRODUCTION
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]
