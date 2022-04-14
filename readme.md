Команды для получение сертификата, для подключения к бд
mkdir -p ~/.postgresql
wget "https://storage.yandexcloud.net/cloud-certs/CA.pem" -O ~/.postgresql/root.crt
chmod 0600 ~/.postgresql/root.crt

Настройки для подключения к бд
conn = psycopg2.connect("""
    host=rc1b-1ryws53zj55l1crz.mdb.yandexcloud.net
    port=6432
    dbname=db1
    user=user1
    password=zxcv1234
    target_session_attrs=read-write
    sslmode=verify-full
""")

superuser (Login: admin, pas: admin)
users (Login: user2, pas: django12)

Задание
1. На чистом сервере развернуть Django
2. Установите Postgres sql и создайте 2 разных таблицы Ai1, Ai2 формата (id (int, pk), current (real), sts (int) )
3. Выберите любой понравившийся шаблон на бутстрапе и разверните на нем страницу авторизации и контента 
    с динамическим обновлением графика (id, current) и таблицей (id, current, sts (== 1), кнопка изменения sts с 1 на 2 для данной записи)
4. Настройки Crud на 2 пользователя с авторизацией
5. При авторизации пользователь №1 должен видеть график и таблицу с данными из Ai1, для второго юзера соответственно Ai2 
    (допускается разнести доныне на разные страницы и предоставлять доступ в соответствии с ролью авторизации т.е. url1 для user1 и url2 для user2)
6. Пользователь №2 не должен получать возможность видеть данные пользователя №1
