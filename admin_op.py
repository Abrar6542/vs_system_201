import mysql.connector
from mysql.connector import Error
from  Db_cred import *
from candidate import *

class admin_op:
    def __init__(self):
        pass 

#---------List all voters--------------
    def a_All_voters(self):
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
                    sql="select * from voters"
                    cur1.execute(sql)
                    result=cur1.fetchall()
                    print(result)
                    return result

        except Error as e:
            print(f"something went wrong..\n{e}")

#---------List All Admins----------------------------------
    def a_All_Admins(self):
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
                    sql="select * from admins"
                    cur1.execute(sql)
                    result=cur1.fetchall()
                    print(result)
                    return result

        except Error as e:
            print(f"something went wrong..\n{e}")

#-----------------------Announcments-------------------------

    def ann_add(self,info):
        with open("Anc.txt","w") as wr:
            wr.write(info)
            return True
        
    def ann_read(self):
        with open("Anc.txt","r") as r:
            res=r.read()
            return res
        
#-----------------List All Candidates--------------------------

    def list_All_candid(self):
        try:
            run=voting_op()
            res1=run.c_rj_unapp_data()
            
            #-----All data--------
            res_list=[]
            for m in res1.values() :
                res_list.append(m)
            
            return res_list
                

        except Exception as e:
            print(f"something went wrong..\n{e}")

    
    #---------------Accept/reject candidates---------------------

    def a_ac_rej_cand_app(self,c_id,stat):
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
            ) as my_db2:
                with my_db2.cursor(dictionary=True) as cur2:
                    sql="update candidates set status=%s where c_id=%s"
                    val=(stat,c_id)
                    cur2.execute(sql,val)
                    my_db2.commit()
                    
            
            #-----------update for json--------------
            run=admin_op()
            run.a_c_unapp_update(c_id,stat)
            return True

        except Error as e:
            print(f"Something went wrong..\n{e}")

    #------------------Json updates-------------
    def a_c_unapp_update(self,c_id,stat):
        run=voting_op() 
        unapp_dict=run.c_rj_unapp_data()
        print(c_id)
        print(stat)
        
        
        unapp_dict[str(c_id)]['status']=stat 

        try:
            with open("unapproved-list.json","w") as write:
                json.dump(unapp_dict,write,indent=4)
                return True

        except Error as e:
            print(f"something went wrong..{e}")
        





#------------------------------------Testing------------------------------
run=admin_op()
#run.a_All_voters()
#run.a_All_Admins()
#run.list_All_candid()
#run.a_c_unapp_update(3477,1)
