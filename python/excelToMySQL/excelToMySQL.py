#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：将Excel数据导入到MySQL数据库,excel表中需要需要包含字段名
"""
import xlrd
import MySQLdb

# 读取EXCEL中内容到数据库中
wb = xlrd.open_workbook('test.xlsx')
sh = wb.sheet_by_index(0)
nrows = sh.nrows  # 行数
ncols = sh.ncols  # 列数
data = []  #数据表中数据
field = []  #数据表中字段名
field.append(sh.row_values(0))
for i in range(1, nrows):
      data.append(sh.row_values(i))
conn = MySQLdb.connect(host='localhost', user='root', passwd='zhouzhou', db = "scheduling",charset='utf8')
cursor = conn.cursor()
# 创建table
cursor.execute("create table if not exists test(" + field[0][0] + " varchar(100));")
for i in range(1,ncols):
    cursor.execute("alter table test add " + field[0][i] + " varchar(100);")
val = ''
for i in range(0, ncols):
      val = val + '%s,'
cursor.executemany("insert into test values(" + val[:-1] + ");", data)
cursor.close()
conn.commit()
conn.close()



# """
# 功能：将Excel数据导入到MySQL数据库,
# 前期工作：1、建立相应的数据表，这里用orders来表示
#           2、更改xlsx的名字以及sheet名字
#           3、更改数据库相关密码等
#           4、更改插入SQL插入语句
#           5、更改for循环，与表对应
# """
# import xlrd
# import MySQLdb
# # Open the workbook and define the worksheet
# book = xlrd.open_workbook("test.xlsx")
# sheet = book.sheet_by_name("test")
# 
# #建立一个MySQL连接
# database = MySQLdb.connect(host="localhost", user = "root", passwd = "zhouzhou", db = "scheduling",charset='utf8')
# 
# # 获得游标对象, 用于逐行遍历数据库数据
# cursor = database.cursor()
# 
# # 创建插入SQL语句
# query = """INSERT INTO orders (product, rep) VALUES (%s, %s)"""
# 
# # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
# for r in range(1, sheet.nrows):   #注意：如果excel表中完全是数据部分，则从改为range(0,sheet.nrows)
#       product      = sheet.cell(r,0).value
#       rep          = sheet.cell(r,1).value
#       values = (product,  rep)
#       # 执行sql语句
#       cursor.execute(query, values)
# # 关闭游标
# cursor.close()
# # 提交
# database.commit()
# # 关闭数据库连接
# database.close()



# # """
# # 功能：将MySQL数据导出到Excel
# # """
# import xlwt
# import MySQLdb
# conn=MySQLdb.connect(host="localhost", user = "root", passwd = "zhouzhou", db = "scheduling",charset='utf8')
# cursor=conn.cursor()
# count = cursor.execute('select * from orders')  #表的名字需要更改
# print 'has %s record' % count
# #重置游标位置
# cursor.scroll(0,mode='absolute')
# #搜取所有结果
# results = cursor.fetchall()
# #测试代码，print results
# #获取MYSQL里的数据字段
# fields = cursor.description
# #将字段写入到EXCEL新表的第一行
# wbk = xlwt.Workbook()
# sheet = wbk.add_sheet('test',cell_overwrite_ok=True)
# for ifs in range(0,len(fields)):
#     sheet.write(0,ifs,fields[ifs][0])
# ics=1
# jcs=0
# for ics in range(1,len(results)+1):
#     for jcs in range(0,len(fields)):
#         sheet.write(ics,jcs,results[ics-1][jcs])
# wbk.save('test.xlsx')
