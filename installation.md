1. Clone the project
```sh
git clone https://github.com/SariyaP/ku-polls
```
2. Change to project directory
```sh
cd ku-polls
```
3. Install the requirements.txt
```sh
pip install -r requirements.txt
```
4. Migrate
```sh
python manage.py migrate
```
5. Load data
```sh
python manage.py loaddata data/users.json
python manage.py loaddata data/polls-v3.json
```
6. Run the server
```sh
python manage.py runserver
```
