import datetime
import time
from tool.condatebase import data_processing
createtime=time.strftime("%Y-%m-%d")+" "+time.strftime("%H:%M:%S")
# 接收register 页面提交的表单
class register_form():
    user_name=""
    password=""
    repassword=""
    email=""
    register_form={}
    register_list =[]
    #构造方法
    def __init__(self):pass
    # 获取表单数据并提交到数据库处理方法
    def RegisterData(self,register_form={}):
        user_name=self.user_name=register_form.get("user_name")
        password=self.password=register_form.get("password")
        # repassword=self.repassword=register_form.get("repassword")
        email=self.email=register_form.get("email")
        register_list=[user_name,password,email,createtime]
        sql_line=['user_name','password','email','create_time']
        register_data = data_processing()
        isSueccesd=register_data.insert_data("myboke", "user", sql_line,register_list)
        print(isSueccesd)
        return isSueccesd



