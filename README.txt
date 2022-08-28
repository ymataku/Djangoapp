## 環境構築
$ docker-compose up --build -d 
$ docker compose exec web bash
$ python manage.py migrate

## migrationsがうまくいかない場合
$ pyton manage.py makemigrations
$ pyton manage.py migrate
を行う
