from view import Chart

class myGraph(object):
    def __init__(self,node_num):
        self.node_num=0
        self.nodes=[]
        self.G=[[float('inf') for i in range(node_num)] for j in range(node_num)]
        self.dis=self.G[:]
        self.sim=[[0 for i in range(node_num)] for j in range(node_num)]

    def getCost(self,node1,node2):
        #markEditOps   ->   p5 (change chart type) and p4 (different aggregation)
        if node1.table.describe==node2.table.describe and node1.x_name==node2.x_name:
            if node1.y_name==node2.y_name and node1.chart==node2.chart:
                return 0.02
            elif node1.y_name==node2.y_name:
                if node1.chart==Chart.pie and node2.chart==Chart.bar:
                    return 0.03
                if node1.chart==Chart.pie and node2.chart==Chart.line:
                    return 0.02
                if node1.chart==Chart.pie and node2.chart==Chart.scatter:
                    return 0.04
                if node1.chart==Chart.bar and node2.chart==Chart.line:
                    return 0.04
                if node1.chart==Chart.bar and node2.chart==Chart.scatter:
                    return 0.02
                if node1.chart==Chart.line and node2.chart==Chart.scatter:
                    return 0.03
            elif node1.chart==node2.chart:
                if node1.y_name[0:3]=='CNT' or node2.y_name[0:3]=='CNT':
                    return 0.02
                t1,t2=node1.y_name,node2.y_name
                if node1.y_name[0:3]=='SUM' or node1.y_name[0:3]=='AVG':
                    t1=t1[4:-1]
                if node2.y_name[0:3]=='SUM' or node2.y_name[0:3]=='AVG':
                    t2=t2[4:-1]
                if t1==t2:
                    return 0.01
        #transformEditOps  ->    p3 (BIN)
        elif node1.table.describe=='' and node2.table.describe[0:3]=='BIN' and node1.x_name==node2.x_name[0:len(node1.x_name)] and node1.y_name==node2.y_name[4:-1] and node1.chart==node2.chart:
            return 0.62
        elif node2.table.describe=='' and node1.table.describe[0:3]=='BIN' and node2.x_name==node1.x_name[0:len(node2.x_name)] and node2.y_name==node1.y_name[4:-1] and node1.chart==node2.chart:
            return 0.62
        #encodingEditOps   ->   p1 (change x) and p2 (change y)
        elif node1.table.describe==node2.table.describe and node1.y_name==node2.y_name and node1.chart==node2.chart:   #change x
            return 4.45
        elif node1.table.describe==node2.table.describe and node1.x_name==node2.x_name and node1.chart==node2.chart:   #change y
            return 4.45
        elif node1.table.describe2==node2.table.describe and node1.table.describe1[0:5]=='GROUP' and node1.x_name==node2.x_name and node1.chart==node2.chart:  #add z
            t1, t2 = node1.y_name, node2.y_name
            if node1.y_name[0:3] == 'SUM' or node1.y_name[0:3] == 'AVG':
                t1 = t1[4:-1]
            if node2.y_name[0:3] == 'SUM' or node2.y_name[0:3] == 'AVG':
                t2 = t2[4:-1]
            if t1 == t2:
                return 4.22
        elif node2.table.describe2==node1.table.describe and node2.table.describe1[0:5]=='GROUP' and node1.x_name==node2.x_name and node1.chart==node2.chart:   #add z
            t1, t2 = node1.y_name, node2.y_name
            if node1.y_name[0:3] == 'SUM' or node1.y_name[0:3] == 'AVG':
                t1 = t1[4:-1]
            if node2.y_name[0:3] == 'SUM' or node2.y_name[0:3] == 'AVG':
                t2 = t2[4:-1]
            if t1 == t2:
                return 4.22
        return float('inf')


    def addNode(self,node):
        self.nodes.append(node)
        for i in range(self.node_num):
            self.G[i][self.node_num] = self.G[self.node_num][i] = self.dis[i][self.node_num]=self.dis[self.node_num][i]=self.getCost(self.nodes[i], node)
        self.node_num+=1

    def getSim(self):
        # get dis by floyd
        for k in range(self.node_num):
            for i in range(self.node_num):
                for j in range(self.node_num):
                    if self.dis[i][j]>self.dis[i][k]+self.dis[k][j]:
                        self.dis[i][j]=self.dis[i][k]+self.dis[k][j]

        #get sim
        for i in range(self.node_num):
            for j in range(self.node_num):
                self.sim[i][j]=1.0/self.dis[i][j]


    def getTopK(self,K):
        score=0
        result=[]
        for k in range(K):
            max_id=-1
            max_delta_score=float('-inf')
            for i in range(self.node_num):
                if i in result:
                    continue
                delta_score=self.nodes[i].score
                for j in result:
                    delta_score-=0.5*(self.sim[i][j]*(self.nodes[i].score+self.nodes[j].score))
                if delta_score>max_delta_score:
                    max_delta_score=delta_score
                    max_id=i
            score=score+max_delta_score
            result.append(max_id)
        return result


# class view(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#
#
# G=myGraph()
# G.addNode(view('a',1))
# G.addNode(view('b',2))
# G.addNode(view('c',3))
# G.addNode(view('d',4))
# G.addNode(view('e',5))
# G.addNode(view('f',6))
# G.addNode(view('g',7))
# G.getSim()
# print G.getTopK(4)


