#coding=utf-8
import cx_Oracle
#获取数据库连接
connection=cx_Oracle.connect("sajet","123456","192.168.20.46/orcl")

cursor = connection.cursor()

#执行数据库语句
res = cursor.execute("select st.terminal_name as terminalName from sajet.sys_terminal st where st.process_id = 100739 and st.terminal_id=52203969 order by st.terminal_name")

print res.fetchone()