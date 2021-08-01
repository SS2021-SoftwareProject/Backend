python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=api
export FLASK_ENV=development
apt install mariadb-server
apt-get install libmariadb-dev
apt-get install libmariadb3