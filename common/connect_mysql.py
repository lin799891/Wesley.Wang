import pymysql


dbinfo = {
    "host":"",
    "user":"",
    "password":"",
    "port":
}
class DbConnect():
    def __init__(self,db_cof,database=""):
        self.db_cof = db_cof
        #打开数据库连接
        self.db = pymysql.connect(
            database=database,
            cursorclass = pymysql.cursors.DictCursor,
            **db_cof
        )
        #使用cursor（）方法获取操作游标
        self.cursor = self.db.cursor()


    def select(self,sql):
        self.cursor.excute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self,sql):
        #sql 删除、提交、修改语句
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            #发生错误回滚
            self.db.rollback()

    def close(self):
        self.db.close()

def select_sql(select_sql):
    #查询数据库
    db = DbConnect(dbinfo,database="fsbox_test")
    result = db.select(select_sql)#查询
    db.close()
    return result

def execute_sql(inser_sql):
    #执行sql
    db = DbConnect(dbinfo,database="fsbox_test")
    db.execute(inser_sql)
    db.close()


if __name__ == '__main__':
    sql_obj = DbConnect(dbinfo,database="fsbox_test")
