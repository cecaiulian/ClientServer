# ClientServer
Client-Server communication for test


Git Token:

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

------------------------------------------------------------------------

sudo apt update
sudo apt install python3-kivy

python3 -m pip install --upgrade pip setuptools virtualenv

------------------------------------------------------------------------

python3 -m venv kivy_venv

source kivy_venv/bin/activate

python3 -m pip install "kivy[base]" kivy_examples

mkdir kivy-deps-build && cd kivy-deps-build

curl https://raw.githubusercontent.com/kivy/kivy/master/tools/build_linux_dependencies.sh -o build_kivy_deps.sh

chmod +x build_kivy_deps.sh

./build_kivy_deps.sh

pip install kivy
