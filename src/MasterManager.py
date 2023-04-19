import sqlite3

from PlanManager import *
from TodoManager import *
from JournalManager import *
from TipsManager import *
from TargetManager import *

class MasterManager():
    @staticmethod
    def createSetupDB():
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''CREATE TABLE IF NOT EXISTS user (
            id VARCHAR(15) NOT NULL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            uncompleted_todos INTEGER NOT NULL,
            unreached_targets INTEGER NOT NULL,
            reached_targets INTEGER NOT NULL,
            journals INTEGER NOT NULL);'''
        conn.execute(q1)
        conn.commit()
        conn.close()

        TipsManager.createQuotesDB()
        TipsManager.insertAllQuotesDB()

        JournalManager.createJournalDB()
        
        PlanManager.createPlanDB()

        TodoManager.createTodoDB()

        TargetManager.createTargetDB()




    @staticmethod
    def checkDB():
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT name FROM sqlite_master WHERE type='table' AND name='user';'''
        q2 = '''SELECT * FROM user;'''
        cursor = conn.execute(q1)
        if cursor.fetchone() == None:
            conn.close()
            return False
        else:
            cursor = conn.execute(q2)
            if cursor.fetchone() == None:
                conn.close()
                return False
            else:
                conn.close()
                return True 