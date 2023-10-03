## Run

First Install Python3

and then create virtual env

type this command to run:

```Shell
python3 -m venv env
```

```Shell
source env/bin/activate
```

Install requirement.txt

```Shell
pip3 install -r requirement.txt
```

Set database in folder origin/settings.py

And run this command for makemigrations
```Shell
./manage.py makemigrations
./manage.py migrate
```

## API Documentation POSTMAN

There is postman file in folder postman
```
