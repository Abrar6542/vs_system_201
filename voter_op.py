import mysql.connector
from mysql.connector import Error
from Db_cred import *
from voting_op import *

class voter_op:
    def __init__(self):
         pass 
    
    #---------Get Voter ID--------------

    def get_VID(self,email,passwd,mob,dob):
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
            ) as my_db1:
                with my_db1.cursor(dictionary=True) as cur1:
                    sql="select v_id,f_name,l_name from voters where email=%s and dob=%s and password=%s and mob=%s"
                    val=(email,dob,passwd,mob)
                    cur1.execute(sql,val)
                    result=cur1.fetchall()
                    print(result)
                    return result 

         except Error as e:
              print(f"Something went wrong \n {e}")

    #-------------Get Approved(voting) candidates list--------------

    def v_get_voting_Candid_list(self):
        try:
            run=voting_op()
            unapp_dict=run.c_rj_unapp_data()
            unapp_list_a=[]

            for m in unapp_dict.values():
                if m['status']==1:
                    unapp_list_a.append(m)
            
            return unapp_list_a

        except Exception as e :
            print(f"something went wrong..{e}")


#-----------------------------Testing------------------------------
run=voter_op()
#run.get_VID("atari2@gmail.com","s123456",4567894325,"2019-01-01")
run.v_get_voting_Candid_list()