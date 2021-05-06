# On the *k*-center and Colourful *k*-center
There are two demonstrations for the code, web app only and full development install. Running the web app through Docker is very simple, whereas the full development install is slightly more involved.

webapp demos:
- learn about *k*-center problems
- solution visualisation and interactive solution visualisation

full development demos:
- all webapp demos
- CLI interface:
    - algorithm benchmarking on ORLIB, GOWALLA and SYNTHETIC
    - memory profiling for algorithms
- End to end snapshot regression tests on Cypress

## Web app only
### prerequisites
Docker:
- Windows: https://docs.docker.com/docker-for-windows/install/
- Ubuntu: https://docs.docker.com/engine/install/ubuntu/

### install
from project root run
```shell
docker build -t colourful-k-center .
docker run -dp 5000:5000 colourful-k-center
```

### demos
open the webpage at localhost:5000/

## Full development
### prerequisites
- Python 3.9
- GLPK
    - Windows: https://sourceforge.net/projects/winglpk/
    - Ubuntu: ```sudo apt install glpk-utils``` or https://www.gnu.org/software/glpk/
- R (optional)
    - Windows: https://cran.r-project.org/bin/windows/base/
    - Ubuntu: ```sudo apt install r-base``` or https://cran.r-project.org/
    
### install
install Python and JS dependencies:
```
pip install -r requirements.txt
cd webapp
yarn install
yarn build
```

### Demos
#### 1: Web App:
Start web app
- ```python run.py```
- open the webpage at localhost:5000/

#### 2: CLI demos:
see ```python cli.py --help``` for info about CLI tool

benchmark: ```python cli.py benchmark <DATA_SET> <ALGORITHM>```
e.g. ```python cli.py benchmark GOWALLA col_pbs``` results are stored in ```GOWALLA/``` (each line is in the format ```[cost] [time]```)
see ```python cli.py benchmark --help``` for more info

profile memory usage: ```python cli.py profile <FIRST_ALGORITHM> <SECOND_ALGORITHM>```
e.g. ```python cli.py profile ban col_pbs```
see ```python cli.py profile --help``` for more info

#### 4: Run Cypress end-to-end tests
additional installation:
```
cd integration_tests
yarn install
```

Open Cypress:
```
cd integration_tests
./node_modules/.bin/cypress open --env type=actual
```