#!/usr/bin/env python3

sudo apt install git

git clone https://github.com/BidjorySamuel/MATK.git

pip install pyinstaller

# Navega até o diretório do seu aplicativo
cd MATK

cd guis
# Instala os requisitos usando o pip
pip install -r requirements.txt



pyinstaller --noconsole --onefile principal_root.py


