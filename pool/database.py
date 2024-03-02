import psycopg2

class DB:
    def __init__(self, database, user, password):
        self.conn = psycopg2.connect(
        database=database,
        user=user,
        password=password,
    )
        self.cur = self.conn.cursor()

    def execute_query(self, query, params):
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur
    
    def add_user(self, name, password, share_password):
        # 비밀번호를 해시화하여 저장
        self.execute_query("INSERT INTO users (name, password, share_password) VALUES (%s, %s, %s);", (name, password, share_password))

    def get_user(self, name, password):
        user_data = self.execute_query("SELECT name FROM users WHERE name = %s AND password = %s;", (name, password))
        if user_data.rowcount == 0:  # 사용자 정보가 없는 경우
            return None
        else:
            return user_data.fetchone()  # 사용자 정보가 있는 경우, 사용자 정보 반환

    




    # def select_user(self, userID):
    #     return self.execute_query("SELECT * FROM users WHERE user_id = %s;", (userID,)).fetchone()

    # def select_user_password(self, userID, password):
    #     return self.execute_query("SELECT * FROM users WHERE user_id = %s AND user_pw = %s;", (userID, password)).fetchone()

    # def insert_user(self, userID, password):
    #     self.execute_query("INSERT INTO users VALUES (%s, %s);", (userID, password))

    # def delete_user(self, userID):
    #     self.execute_query("DELETE FROM users WHERE user_id = %s;", (userID,))

    # def chat(self, userID, input_text, output):
    #     self.execute_query("INSERT INTO chat_log (user_id, question, answer) VALUES (%s ,%s, %s)",(userID,input_text,output))

    # def select_log(self, userID):
    #     return self.execute_query("SELECT * FROM Chat_Log WHERE user_id = %s ORDER BY timestamp ASC;",(userID,)).fetchall()