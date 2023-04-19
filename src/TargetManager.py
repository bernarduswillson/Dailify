import sqlite3

class TargetManager() :
    @staticmethod
    def createTargetDB() :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''CREATE TABLE IF NOT EXISTS target (
            target_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            target_name VARCHAR(255) NOT NULL, 
            target_year INTEGER, 
            target_status BOOLEAN DEFAULT 0)'''
        conn.execute(q1)
        conn.commit()
        conn.close()
    
    @staticmethod
    def insertTargetDB(target_name, target_year) :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''INSERT INTO target (target_name, target_year) VALUES (?, ?)'''
        conn.execute(q1, (target_name, target_year))
        conn.commit()
        conn.close()
    
    @staticmethod
    def getTargetDB() :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''SELECT * FROM target WHERE target_status = 0'''
        cursor = conn.execute(q1)
        result = cursor.fetchall()
        conn.close()
        return result
    
    @staticmethod
    def getReachedDB() :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''SELECT * FROM target WHERE target_status = 1'''
        cursor = conn.execute(q1)
        result = cursor.fetchall()
        conn.close()
        return result
    
    def updateTargetDB(target_id, target_name, target_year) :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''UPDATE target SET target_name = ?, target_year = ? WHERE target_id = ?'''
        conn.execute(q1, (target_name, target_year, target_id))
        conn.commit()
        conn.close()
    
    def deleteTargetDB(target_id) :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''DELETE FROM target WHERE target_id = ?'''
        conn.execute(q1, (target_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def reachedTargetDB(target_id) :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''UPDATE target SET target_status = 1 WHERE target_id = ?'''
        conn.execute(q1, (target_id,))
        conn.commit()
        conn.close()
    
    @staticmethod
    def unReachedTargetDB(target_id) :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''UPDATE target SET target_status = 0 WHERE target_id = ?'''
        conn.execute(q1, (target_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def getTargetCountDB() :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''SELECT COUNT(*) FROM target'''
        cursor = conn.execute(q1)
        result = cursor.fetchone()
        conn.close()
        return result[0]
    
    @staticmethod
    def getAllTargetDB() :
        conn = sqlite3.connect("src/database/dailify.db")
        q1 = '''SELECT * FROM target'''
        cursor = conn.execute(q1)
        result = cursor.fetchall()
        conn.close()
        return result