from flask import Flask,render_template,request,redirect,url_for
from signups import *
from logins import *
from admin_op import *
from voter_op import *
from candidate import *


app = Flask(__name__ )

#--------------------start----------------------
@app.route('/')
def start():
    return render_template('main1.html')



#===========================================lOGINS AND REGISTRATIONS(voters & admins)==================================
#--------------voter registration---------------
@app.route('/ret_vRegForm')
def ret_vregForm():
    return render_template('v_reg-form.html')

@app.route('/v_registration',methods=['POST'])
def acc_vregForm():
    f_name1=request.form.get('fname').upper()
    l_name1=request.form.get('lname').upper()
    dob1=request.form.get('dob')
    mob1=request.form.get('mob')
    email1=request.form.get('email')
    pass1=request.form.get('password')
    city1=request.form.get('city').upper()

    run=signups()
    #-------age-----------------
    age1=run.age_calc(dob1)
    #---------------------------
   
    run.v_sign(f_name1,l_name1,dob1,mob1,email1,pass1,city1,age1)
    a=" Voter Registred Sucessfully.. Login with your voter ID here."
    return render_template('v_LoginForm.html',a=a)


#--------------Admin registration---------------
@app.route('/ret_aRegForm')
def ret_aregForm():
    return render_template('a_reg-form.html')

@app.route('/a_registration',methods=['POST'])
def acc_aregForm():
    f_name1=request.form.get('fname').upper()
    l_name1=request.form.get('lname').upper()
    dob1=request.form.get('dob')
    mob1=request.form.get('mob')
    email1=request.form.get('email')
    pass1=request.form.get('password')
    

    run=signups()
    age1=run.age_calc(dob1)
    run.a_sign(f_name1,l_name1,email1,pass1,mob1,dob1,age1)
    
    a="Admin registered sucessfully, Login here."
    return render_template('a_LoginForm.html',a=a)

#-----------------Voters Login--------------
@app.route('/v_LoginForm')
def ret_vLogin():
    return render_template('v_LoginForm.html')

@app.route('/acc_vlogins', methods=['POST'])
def acc_vLogin():
    v_id1=request.form.get('v_id')
    email1=request.form.get('email')
    pass1=request.form.get('password')

    run=logins()
    res=run.v_login(v_id1,email1,pass1)
    
    if not res:
        a="User in voter list NOT FOUND !"
        return render_template('errors.html')
    
    else:
        run1=admin_op()
        read=run1.ann_read()
        return render_template('v_HomePage.html', res=res,read=read)


#-----------------Admin Login--------------
@app.route('/a_LoginForm')
def ret_aLogin():
    return render_template('a_LoginForm.html')

@app.route('/acc_alogins', methods=['POST'])
def acc_aLogin():
    a_id1=request.form.get('a_id')
    email1=request.form.get('email')
    pass1=request.form.get('password')

    run=logins()
    res=run.a_login(a_id1,email1,pass1)
    
    print(res)
    if not res:
       
        return render_template('errors.html')
    
    else:
        run1=admin_op()
        read=run1.ann_read()
        return render_template('a_HomePage.html', res=res,read=read)

#========================================--ADMINS ACTIVITY--============================================

#-------------------List all voters------------------
@app.route('/ret_voter_list')
def a_ret_voters():

    run=admin_op()
    res=run.a_All_voters()
    return render_template('a_all-VList.html',res=res)

#-------------------List all Admins------------------
@app.route('/ret_admin_list')
def a_ret_admins():

    run=admin_op()
    res=run.a_All_Admins()
    return render_template('a_all-AList.html',res=res)

#-------------------Announcments----------------------

@app.route('/a_anc_add_form')
def a_add_announce_form():
    
    return render_template('a_anc_add-form.html')

@app.route('/a_anc_add',methods=['POST'])
def a_add_announce():
    info1=request.form.get('info')
    run=admin_op()
    run.ann_add(info1)
    a="Information Added sucesfully"
    return redirect(url_for('a_add_announce_form',value=a))

#---------------Approve candidates------------
@app.route('/c_Approve_candid',methods=['POST'])
def a_approve_candid():
    c_id=request.form.get('c_id')
    stat=1
    run=admin_op()
    run.a_ac_rej_cand_app(c_id,stat)
    return redirect('/c_All_candid')

#---------------Reject candidates------------
@app.route('/c_Reject_candid',methods=['POST'])
def a_reject_candid():
    c_id=request.form.get('c_id')
    stat=2
    run=admin_op()
    run.a_ac_rej_cand_app(c_id,stat)
    return redirect('/c_All_candid')


#--------------List All candidates--------------------
@app.route('/c_All_candid')
def list_All_candid():
    run=admin_op()
    res=run.list_All_candid()
    stat="Not yet"
    return render_template('c_all-CList.html',res=res,stat=stat)

#=======================================--VOTERS ACTIVITY--=============================================

#---------------------Know Voter ID--------------------------
@app.route('/v_getVIDForm')
def v_getVID_form():
    return render_template('v_get-VID_form.html')


@app.route('/v_vID', methods=['POST'])
def v_getVID():
    email1=request.form.get('email')
    passwd1=request.form.get('password')
    dob1=request.form.get('dob')
    mob1=request.form.get('mob')
    
    run=voter_op()
    res=run.get_VID(email1,passwd1,mob1,dob1)

    if not res:
        res1=False
        a="No Voter ID Exist..!"
        return render_template('v_get-VID_form.html',a=a)
    
    else:
        return render_template('v_get-VID.html',res=res)
    

    #-----------------Get voting candidates list(pooling day)-----------------
@app.route('/get_poll_candid')
def v_List_All_votig_candid():
    run=voter_op()
    res=run.v_get_voting_Candid_list()
    return render_template('v_all-Voting_List.html',res=res)


#=======================================--CANDIDATE ACTIVITY--===========================================
#----------------party-------------------------
@app.route('/c_party_acc')
def c_ret_partyList():
    run=cand_op()
    res=run.ret_p_list()
    return render_template('c_party.html',res=res)

@app.route('/c_party_add',methods=['POST'])
def c_add_partyList():
    p_name=request.form.get('p_name').upper()
    run=cand_op()
    a=run.add_p_list(p_name)
    return redirect('/c_party_acc')

@app.route('/c_party_delete',methods=['POST'])
def c_del_partyList():
    p_id=request.form.get('p_id')
    a=cand_op().del_p_list(p_id)
    
    return redirect('/c_party_acc')

#-----------------------Constituency---------------------
@app.route('/c_constituency_acc')
def c_ret_constituencyList():
    run=cand_op()
    res=run.ret_ct_list()
    return render_template('c_constituency.html',res=res)

@app.route('/c_constituency_add',methods=['POST'])
def c_add_constituencyList():
    ct_name=request.form.get('ct_name').upper()
    run=cand_op()
    a=run.add_ct_list(ct_name)
    return redirect('/c_constituency_acc')

@app.route('/c_constituency_delete',methods=['POST'])
def c_del_constituencyList():
    ct_id=request.form.get('ct_id')
    a=cand_op().del_ct_list(ct_id)
    
    return redirect('/c_constituency_acc')

#------------------------Candidate Registration----------------------

@app.route('/c_regist_form')
def c_regist_form():
    run=cand_op()
    ct_res=run.ret_ct_list()
    p_res=run.ret_p_list()
    return render_template('c_reg-form.html',ct_res=ct_res,p_res=p_res)

@app.route('/c_registration',methods=['POST'])
def c_registration():
    v_id=request.form.get('v_id')
    p_id=request.form.get('p_id')
    ct_id=request.form.get('ct_id')
    email=request.form.get('email')
    password=request.form.get('password')

    run=cand_op()
    a=run.c_registration(v_id,p_id,ct_id,email,password)
    return render_template('c_LoginForm.html',a=a)


#---------------Candidate Login----------------------------

@app.route('/c_LoginForm')
def ret_cLogin():
    return render_template('c_LoginForm.html')

@app.route('/candi_clogins', methods=['POST'])
def acc_cLogin():
    c_id1=request.form.get('c_id')
    email1=request.form.get('email')
    pass1=request.form.get('password')

    run=cand_op()
    res,stat=run.c_login(c_id1,email1,pass1)
    
    print(res)
    if not res:
       
        return render_template('errors.html')
    
    else:
        run1=admin_op() 
        read=run1.ann_read()
        return render_template('c_HomePage.html', res=res,stat=stat)
    
    #---------------------Know Candidate ID--------------------------
@app.route('/c_getCIDForm')
def c_getCID_form():
    return render_template('c_get-CID_form.html')


@app.route('/c_cID', methods=['POST'])
def c_getCID():
    email1=request.form.get('email')
    passwd1=request.form.get('password')
    v_id=request.form.get('v_id')
    
    
    run=cand_op()
    res=run.get_CID(v_id,email1,passwd1)
    

    if not res:
        res=False
        a="No Voter ID Exist..!"
        return render_template('c_get-CID_form.html',a=a)
    
    else:
        return render_template('c_get-CID.html',res=res)

    









#==========================================END===========================================================

if __name__=='__main__':
    app.run()