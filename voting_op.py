from Db_cred import *
import mysql.connector
from mysql.connector import Error


import os
import json

class voting_op:
    def __init__(self):
         pass 


#----------------Candidate Unapproved List(Applications)
    def c_get_unapp_data(self,c_id):
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
                    sql1="select c_id,status,v_id,email,ct_id,p_id from candidates where c_id=%s"
                    val1=(c_id,)
                    cur1.execute(sql1,val1)
                    res1=cur1.fetchall()
                    print(res1)

                    ct_id=res1[0].get('ct_id')
                    p_id=res1[0].get('p_id')
                    v_id=res1[0].get('v_id')

                    run=voting_op()
                    res2=run.c_ret_P_C_names(ct_id,p_id,v_id)
                   
            
                    result =res1 +res2 
                    
                    dict_c={}
                    for m in result:
                        dict_c.update(m)
                   
                    run2=voting_op()
                    run2.c_add_unapp_data(c_id,dict_c)

                    return True

            
         except Error as e:
            print(f"something went wrong\n{e}") 

    
    #-----------Add to unaprroved List--------

    def c_add_unapp_data(self,c_id,c_data):     
        run=voting_op()
        unapp_list=run.c_rj_unapp_data() # dict import 
        unapp_list[str(c_id)]=c_data
        try:
            with open("unapproved-list.json","w") as a: 
              json.dump(unapp_list,a,indent=4)
              return True
            
        except Exception as e:
            print(f"Something went wrong at writing file \n {e}")
        
    #--return all dict file data-------------
    
    def c_rj_unapp_data(self):
        file="unapproved-list.json"
        try:
            if not os.path.exists(file) or os.path.getsize(file)==0:
             with open(file,"w") as w:
                 json.dump({},w)

            with open(file,"r") as read:
                 res=json.load(read)
                 return res
             
        except Exception as e:
            print(f"Something Went wrong at file reading\n{e}")
        
 #----return const and party and voters(tables) names------------{Redundant due to circular import issues}
    def c_ret_P_C_names(self,ct_id,p_id,v_id):
        host1=DB_cred.host
        user1=DB_cred.user
        password1=DB_cred.password
        database1=DB_cred.database

        with mysql.connector.connect(
                host=host1,
                user=user1,
                password=password1,
                database=database1
            ) as my_db10:
                with my_db10.cursor(dictionary=True) as cur10:
                    sql1="select p_name from party where p_id=%s"
                    val1=(p_id,)

                    sql2="select ct_name from constituency where ct_id=%s"
                    val2=(ct_id,)

                    sql3="select f_name,l_name,mob,city,age from voters where v_id=%s"
                    val3=(v_id,)



                    cur10.execute(sql1,val1)
                    res1=cur10.fetchall()

                    cur10.execute(sql2,val2)
                    res2=cur10.fetchall()

                    cur10.execute(sql3,val3)
                    res3=cur10.fetchall()

                    
                    result= res1 + res2 + res3
                    print(result)

                    return result
    
    



#-----------------------Testings-----------------------------
run7=voting_op()
#run7.c_get_unapp_data(3473)
#run7.c_add_unapp_data(293,{1323:"valer1",2:"valr2",3:"valf3"})
#run7.c_rj_unapp_data()
