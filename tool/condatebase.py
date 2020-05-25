import pymysql

delete_condition='苗苗' # 删除的用户名
delete_table='user' # 删除数据所在的表格
delete_line='user_name' # 删除条件
update_table='user'  # 更新数据所在的表名
update_line='password' #需要更新的列
update_data='3333' #更新的内容
update_condition_line='user_name'  #更新的条件查询列
update_condition='苗苗' #查询的内容
conn=pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='myboke',
    charset='utf8'

)
# 获取游标
cur = conn.cursor()

# 删除数据
def delete_data(table,line,condition):
    sql="DELETE FROM %s WHERE %s ='%s' "
    data=(table,line,condition)
    cur.execute(sql % data)
    conn.commit()
    print(cur.rowcount)
# delete_data(delete_table,delete_line,delete_condition)

#修改数据，暂时只能修改一列内容
def update_data(table,update_line,update_data,condition_line,condition):
    sql="update %s set %s = '%s' where %s = '%s'"
    data=(table,update_line,update_data,condition_line,condition)
    lsql=sql % data
    cur.execute(sql % data)
    conn.commit()
    print(cur.rowcount)
# update_data(update_table,update_line,update_data,update_condition_line,update_condition)
# 查询数据
def select_data():
    select_list=[]
  sql="selent"