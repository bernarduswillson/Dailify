import sqlite3

class PlanManager:
    @staticmethod
    def createPlanDB():
        conn = sqlite3.connect('src/database/dailify.db')
        q = '''CREATE TABLE IF NOT EXISTS plan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATETIME DEFAULT CURRENT_TIMESTAMP);'''
        conn.execute(q)
        conn.commit()
        conn.close()

    @staticmethod
    def getPlan(date):
        conn = sqlite3.connect('src/database/dailify.db')
        q = '''SELECT * FROM plan WHERE date=?;'''
        cursor = conn.execute(q, (date,))
        if cursor.fetchone() == None:
            conn.close()
            return [-1]
        ret = cursor.fetchone()
        conn.close()
        return ret

    @staticmethod
    def getPlanId(date):
        conn = sqlite3.connect('src/database/dailify.db')
        q = '''SELECT id FROM plan WHERE date=?;'''
        cursor = conn.execute(q, (date,))
        ret = cursor.fetchone()
        conn.close()
        if ret == None:
            return None
        else:
            return ret[0]

    @staticmethod
    def checkPlan(date):
        conn = sqlite3.connect('src/database/dailify.db')
        q = '''SELECT * FROM plan WHERE date=?;'''
        cursor = conn.execute(q, (date,))
        if cursor.fetchone() == None:
            conn.close()
            return False
        conn.close()
        return True
    
    @staticmethod
    def createPlan(date):
        conn = sqlite3.connect('src/database/dailify.db')
        q = '''INSERT INTO plan (date) VALUES (?);'''
        conn.execute(q, (date,))
        conn.commit()
        conn.close()