[[ -z "$1" ]] && { echo "Release name is required" ; exit 1; }
RELEASE_FOLDER="colourful-k-center-$1"
echo "$RELEASE_FOLDER"
mkdir "$RELEASE_FOLDER"
mkdir "$RELEASE_FOLDER/webapp"
yarn --cwd webapp install
yarn --cwd webapp build
cp -r webapp/build "$RELEASE_FOLDER/webapp"
cp -r src "$RELEASE_FOLDER"
cp requirements.txt "$RELEASE_FOLDER"
cp run.py "$RELEASE_FOLDER"
cp README.md "$RELEASE_FOLDER"
echo "Release $1 created successfully"
