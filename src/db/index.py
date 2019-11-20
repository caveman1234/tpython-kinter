import pymysql
connection = pymysql.connect(host='120.27.209.87',
                             user='root',
                             password='Wjm123456',
                             db='DR',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM TE_PARA_TRANKEYWORDS_INFO"
        cursor.execute(sql)
        # result = cursor.fetchone()
        # result = cursor.fetchmany()
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()