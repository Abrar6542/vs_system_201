from Db_cred import *
import mysql.connector
from mysql.connector import Error
class logins:
    def __init__(self):
        pass

    #--------------v_logins---------------
    def v_login(self,v_id,email,v_password):
        try:
            host1=DB_cred.host
            user1=DB_cred.user
            password1=DB_cred.password
            database1=DB_cred.database

            with mysql.connector.connect(
                host=host1,
                user=user1,
                password=password1,
                database=database1
            ) as m_db1:
                with m_db1.cursor(dictionary=True) as cur1:
                    sql="select * from voters where v_id=%s and email=%s and password=%s"
                    val=(v_id,email,v_password)

                    cur1.execute(sql,val)
                    result=cur1.fetchall()
                    
                    if result is None:
                        print("Failed to login")
                        return False
                    
                    else:
                        print("logged in sucessfully\n")
                        
                        print(f"sucessfully fetched\n{result}")
                        return result

        except Error as e:
            print(f"something went wrong\n{e}")   
    
    #-------------------admin login----------------------------

    def a_login(self,a_id,email,a_password):
        try:
            host1=DB_cred.host
            user1=DB_cred.user
            password1=DB_cred.password
            database1=DB_cred.database

            with mysql.connector.connect(
                host=host1,
                user=user1,
                password=password1,
                database=database1
            ) as m_db2:
                with m_db2.cursor(dictionary=True) as cur2:
                    sql="select * from admins where a_id=%s and email=%s and password=%s"
                    val=(a_id,email,a_password)

                    cur2.execute(sql,val)
                    result=cur2.fetchall()
                    
                    if result is None:
                        print("Failed to login")
                        return False
                    
                    else:
                        print("logged in sucessfully\n")
                        print(f"sucessfully fetched\n{result} ")
                    
                        return result

        except Error as e:
            print(f"something went wrong\n{e}")   
    
run=logins()
run.v_login(147640,"atari@gmail.com","a12345")
#run.a_login(141,"admin@gmail.com","s12345")