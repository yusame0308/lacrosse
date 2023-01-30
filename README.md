1. Djangoなどの環境構築
```
pip install django
pip install djangorestframework
pip install pillow
```
2. このリポジトリをclone
3. 以下のコマンドでSecret Keyを生成
```
make secretkey
```
4. ルートディレクトリで以下のコマンド
```
make migrate
make create-admin-user
```
5. サーバーを起動
```
make run
```
- 管理画面(http://localhost:8000/admin)
- API(http://localhost:8000/api)
