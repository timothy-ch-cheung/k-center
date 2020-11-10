yarn --cwd webapp install
yarn --cwd webapp build
nohup python3 src/serverapp.py &