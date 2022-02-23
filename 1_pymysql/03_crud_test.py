from contextlib import contextmanager
import pymysql


dict_datasource = {'host': '127.0.0.1', 'port': '3306', 'username': 'test', 'password': 'test', 'database': 'test_db'}


def test_select():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
            SELECT * from user
            '''
            cur.execute(sql)
            print(sql)
            results = cur.fetchall()
            for result in results:
                print(result)
    print('test_select end!\n', '-----' * 20)


def test_insert():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
            INSERT INTO user(name, birth_date, phone_number) VALUES ("test1", "840912", "01099995656"),
            ("test2", "980102", "01077776363")
            '''
            cur.execute(sql)
            print(sql)
        conn.commit()
    print('test_insert end!\n', '-----' * 20)


def test_update():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
            UPDATE user set active=0 WHERE name like "test%"
            '''
            cur.execute(sql)
            print(sql)
        conn.commit()
    print('test_update end!\n', '-----' * 20)


def test_delete():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
            DELETE FROM user WHERE name like 'test%'
            '''
            cur.execute(sql)
            print(sql)
        conn.commit()
    print('test_delete end!\n', '-----' * 20)


@contextmanager
def get_db_connection(port=dict_datasource['port']):
    conn = pymysql.connect(host=dict_datasource['host'], user=dict_datasource['username'], port=int(port),
                           password=dict_datasource['password'], db=dict_datasource['database'], charset="utf8",
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        yield conn
    finally:
        conn.close()


if __name__ == '__main__':
    test_select()

    test_insert()
    test_select()

    test_update()
    test_select()

    test_delete()
    test_select()
