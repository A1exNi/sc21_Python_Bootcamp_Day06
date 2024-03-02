# Задание 1
Для проверки задания 1 выполните команды перечисленные ниже.
1. python3 -m venv venv_report
2. source venv_report/bin/activate
3. pip install protobuf
4. pip install grpcio-tools
5. pip install grpcio
6. python reporting_server.py
7. Во втором терминале source venv_report/bin/activate
8. Во втором терминале python ./reporting_client.py 17 45 40.0409 -29 00 28.118

# Задание 2
Для проверки задания 2 выполните команды перечисленные ниже.
1. pip install pydantic
2. Если сервер не запущен выполнить команду python reporting_server.py
3. Во втором терминале python ./reporting_client_v2.py 17 45 40.0409 -29 00 28.118

# Задание 3
Для проверки задания 2 выполните команды перечисленные ниже.
1. pip install SQLAlchemy
2. pip install alembic
3. alembic init alembic
4. pip install psycopg2
5. cd /opt/goinfre/username
6. eval "$(/opt/goinfre/username/homebrew/bin/brew shellenv)"
7. brew install postgresql
8. pg_ctl -D /opt/goinfre/username/homebrew/var/postgresql@14 start
9. createdb dbspaceships
10. open alembic.ini and change in 63 line username
11. alembic upgrade head
12. Если сервер не запущен выполнить команду python reporting_server.py
13. Во втором терминале python ./reporting_client_v3.py 17 45 40.0409 -29 00 28.118
14. python ./reporting_client_v3.py scan 17 45 40.0409 -29 00 28.118
15. python ./reporting_client_v3.py list_traitors