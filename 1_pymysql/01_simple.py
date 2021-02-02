import pymysql


if __name__ == '__main__':
    with pymysql.connect(host='127.0.0.1', user='test', password='test', port=3306, db='test_db', charset="utf8",
                         cursorclass=pymysql.cursors.DictCursor) as conn:
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
