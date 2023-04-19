import sqlite3

class JournalManager():
    @staticmethod
    def createJournalDB():
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''CREATE TABLE IF NOT EXISTS journal (
            date DATETIME NOT NULL PRIMARY KEY,
            path VARCHAR(255) NOT NULL,
            mood INTEGER,
            rate INTEGER);'''
        conn.execute(q1)
        conn.commit()
        conn.close()

    @staticmethod
    def getJournal(dates):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT * FROM journal WHERE date=?'''
        cursor = conn.execute(q1, (dates,))
        return cursor.fetchone()
    
    @staticmethod
    def createJournal(dates):
        conn = sqlite3.connect('src/database/dailify.db')
        filename="journal-{}.txt".format(dates)
        path = "src/database/JournalTXT/{}".format(filename)
        q1 = "INSERT INTO journal VALUES (?, ?, 0, 0);"
        conn.execute(q1, (dates, path))
        conn.commit()
        conn.close()
        file = open(path, "w")
        file.close()

    @staticmethod
    def saveRate(date, rate):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = "UPDATE journal SET rate=? WHERE date=?"
        values = (rate, date)
        conn.execute(q1, values)
        conn.commit()
        conn.close()
    
    @staticmethod
    def saveMood(date, mood):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = "UPDATE journal SET mood=? WHERE date=?"
        values = (mood, date)
        conn.execute(q1, values)
        conn.commit()
        conn.close()
    
    @staticmethod
    def getPath(date):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT path FROM journal WHERE date=?'''
        cursor = conn.execute(q1, (date,))
        return cursor.fetchone()[0]
    
    @staticmethod
    def getRate(date):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT rate FROM journal WHERE date=?'''
        cursor = conn.execute(q1, (date,))
        return cursor.fetchone()[0]
    
    @staticmethod
    def getMood(date):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT mood FROM journal WHERE date=?'''
        cursor = conn.execute(q1, (date,))
        return cursor.fetchone()[0]
        
    @staticmethod
    def checkJournal(date):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT * FROM journal WHERE date=?'''
        cursor = conn.execute(q1, (date,))
        if cursor.fetchone() == None:
            return False
        else:
            return True
        
    @staticmethod
    def countJournal():
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT path FROM journal WHERE rate != 0 or mood != 0;'''
        cursor = conn.execute(q1)
        return len(cursor.fetchall())
        