import sqlite3


# データベースの接続をする関数
def create_connect(db_file):
    connect = None
    try:
        connect = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connect


# テーブル作成関数
def create_table(con):
    create_tb = """
    CREATE TABLE IF NOT EXISTS ex_news_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        news_title TEXT NOT NULL,
        news_url TEXT
    )
    """
    try:
        cursor = con.cursor()
        cursor.excute(create_tb)
    except sqlite3.Error as e:
        print(e)


# ディクショナリをテーブルに挿入する関数
def insert_dict(con, data):
    sql = ''' INSERT INTO ex_news_list(news_title, news_url)
              VALUES(?,?) '''
    cursor = con.cursor()
    for key, value in data.items():
        cursor.execute(sql, (key, value))
    con.commit()


# テーブルからディクショナリを読み出す関数
def select_all(con):
    cursor = con.cursor()
    cursor.execute("SELECT news_title, news_url FROM ex_news_list")
    
    rows = cursor.fetchall()
    result = {}
    for row in rows:
        result[row[0]] = row[1]
    return result


