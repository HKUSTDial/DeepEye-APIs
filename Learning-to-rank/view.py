import math
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
        self.z_id=z_id
        self.series_num=series_num
        self.X=X
        self.Y=Y
        self.chart=chart
        self.tuple_num=table.tuple_num
        self.score=0

    def getCorrelation(self,series_id):
        if self.fx.type==Type.categorical:
            return 0
        if self.fx.type==Type.temporal:
            data1=[i for i in range(self.tuple_num/self.series_num)]
        else:
            data1=self.X[series_id]
        data2=self.Y[series_id]
        log_data1=log_data2=[]
        if self.fx.type!=Type.temporal and self.fx.min>0:
            log_data1=map(math.log,data1)
        if self.fy.min>0:
            log_data2=map(math.log,data2)
        # linear
        result = abs(corrcoef(data1, data2)[0][1])

        # exponential
        if log_data2:
            r = abs(corrcoef(data1, log_data2)[0][1])
            if r > result:
                result = r

        # logarithm
        if log_data1:
            r = abs(corrcoef(log_data1, data2)[0][1])
            if r > result:
                result = r

        # power
        if log_data1 and log_data2:
            r = abs(corrcoef(log_data1, log_data2)[0][1])
            if r > result:
                result = r

        return result


    def output(self):
        correlation = max([self.getCorrelation(i) for i in range(self.series_num)])
        if self.fx.type == Type.temporal:
            return '1 qid:1 1:' + str(self.fx.type) + ' 2:' + str(self.fy.type) + ' 3:' + str(
                self.tuple_num) + ' 4:' + str(self.tuple_num) + ' 5:0 6:' + str(self.fy.min) + ' 7:0 8:' + str(
                self.fy.max) + ' 9:' + str(self.fx.distinct) + ' 10:' + str(self.fy.distinct) + ' 11:' + str(
                self.fx.ratio) + ' 12:' + str(self.fy.ratio) + ' 13:' + str(correlation) + ' 14:' + str(self.chart)
        else:
            return '1 qid:1 1:' + str(self.fx.type) + ' 2:' + str(self.fy.type) + ' 3:' + str(
                self.tuple_num) + ' 4:' + str(self.tuple_num) + ' 5:' + str(self.fx.min) + ' 6:' + str(
                self.fy.min) + ' 7:' + str(self.fx.max) + ' 8:' + str(self.fy.max) + ' 9:' + str(
                self.fx.distinct) + ' 10:' + str(self.fy.distinct) + ' 11:' + str(self.fx.ratio) + ' 12:' + str(
                self.fy.ratio) + ' 13:' + str(correlation) + ' 14:' + str(self.chart)









