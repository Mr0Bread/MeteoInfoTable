from Application import *


def main():
    class Main(Application):
        def __init__(self):
            self.connect_to_database()

        def connect_to_database(self):
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         port=3306,
                                         password='mr0bread',
                                         db='MeteoInfoTable',
                                         cursorclass=pymysql.cursors.DictCursor)

            try:
                with connection.cursor() as cursor:
                    sqlQuery = "INSERT INTO meteoinfotable( 'Stacija', " \
                               "'Laiks', " \
                               "'Gaisa temperatūra', " \
                               "'Gaisa temperatūras tendence (-1 h)'," \
                               "'Gaisa mitrums'," \
                               "'Rasas punkts'," \
                               "'Nokrišņi'," \
                               "'Intensitāte mm/h'," \
                               "'Redzamība'," \
                               "'Ceļa temperatūra 1'," \
                               "'Ceļa temperatūra 1 tendence (-1h)'," \
                               "'Ceļa stāvoklis 1'," \
                               "'Ceļa brīdinājums 1'," \
                               "'Sasalšanas punkts 1'," \
                               "'Ceļa temperatūra 2'," \
                               "'Ceļa temperatūra 2 tendence (-1h)'," \
                               "'Ceļa stāvoklis 2'," \
                               "'Ceļa brīdinājums 2'," \
                               "'Sasalšanas punkts 2') VALUES (%s, %s, %s, %s, %s, %s, %s, %s, " \
                               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sqlQuery, ('1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2',
                                              '2', '2', '2', '2', '2', '2', '2', '2'))
                    connection.commit()
            finally:
                connection.close()


if __name__ == '__main__':
    main()
