# Final Year Project on Fair K-Center Clustering
By Timothy Cheung

**There are two methods to run the server:**
- Docker: minimal setup
- Install all dependencies: better for development

## Docker Setup:
build image:
```docker build -t colourful-k-center .```
run image:
```docker run -dp 5000:5000 colourful-k-center```
the app can be accessed at
```localhost:5000```

## Development Setup
install dependencies:
```
pip install -r requirements.txt
cd webapp
yarn install
yarn build
```
### install glpk (windows)
https://sourceforge.net/projects/winglpk/

### install glpk (linux):
```
sudo apt-get install -y glpk-utils
```

### run
Run server ```python3 run.py```

## Run tests
```python3 -m pytest tests```

## Deploy to Heroku
Create a new app on Heroku, name it ```<app_name>```. Change directory to the root of this repo and execute the following:
```
heroku container:push web --app <app_name>
heroku container:release web --app <app_name>
```

## Stats
[![codecov](https://codecov.io/gh/timothy-ch-cheung/k-center/branch/master/graph/badge.svg?token=n5JVnL4MUa)](https://codecov.io/gh/timothy-ch-cheung/k-center)
