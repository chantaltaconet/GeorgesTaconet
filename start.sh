source ~/.venv/bin/activate
cd /home/GeorgesTaconet/JupyterBook
jupyter-book clean -y
jupyter-book build
jupyter-book start --execute
