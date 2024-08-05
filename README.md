# FastAPI-JWT-Sample

FastAPIによるJWTの実装

# セットアップ

```bash
pip install -r requirements.txt
```

# FastAPI実行

```bash
uvicorn main:app --reload
```

# 認証のテスト

## 新しいユーザーを作成する

```bash
curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{"username": "testuser", "email": "test@example.com", "password": "testpassword"}'
```

## JWT トークンを取得

```bash
curl -X POST "http://127.0.0.1:8000/token" -d "username=testuser&password=testpassword"
```

## エンドポイントにアクセス

上記で取得したJWTトークンを利用する。

```bash
curl -X GET "http://127.0.0.1:8000/users/me/" -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 参考

- https://dev.to/rishisharma/building-jwt-auth-chaining-with-fastapi-and-python-11hn
- https://fastapi.tiangolo.com/ja/tutorial/security/oauth2-jwt/
