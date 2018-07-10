import math
import numpy as np
np.seterr(divide='ignore',invalid='ignore')
from numpy import corrcoef
from features import Type


class Chart(object):
    bar=0
    line=1
    scatter=2
    pie=3
    chart=['bar','line','scatter','pie']


class View(object):
    def __init__(self,table,x_id,y_id,z_id,series_num,X,Y,chart):
        self.table=table
        self.fx=table.features[x_id]
        self.fy=table.features[y_id]
        self.x_name=self.fx.name
        self.y_name=self.fy.name
        self.z_id=z_id
        self.series_num=series_num
        self.X=X
        self.Y=Y
        self.chart=chart
        self.tuple_num=table.tuple_num
        self.M=self.Q=self.W=self.score=0
        self.getM()
        self.getQ()

    def getCorrelation(self,series_id):
        if self.fx.type==Type.temporal:
            data1=[i for i in range(self.tuple_num/self.series_num)]
        else:
            data1=self.X[series_id]
        data2=self.Y[series_id]
        log_data1=log_data2=[]
        if self.fx.type!=Type.temporal and self.fx.min>0:
            log_data1=map(math.log,data1)
        if self.fy.minmin>0:
            log_data2=map(math.log,data2)
        
        # linear
        try:
            result = abs(corrcoef(data1, data2)[0][1])
        except Exception as e:
            print "linear"
            result = 0;
        else:
            pass
        

        # exponential
        if log_data2:
            try:
                r = abs(corrcoef(data1, log_data2)[0][1])
                if r > result:
                    result = r
            except Exception as e:
                print "exponential"
                result = 0;
            else:
                pass
            

        # logarithm
        if log_data1:
            try:
                r = abs(corrcoef(log_data1, data2)[0][1])
                if r > result:
                    result = r
            except Exception as e:
                print "logarithm"
                result = 0;
            else:
                pass
            

        # power
        if log_data1 and log_data2:
            try:
                r = abs(corrcoef(log_data1, log_data2)[0][1])
                if r > result:
                    result = r
            except Exception as e:
                print "power"
                result = 0;
            else:
                pass

        return result

    def getM(self):
        if self.chart==Chart.pie:
            if self.tuple_num==1:
                self.M=0
            elif 2<=self.tuple_num<=10:
                sumY=sum(self.Y[0])
                self.M=reduce(lambda x,y:x+y,map(lambda y:-(1.0*y/sumY)*math.log(1.0*y/sumY),self.Y[0]))
            elif self.tuple_num>10:
                sumY=sum(self.Y[0])
                self.M=reduce(lambda x,y:x+y,map(lambda y:-(1.0*y/sumY)*math.log(1.0*y/sumY),self.Y[0]))*10.0/self.tuple_num
        elif self.chart==Chart.bar:
            if self.tuple_num==1:
                self.M=0
            elif 2<=self.tuple_num<=20:
                self.M=(max(self.Y[0])-min(self.Y[0]))/(sum(self.Y[0])/float(self.tuple_num/self.series_num))
            else:
                self.M=10.0/self.tuple_num*((max(self.Y[0])-min(self.Y[0]))/(sum(self.Y[0])/float(self.tuple_num/self.series_num)))
        elif self.chart==Chart.scatter:
            if self.series_num==1:
                self.M=self.getCorrelation(0)
            else:
                self.M=max([self.getCorrelation(i) for i in range(self.series_num)])
        else:
            if self.series_num==1:
                if self.getCorrelation(0)>0.3:
                    self.M=1
                else:
                    self.M=0
            else:
                if max([self.getCorrelation(i) for i in range(self.series_num)])>0.3:
                    self.M=1
                else:
                    self.M=0

    def getQ(self):
        self.Q=1
        if self.chart==Chart.bar or self.chart==Chart.pie:
            self.Q=1-1.0*(self.tuple_num/self.series_num)/self.table.instance.tuple_num

    def output(self,order):
        classify = str([])
        if self.series_num > 1:
            classify = str([v[0] for v in self.table.classes]).replace("u'", '\'').decode("unicode-escape").replace("'",'"')
        x_data = str(self.X)
        if self.fx.type == Type.numerical:
            x_data = str(self.X).replace("'", '"').replace('L', '')
        elif self.fx.type == Type.categorical:
            x_data = str(self.X).replace("u'", '\'').decode("unicode-escape").replace("'", '"')
        else:
            len_x = len(self.X)
            x_data = '[' + reduce(lambda s1, s2: s1 + s2, [str(map(str, self.X[i])) for i in range(len_x)]).replace("'",'"') + ']'
        y_data = str(self.Y)
        if self.fy.type == Type.numerical:
            y_data = y_data.replace('L', '')
        data ='{"order1":' + str(order) + ',"order2":' + str(1) +  ',"describe":"' + self.table.describe + '","x_name":"' + self.fx.name + '","y_name":"' + self.fy.name + '","chart":"' + Chart.chart[self.chart] + '","classify":' + classify + ',"x_data":' + x_data + ',"y_data":' + y_data + '}'
        #data = 'score:' + str(round(self.score, 2)) + '\tM:' + str(round(self.M, 2)) + '\tQ:' + str(round(self.Q, 2)) + '\tW:' + str(round(self.W, 2)) + '{"order":' + str(order) + ',"describe":"' + self.table.describe + '","x_name":"' + self.fx.name + '","y_name":"' + self.fy.name + '","chart":"' + Chart.chart[self.chart] + '","classify":' + classify + ',"x_data":' + x_data + ',"y_data":' + y_data + '}'
        print data





