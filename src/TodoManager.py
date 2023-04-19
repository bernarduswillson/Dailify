import sqlite3

class TodoManager:
    @staticmethod
    def createTodoDB():
        conn = sqlite3.connect('src/database/dailify.db')
        q = '''CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_plan INTEGER NOT NULL,
            content VARCHAR(50) NOT NULL,
            time_start DATETIME,
            time_end DATETIME,
            checked INTEGER DEFAULT 0,
            FOREIGN KEY (id_plan) REFERENCES plan(id)
            );'''
        conn.execute(q)
        conn.commit()
        conn.close()
    
    def getPlanTodos(plan_id):
        conn = sqlite3.connect('src/database/dailify.db')
        q = '''SELECT * FROM todo WHERE id_plan = ?;'''
        cursor = conn.execute(q, (plan_id,))
        return cursor.fetchall()

    def createTodo(todo):
        conn = sqlite3.connect('src/database/dailify.db')
        q = '''INSERT INTO todo (id_plan, content, time_start, time_end, checked) VALUES (?, ?, ?, ?, ?);'''
        conn.execute(q, (todo.getPlanId(), todo.getContent(), todo.getStart(), todo.getEnd(), todo.getChecked(),))
        conn.commit()
        conn.close()
    
    # def deleteTodo(id):
    #     conn = sqlite3.connect('src/database/dailify.db')
    #     q = '''DELETE FROM todo WHERE id = ?;'''
    #     conn.execute(q, (id,))
    #     conn.commit()
    #     conn.close()