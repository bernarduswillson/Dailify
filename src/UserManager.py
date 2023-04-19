import sqlite3

class UserManager():
    @staticmethod
    def getUser():
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT * FROM user'''
        cursor = conn.execute(q1)
        return cursor.fetchone()
    
    @staticmethod
    def insertUser(name):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''INSERT INTO user VALUES ("0", '{}', 0, 0, 0, 0);'''.format(name)
        conn.execute(q1)
        conn.commit()
        conn.close()

    @staticmethod
    def updateUser(id, user):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = "UPDATE user SET username=?, uncompleted_todos=?, unreached_targets=?, reached_targets=?, journals=? WHERE id=?"
        values = (user.getName(), user.getUncompletedTodos(), user.getUnreachedTargets(), user.getReachedTargets(), user.getCreatedJournals(), id)
        conn.execute(q1, values)
        conn.commit()
        conn.close()