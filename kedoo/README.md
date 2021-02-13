# Micro-authorization and registration

## Running server

```bash
$ python3 manage.py runserver
```

## Registration

```bash
curl -X POST http://127.0.0.1:8000/api/reg -d "username=test&password=1234.s"
```

## Login

```bash
curl -X POST -d "username=test&password=1234.s" http://127.0.0.1:8000/api/login
```

The response to this request will be the user's Token.

## Status

```bash
curl -X GET -I -H "Authorization: Token 1bf8cfbfc1b3ba5f9fafeba4def5331cbf8bb39f" http://127.0.0.1:8000/api/status
```

- If the user is logged in, the HTTP status code 200 will be received.
- If the user with this token is not logged in, the HTTP 401 status code will be received.

## Logout

```bash
curl -X GET -H "Authorization: Token 1bf8cfbfc1b3ba5f9fafeba4def5331cbf8bb39f" http://127.0.0.1:8000/api/logout
```
