import pymysql

delete_condition = '北河'  # 删除的用户名
delete_table = 'user'  # 删除数据所在的表格
delete_line = 'user_name'  # 删除条件
update_table = 'user'  # 更新数据所在的表名
update_line = 'password'  # 需要更新的列
update_data = '3333'  # 更新的内容
update_condition_line = 'user_name'  # 更新的条件查询列
update_condition = '苗苗'  # 查询的内容
database_name = "myboke"  # 查询的数据库名
table_name = "user"  # 查询的表格名
select_table="user" # 查询表名
select_line="user_name" # 查询字段
select_condition="北河" # 查询内容
insert_table="user"  # 插入表名
insert_value=[24,'北河', '1211111', '95', '0', '13500000000', 'mtx_0@qq.com', '2019-09-17 17:46:49']# 需要插入的列表
conn = pymysql.Connect(
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
def delete_data(delete_table, delete_line, delete_condition):

    sql = "DELETE FROM %s WHERE %s ='%s' " % (delete_table, delete_line, delete_condition)
    print(sql)
    cur.execute(sql)
    conn.commit()
    print(cur.rowcount)
    if cur.rowcount > 0:
        return "删除成功"


# 修改数据，暂时只能修改一列内容
def update_data(table, update_line, update_data, condition_line, condition):
    sql = "update %s set %s = '%s' where %s = '%s'" % (table, update_line, update_data, condition_line, condition)
    print(sql)
    cur.execute(sql)
    conn.commit()
    print(cur.rowcount)
    if cur.rowcount>0:
        return "修改成功"

# 获取某个表格的所有字段名，返回一个列表
def table_line(table_name, database_name):
    sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s'and table_schema ='%s'"
    table_line = []
    data = (table_name, database_name)
    cur.execute(sql % data)
    conn.commit()
    cur_fetchall = cur.fetchall()  # 储存fetchall（）的返回结果
    for i in range(len(cur_fetchall)):
        table_line.append(cur_fetchall[i][0])
    return table_line

# 查询数据，返回字典类型 传入，数据库名,表名，字段名，条件
def select_data(database_name,select_table,select_line,select_condition):
    sql = "select * from %s where %s = '%s' "
    data=(select_table,select_line,select_condition)
    cur.execute(sql % data)
    conn.commit()
    cur_fetchall = cur.fetchall()  # 储存fetchall（）的返回结果
    lines=table_line(table_name, database_name) # 所有字段的列表
    select_data = dict() # 创建一个字典
    select_line=[] # 创建一个列表 储存查询结果
    for i in range(len(lines)):
        select_line.append(cur_fetchall[0][i])
        select_data[lines[i]] = select_line[i] # 往字典中添加元素
    return select_data

# 添加数据
def insert_data(database_name,insert_table,insert_value):
    # sql="insert into table_name () values ()"
    sql_line=[] # 需要添加的字段名，
    # 不添加id，使id 自增
    lines_name=table_line(insert_table, database_name)
    # for i in range(1,len(lines_name)):
    #     sql_line.append(lines_name[i])
    #
    # # line_name=tuple(sql_line).__str__()  # 获取表格的字段名，并将列表转化元组转化为为字符串
    line_value=tuple(insert_value).__str__() # 将传入的值列表转化为字符串
    sql="insert into %s  values %s" % (insert_table,line_value)
    cur.execute(sql)
    conn.commit()
    print(cur.rowcount)
# insert_data(database_name,insert_table,insert_value)

# 获取表格中id 的最大值，返回一个int 类型的数值
def maxid(table):
    sql="select max(id) from %s" % table
    cur.execute(sql)
    conn.commit()
    max=int(cur.fetchone()[0])
    return  max