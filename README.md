1. Djangoなどの環境構築
```
pip install django
pip install djangorestframework
```
2. このリポジトリをclone
3. settings.pyのあるディレクトリで以下のコマンド
```
python generate_secretkey_setting.py > settings_local.py
```
4. ルートディレクトリで以下のコマンド
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
5. サーバーを起動
```
python manage.py runserver
```
- 管理画面(http://localhost:8000/admin)
- API(http://localhost:8000/api)
