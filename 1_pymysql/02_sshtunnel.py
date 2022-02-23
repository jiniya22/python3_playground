import pymysql
from sshtunnel import SSHTunnelForwarder


if __name__ == '__main__':
    with SSHTunnelForwarder('apple', remote_bind_address=('127.0.0.1', 3306)) as tunnel:
        with pymysql.connect(host='127.0.0.1', user='test2', password='test2', port=tunnel.local_bind_port,
                             db='test_db', charset="utf8", cursorclass=pymysql.cursors.DictCursor) as conn:
            with conn.cursor() as cur:
                sql = '''
                SELECT * from users
                '''
                cur.execute(sql)
                print(sql)
                results = cur.fetchall()
                for result in results:
                    print(result)
    print('\nfinish!\n', '-----' * 20)
