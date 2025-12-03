
from Db_cred import *
import mysql.connector
from mysql.connector import Error
from voting_op import *


class cand_op:
    def __init__(self):
        pass 
    
    #----------Return party list----------
    def ret_p_list(self):
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
                    sql="select * from party"
                    cur1.execute(sql)
                    result=cur1.fetchall()
                    print(result)
                    return result

        except Error as e:
            print(f"something went wrong..\n{e}")

    #--------------Add party---------------------
   
    def add_p_list(self,p_name):
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
                with my_db2.cursor() as cur2:
                    sql="insert into party (p_name) values(%s)"
                    val=(p_name,)
                    cur2.execute(sql,val)
                    my_db2.commit()
                    a="party registered Successfully"

                    return a
        except Error as e:
            print(f"something went wrong..\n{e}")

    #--------------------Delete party-------------
    def del_p_list(self,p_id):
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
            ) as my_db3:
                with my_db3.cursor() as cur3:
                    sql="delete from party where p_id=%s "
                    val=(p_id,)
                    cur3.execute(sql,val)
                    my_db3.commit()
                    a="party deleted Successfully"
                    return a
        except Error as e:
            print(f"something went wrong..\n{e}")

 

    #----------Return constituency list----------
    def ret_ct_list(self):
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
            ) as my_db4:
                with my_db4.cursor(dictionary=True) as cur4:
                    sql="select * from constituency"
                    cur4.execute(sql)
                    result=cur4.fetchall()
                    print(result)
                    return result

        except Error as e:
            print(f"something went wrong..\n{e}")

    #--------------Add constituency---------------------
   
    def add_ct_list(self,ct_name):
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
            ) as my_db5:
                with my_db5.cursor() as cur5:
                    sql="insert into constituency (ct_name) values(%s)"
                    val=(ct_name,)
                    cur5.execute(sql,val)
                    my_db5.commit()
                    a="constituency registered Successfully"
                    return a
        except Error as e:
            print(f"something went wrong..\n{e}")

    #--------------------Delete constituency-------------
    def del_ct_list(self,ct_id):
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
            ) as my_db3:
                with my_db3.cursor() as cur3:
                    sql="delete from constituency where ct_id=%s "
                    val=(ct_id,)
                    cur3.execute(sql,val)
                    my_db3.commit()
                    a="party deleted Successfully"
                    return a
        except Error as e:
            print(f"something went wrong..\n{e}")


    #-------------candidate registration-------------
    
        #------verify voters-------
    def c_verify_vID(self,v_id):
        host1=DB_cred.host
        user1=DB_cred.user
        password1=DB_cred.password
        database1=DB_cred.database

        with mysql.connector.connect(
                host=host1,
                user=user1,
                password=password1,
                database=database1
            ) as my_db7:
                with my_db7.cursor() as cur7:
                    sql="select * from voters where v_id=%s"
                    val=(v_id,)
                    cur7.execute(sql,val)
                    result=cur7.fetchall()

                    if result is None:
                        res=False
                        return res
                    
                    else:
                        return result


  #----return const and party and voters(tables) names----------------
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

         
    def c_registration(self,v_id,p_id,ct_id,email,password):
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
            ) as my_db6:
                with my_db6.cursor(dictionary=True) as cur6:
                    ver=cand_op().c_verify_vID(v_id)
                    if ver == False:
                        a="No voter ID Exist !"
                        return a
                    else:
                        sql="insert into candidates (v_id,p_id,ct_id,email,password,status) values(%s,%s,%s,%s,%s,%s)"
                        status=0
                        val=(v_id,p_id,ct_id,email,password,status)
                        cur6.execute(sql,val)
                        my_db6.commit()
                        #-----------------------
                        
                        sql2="select c_id from candidates where v_id=%s and email=%s and password=%s"
                        val2=(v_id,email,password)

                        cur6.execute(sql2,val2)
                        u_add=cur6.fetchall()

                        c_id=u_add[0].get('c_id')
                        print(c_id)
                        run3=voting_op()
                        run3.c_get_unapp_data(c_id)
                       #-------------------------

                        a="Application submitted sucessfully"
                        return a
                
  
        except Error as e:
            print(f"something went wrong..\n{e}")
    

    #-----------------------Candidate login-----------------------

    def c_login(self,c_id,email,a_password):
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
            ) as m_db11:
                with m_db11.cursor(dictionary=True) as cur11:
                    sql="select * from candidates where c_id=%s and email=%s and password=%s"
                    val=(c_id,email,a_password)

                    cur11.execute(sql,val)
                    result=cur11.fetchall()

                    
                    if result is None:
                        print("Failed to login")
                        return False
                    
                    else:
                        print("logged in sucessfully\n")
                        #print(f"sucessfully fetched\n{result} ")
                        #print(result)

                        p_id=result[0].get('p_id')
                        ct_id=result[0].get('ct_id')
                        v_id=result[0].get('v_id')
                        c_stat=result[0].get('status') # for checking status
                        stat=run.c_status(c_stat)
                       
                        f_res=run.c_ret_P_C_names(ct_id,p_id,v_id)
                        result2= result + f_res
                        
                        result3={}
                        for m in result2:
                            result3.update(m)
                        
                        result_f=[]
                        result_f.append(result3)
                       
                        return result_f,stat

        except Error as e:
            print(f"something went wrong\n{e}") 

 #---------Get Candidate ID--------------

    def get_CID(self,v_id,email,passwd):
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

                    sql="select c_id from candidates where email=%s and password=%s"
                    val=(email,passwd,)
                    cur1.execute(sql,val)
                    result1=cur1.fetchall()

                    sql="select f_name,l_name from voters where v_id=%s"
                    val=(v_id,)
                    cur1.execute(sql,val)
                    result2=cur1.fetchall()

                    res=result1+result2
                    res_d={}
                    for m in res:
                        res_d.update(m)
                    
                    result_f=[]
                    result_f.append(res_d)

                    
                    return result_f 

         except Error as e:
              print(f"Something went wrong \n {e}")


    #-----------------------candidate status---------------
    def c_status(self,c_stat):
        if c_stat == 0:
            stat="Pending"
            return 0
        elif c_stat==1:
            stat="Approved"
            return 1
        elif c_stat==2:
             return 2
        else:
            return 35

#----------------------testing-------------
run=cand_op()
#run.add_ct_list("Kerebilachi")
#run.ret_p_list()
#run.c_registration(147651,65,7076,"can7Aamirshar@gmail.com","a12345")
#run.c_ret_P_C_names(7072,61)
#run.c_login(710,"candi3@gmail.com","a12345")
#run.get_CID(147651,"candi4@gmail.com","a12345")

