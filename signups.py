from Db_cred import *
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date

class signups:
    def __init__(self):
        pass
#----------------Voter sign-up------------------------------

    def v_sign(self,f_name,l_name,dob,mob,email,v_password,city,age):
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
            ) as my_db:
                with my_db.cursor() as cur:
                    sql="insert into voters (f_name,l_name,dob,mob,email,password,city,age) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    val=(f_name,l_name,dob,mob,email,v_password,city,age)

                    cur.execute(sql,val)
                    my_db.commit()

                    print("Sucessefully executed :)")

        except Error as e:
            print(f"something went wrong {e} ")

    #------------Admin sign-up------------------------------------------------------
    def a_sign(self,f_name,l_name,email,password,mob,dob,age):
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
                    sql2="insert into admins (f_name,l_name,email,password,mob,dob,age) values (%s,%s,%s,%s,%s,%s,%s)"
                    val2=(f_name,l_name,email,password,mob,dob,age)

                    cur2.execute(sql2,val2)
                    my_db2.commit()

                    print("sucessfully executed")

        except Error as f:
            print(f"something went wrong\n{f}")

    #--------------------AGE calculator----------------------------

    def age_calc(self,age1):

        age_f=datetime.strptime(age1,"%Y-%m-%d").date()
        today=date.today()
        
        age_res=today.year-age_f.year-((today.month,today.day)<(age_f.month,age_f.day))
        

        print(age_res)
        return age_res

#----------------------------------------------------------------------------------------------
run=signups()
#run.v_sign("fn","ln","07-12-1998",8765365438,"atari@gmail.com","a12345","bangalore")
#run.a_sign("afn","aln","admin@gmail.com","s12345",8764356423)
run.age_calc("2001-11-07")