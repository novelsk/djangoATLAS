mkdir -p ~/.postgresql
wget "https://storage.yandexcloud.net/cloud-certs/CA.pem" -O ~/.postgresql/root.crt
chmod 0600 ~/.postgresql/root.crt

conn = psycopg2.connect("""
    host=rc1b-1ryws53zj55l1crz.mdb.yandexcloud.net
    port=6432
    dbname=db1
    user=user1
    password=<password>
    target_session_attrs=read-write
    sslmode=verify-full
""")
