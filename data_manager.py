import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DB = os.getenv("DB")





class Member_State:

    def __init__(self):
        self.con = sqlite3.connect(DB)
        self.cur = self.con.cursor()
        self.table = self.creat_table()


    def creat_table(self):

        self.cur.execute("CREATE TABLE IF NOT EXISTS member_state(member_id, name, missed, is_subscribed)")
        self.con.commit()
    
    def add_new_member(self,member_id,name):
        
        member_id = member_id
        name = name
        missed = 1
        is_subscribed = 0

        self.cur.execute("INSERT INTO member_state (member_id, name, missed, is_subscribed) VALUES (?, ?, ?, ?)",
        (member_id, name, missed, is_subscribed))
        self.con.commit()
        print("done")
    
    def check_member_id(self,member_id, name):
        """To check if the member is in the database"""
        res = self.cur.execute("SELECT member_id FROM member_state")
        self.con.commit()
        member_ids = []
        for id in res.fetchall():
            id[0]    
            member_ids.append(id[0])            
        if member_id not in set(member_ids) or member_ids == []:   
            self.add_new_member(member_id, name)  


    def update_member_missed(self,member_id,):
        """To update the member missed score"""
      
        self.cur.execute("""
        UPDATE member_state
        SET missed = ? 
        WHERE 
        user_id = ? AND chat_id = ?
        """, (0, member_id))
        self.con.commit()

    def weekly_missed_update(self):
        """To beggin a new week"""
        res = self.cur.execute("SELECT missed, user_id FROM member_state")
        r = res.fetchall()
        for user in range(len(r)):
            new_missed = r[user][0] + 1
            member_id = r[user][1]
            self.cur.execute("""
            UPDATE member_state
            SET missed = ? 
            WHERE 
            member_id = ?
            """, (new_missed,member_id))
            self.con.commit()
    
    def get_missed(self,member_id):
        """To get the member missed score"""
        missed = self.cur.execute("SELECT missed FROM user_state WHERE user_id = ? AND chat_id = ?", (member_id,))
        user_missed = missed.fetchone()[0]
        return user_missed