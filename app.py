from flask import *
import os

app =  Flask(__name__)

login_status = False


def get_filename(file_dir):
    dir = None
    for files in os.listdir(file_dir):
        dir = files
    return dir


def get_file_status(msg):
    if msg is None:
        return False
    else:
        return True


file_dir1 = "static/download/7"
file_dir2 = "static/download/8"
file_dir3 = "static/download/9"
msg1 = get_filename(file_dir1)
msg1_status = get_file_status(msg1)
msg2 = get_filename(file_dir2)
msg2_status = get_file_status(msg2)
msg3 = get_filename(file_dir3)
msg3_status = get_file_status(msg3)

def get_none_to_no(msg,status):
    if msg == None or status == False:
        return "无"
    else:
        return msg


@app.route('/')
def index():
    m1 = get_none_to_no(msg1,msg1_status)
    m2 = get_none_to_no(msg2,msg2_status)
    m3 = get_none_to_no(msg3,msg3_status)
    return render_template('index.html',msg1 = m1, msg2 = m2, msg3 = m3)

@app.route('/admin',methods=['POST','GET'])
def admin_login():
    if request.method=='GET':
        return  render_template('admin_login.html')
    user=request.form.get('usr')
    pwd=request.form.get('pwd')
    if user=='admin' and pwd=='123':
        global login_status
        login_status = True
        m1 = get_none_to_no(msg1,msg1_status)
        m2 = get_none_to_no(msg2,msg2_status)
        m3 = get_none_to_no(msg3,msg3_status)
        return render_template("admin.html",msg1 = m1, msg2 = m2, msg3 = m3)
    else:
        return  render_template('admin_login.html',msg='用户名或密码输入错误')    
@app.route('/admin_login_sucess')
def admin_login_sucess():
    if login_status == True:
        m1 = get_none_to_no(msg1,msg1_status)
        m2 = get_none_to_no(msg2,msg2_status)
        m3 = get_none_to_no(msg3,msg3_status)
        return render_template("admin.html",msg1 = m1, msg2 = m2, msg3 = m3)
    if login_status == False:
        return "<script>alert('未登录');window.open('/admin','_self');</script>"
@app.route('/admin_logout')
def admin_loginout():
    global login_status
    login_status = False
    return "<script>alert('已退出！');window.open('/','_self');</script>"



@app.route('/download/7')
def download7():
    file_path = f"static/download/7/{msg1}"
    if msg1_status == False: 
        if login_status == False:   
            return "<script>alert('无文件');window.open('/','_self');</script>"
        return "<script>alert('无文件');window.open('/admin_login_sucess','_self');</script>"
    else:
        return send_file(file_path,as_attachment=True)
@app.route('/download/7/delete')
def download7_delete():
    global msg1_status
    file_path = f"static/download/7/{msg1}"
    if msg1_status == False:    
        return "<script>alert('无文件');window.open('/admin_login_sucess','_self');</script>"
    os.remove(file_path)
    msg1_status = False
    return "<script>alert('删除成功！');window.open('/admin_login_sucess','_self');</script>"
@app.route('/download/7/upload',methods = ['POST'])
def download7_upload():
    global msg1_status,msg1
    if msg1_status == True:
        return "<script>alert('已存在文件！如需上传新文件，请删除旧文件！');window.open('/admin_login_sucess','_self');</script>"
    file = request.files['input_file']
    if file:
        file.save( file_dir1+'/'+file.filename)
        msg1_status = True
        msg1 = file.filename
        return "<script>alert('上传成功！');window.open('/admin_login_sucess','_self');</script>"
    else:
        return "<script>alert('上传失败！未选择文件！');window.open('/admin_login_sucess','_self');</script>"



@app.route('/download/8')
def download8():
    file_path = f"static/download/8/{msg2}"
    if msg2_status == False: 
        if login_status == False:   
            return "<script>alert('无文件');window.open('/','_self');</script>"
        return "<script>alert('无文件');window.open('/admin_login_sucess','_self');</script>"
    else:
        return send_file(file_path,as_attachment=True)


@app.route('/download/8/delete')
def download8_delete():
    global msg2_status
    file_path = f"static/download/8/{msg2}"
    if msg2_status == False:    
        return "<script>alert('无文件');window.open('/admin_login_sucess','_self');</script>"
    os.remove(file_path)
    msg2_status = False
    return "<script>alert('删除成功！');window.open('/admin_login_sucess','_self');</script>"
@app.route('/download/8/upload',methods = ['POST'])
def download8_upload():
    global msg2_status,msg2
    if msg2_status == True:
        return "<script>alert('已存在文件！如需上传新文件，请删除旧文件！');window.open('/admin_login_sucess','_self');</script>"
    file = request.files['input_file2']
    if file:
        file.save( file_dir2+'/'+file.filename)
        msg2_status = True
        msg2 = file.filename
        return "<script>alert('上传成功！');window.open('/admin_login_sucess','_self');</script>"
    else:
        return "<script>alert('上传失败！未选择文件！');window.open('/admin_login_sucess','_self');</script>"




@app.route('/download/9')
def download9():
    file_path = f"static/download/9/{msg3}"
    if msg3_status == False: 
        if login_status == False:   
            return "<script>alert('无文件');window.open('/','_self');</script>"
        return "<script>alert('无文件');window.open('/admin_login_sucess','_self');</script>"
    else:
        return send_file(file_path,as_attachment=True)
@app.route('/download/9/delete')
def download9_delete():
    global msg3_status
    file_path = f"static/download/9/{msg3}"
    if msg3_status == False:    
        return "<script>alert('无文件');window.open('/admin_login_sucess','_self');</script>"
    os.remove(file_path)
    msg3_status = False
    return "<script>alert('删除成功！');window.open('/admin_login_sucess','_self');</script>"
@app.route('/download/9/upload',methods = ['POST'])
def download9_upload():
    global msg3_status,msg3
    if msg3_status == True:
        return "<script>alert('已存在文件！如需上传新文件，请删除旧文件！');window.open('/admin_login_sucess','_self');</script>"
    file = request.files['input_file3']
    if file:
        file.save( file_dir3+'/'+file.filename)
        msg3_status = True
        msg3 = file.filename
        return "<script>alert('上传成功！');window.open('/admin_login_sucess','_self');</script>"
    else:
        return "<script>alert('上传失败！未选择文件！');window.open('/admin_login_sucess','_self');</script>"

@app.route('*')
def test():
    return 0

if __name__ == "__main__":
    app.run(debug=True)