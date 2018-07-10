#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
from instance import Instance
from table import Table
from myGraph import myGraph
from features import Type

#read data from database => get argument from cmd
instance=Instance(sys.argv[1])
instance.addTable(Table(instance,False,'',''))
conn=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='Db10204!!',db='dataVisDB',charset='utf8')
cur=conn.cursor()
instance.column_num=instance.tables[0].column_num=(len(sys.argv)-3)/2
for i in range(0,instance.column_num):
    instance.tables[0].names.append(sys.argv[3+i])
    instance.tables[0].types.append(Type.getType(sys.argv[3+i+instance.column_num].lower()))
instance.tables[0].origins=[i for i in range(instance.tables[0].column_num)]
instance.tuple_num=instance.tables[0].tuple_num=cur.execute(sys.argv[2])
instance.tables[0].D=map(list,cur.fetchall())
cur.close()
conn.close()

#if table == none ===> exit
if len(instance.tables[0].D)==0:
    print '{}'
    sys.exit(0)
    
# read data from database => get table_name
# table_name='electricity'
# instance=Instance(table_name)
# instance.addTable(Table(instance,False,'',''))
# conn=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='dataVisDB',charset='utf8')
# cur=conn.cursor()
# instance.column_num=instance.tables[0].column_num=cur.execute('describe '+table_name)
# desc=cur.fetchall()
# for i in range(instance.column_num):
#     instance.tables[0].names.append(desc[i][0])
#     instance.tables[0].types.append(Type.getType(desc[i][1].lower()))
# instance.tables[0].origins=[i for i in range(instance.tables[0].column_num)]
# instance.tuple_num=instance.tables[0].tuple_num=cur.execute('select * from '+table_name)
# instance.tables[0].D=map(list,cur.fetchall())
# cur.close()
# conn.close()

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



# rder1=order2=1
# old_view=''
# for i in range(instance.view_num):
#     view=instance.tables[instance.views[i].table_pos].views[instance.views[i].view_pos]
#     classify=str([])
#     if view.series_num>1:
#         classify=str([v[0] for v in view.table.classes]).replace("u'",'\'').decode("unicode-escape").replace("'",'"')
#     x_data=str(view.X)
#     #print x_data
#     if view.fx.type==Type.numerical:
#         x_data=str(view.X).replace("'",'"').replace('L','')
#     elif view.fx.type==Type.categorical:
#         x_data=str(view.X).replace("u'",'\'').decode("unicode-escape").replace("'",'"')
#     else:
#         len_x=len(view.X)
#         x_data='['+reduce(lambda s1,s2:s1+s2,[str(map(str,view.X[i])) for i in range(len_x)]).replace("'",'"')+']'
#     y_data=str(view.Y)
#     if view.fy.type==Type.numerical:
#         y_data=y_data.replace('L','')
#     if old_view:
#         if view.table.describe==old_view.table.describe and view.fx.name==old_view.fx.name and view.fy.origin==old_view.fy.origin:
#             order2+=1
#         elif view.fx.origin==old_view.fx.origin and view.fy.origin==old_view.fy.origin and view.z_id==old_view.z_id and view.score==old_view.score:
#             order2+=1
#         elif view.table.describe==old_view.table.describe and view.fx.name==old_view.fx.name and view.fy.minmin*old_view.fy.minmin>=0:
#             order2+=1
#         elif view.z_id==old_view.z_id and view.table.describe[-7:]=='BY ZERO' and old_view.table.describe[-7:]=='BY ZERO':
#             order2+=1
#         else:
#             order1+=1
#             order2=1
#     data='score:'+str(round(view.score,2))+'\tM:'+str(round(view.M,2))+'\tQ:'+str(round(view.Q,2))+'\tW:'+str(round(view.W,2))+'{"order1":'+str(order1)+',"order2":'+str(order2)+',"describe":"'+view.table.describe+'","x_name":"'+view.fx.name+'","y_name":"'+view.fy.name+'","chart":"'+Chart.chart[view.chart]+'","classify":'+classify+',"x_data":'+x_data+',"y_data":'+y_data+'}'
#     print data
#     old_view=view


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



