source ~/.venv/bin/activate
cd /home/GeorgesTaconet/JupyterBook
jupyter-book clean -y
jupyter-book build
jupyter-book start --execute

git push -u origin main

https://chantaltaconet.github.io/GeorgesTaconet/