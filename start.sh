yarn --cwd webapp build
cd src/server || exit
gunicorn app:app