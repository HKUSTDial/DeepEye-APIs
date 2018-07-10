#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
from instance import Instance
from table import Table
from myGraph import myGraph
from features import Type

#read data from database
dbArgs = sys.argv[1:6]
# print dbArgs
instance=Instance(sys.argv[6])
instance.addTable(Table(instance,False,'',''))
conn=MySQLdb.connect(host=dbArgs[0],port=int(dbArgs[1]),user=dbArgs[2],passwd=dbArgs[3],db=dbArgs[4],charset='utf8')
cur=conn.cursor()
instance.column_num=instance.tables[0].column_num=(len(sys.argv)-8)/2
for i in range(0,instance.column_num):
    instance.tables[0].names.append(sys.argv[8+i])
    instance.tables[0].types.append(Type.getType(sys.argv[8+i+instance.column_num].lower()))
instance.tables[0].origins=[i for i in range(instance.tables[0].column_num)]
instance.tuple_num=instance.tables[0].tuple_num=cur.execute(sys.argv[7])
instance.tables[0].D=map(list,cur.fetchall())
cur.close()
conn.close()

#if table == none ===> exit
if len(instance.tables[0].D)==0:
    print '{}'
    sys.exit(0)

#get all views and their score
instance.addTables(instance.tables[0].dealWithTable())
begin_id=1
while begin_id<instance.table_num:
    instance.tables[begin_id].dealWithTable()
    begin_id+=1
if instance.view_num==0:
    print '{}'
    sys.exit(0)
instance.getM()
instance.getW()
instance.getScore()


G=myGraph(instance.view_num)
for i in range(instance.view_num):
    view=instance.tables[instance.views[i].table_pos].views[instance.views[i].view_pos]
    G.addNode(view)
G.getSim()
result=G.getTopK(instance.view_num)
order=1
for item in result:
    G.nodes[item].output(order)
    order+=1



