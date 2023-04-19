import sqlite3

class TipsManager():
    @staticmethod
    def createQuotesDB():
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            quote VARCHAR(255) NOT NULL);'''
        conn.execute(q1)
        conn.commit()
        conn.close()

    @staticmethod
    def insertQuotesDB(quote):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''INSERT INTO quotes (quote) VALUES ('%s');''' % (quote)
        conn.execute(q1)
        conn.commit()
        conn.close()

    @staticmethod
    def insertAllQuotesDB():
        TipsManager.insertQuotesDB('"If the plan does not work, change the plan but never the goal."')
        TipsManager.insertQuotesDB('"The best way to predict the future is to create it."')
        TipsManager.insertQuotesDB('"How you fall does not matter. It is how you land."')
        TipsManager.insertQuotesDB('"Accept everything just the way it is."')
        TipsManager.insertQuotesDB('"Failure is not a reason to give up as long as you believe in yourself."')
        TipsManager.insertQuotesDB('"Winners never quit, and quitters never win."')
        TipsManager.insertQuotesDB('"There is no failure except in no longer trying."')
        TipsManager.insertQuotesDB('"The only way to do great work is to love what you do."')
        TipsManager.insertQuotesDB('"Our greatest weakness lies in giving up."')
        TipsManager.insertQuotesDB('"Simplicity boils down to two steps : Identify the essential. Eliminate the rest."')
        TipsManager.insertQuotesDB('"You will never lose. Either you win or you learn."')
        TipsManager.insertQuotesDB('"It always seems impossible until it is done."')
        TipsManager.insertQuotesDB('"Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence."')
        TipsManager.insertQuotesDB('"Only I can change my life. No one can do it for me."')
        TipsManager.insertQuotesDB('"Tenderness and kindness are not signs of weakness and despair, but manifestations of strength and resolution."')
        TipsManager.insertQuotesDB('"It does not matter how slowly you go as long as you do not stop."')
        TipsManager.insertQuotesDB('"Successful men and women keep moving. They make mistakes, but they do not quit."')
        TipsManager.insertQuotesDB('"If we never try, we will never know."')
        TipsManager.insertQuotesDB('"Your biggest weakness is when you give up and your greatest power is when you try one more time."')
        TipsManager.insertQuotesDB('"Sometimes the smallest step in the right direction end up being the biggest step of your life for your success."')
        TipsManager.insertQuotesDB('"The future depends on what you do today."')
        TipsManager.insertQuotesDB('"You only live once, but if you do it right, once is enough."')
        TipsManager.insertQuotesDB('"It is never too late to be what you might have been."')
        TipsManager.insertQuotesDB('"No great achiever – even those who made it seem easy – ever succeeded without hard work."')
        TipsManager.insertQuotesDB('"You learn the value of hard work by working hard."')
        TipsManager.insertQuotesDB('"Patience can be bitter but her fruit is always sweet."')
        TipsManager.insertQuotesDB('"Goodness and hard work are rewarded with respect."')
        TipsManager.insertQuotesDB('"Every new day is another chance to change your life."')
        TipsManager.insertQuotesDB('"Life is like riding a bicycle. To keep your balance you must keep moving."')
        TipsManager.insertQuotesDB('"Everything I have ever let go of has claw marks on it."')
        TipsManager.insertQuotesDB('"If opportunity does not come to you, then create it."')
        TipsManager.insertQuotesDB('"Do your best at every opportunity that you have."')
        TipsManager.insertQuotesDB('"Work hard in silence, let your success be your noise."')
        TipsManager.insertQuotesDB('"Happiness is an inside job."')
        TipsManager.insertQuotesDB('"Good things come to those who work for it."')
        TipsManager.insertQuotesDB('"Do not give up because you had a bad day, forgive yourself and do better tomorrow."')
        TipsManager.insertQuotesDB('"Life does not get easier, you just get stronger."')
        TipsManager.insertQuotesDB('"Never stop learning because life never stops teaching."')
        TipsManager.insertQuotesDB('"Do not limit your challenges, challenge your limit."')
        TipsManager.insertQuotesDB('"Do not blame distractions, improve your focus."')
        TipsManager.insertQuotesDB('"Life is simple, but we insist on making it complicated."')
        TipsManager.insertQuotesDB('"Do something today that your future self will thank you for."')
        TipsManager.insertQuotesDB('"Do not practice until you get it right. Practice until you can not get it wrong."')
        TipsManager.insertQuotesDB('"The rewards for work well done is the opportunity to do more."')
        TipsManager.insertQuotesDB('"Nothing great was ever achieved without enthusiasm."')

    @staticmethod
    def getRandomQuote(prevID):
        conn = sqlite3.connect('src/database/dailify.db')
        q1 = '''SELECT * FROM quotes WHERE id != {} ORDER BY RANDOM() LIMIT 1;'''.format(prevID)
        cursor = conn.execute(q1)
        return cursor.fetchone()