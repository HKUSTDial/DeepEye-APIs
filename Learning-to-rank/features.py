class Type(object):
    none=0
    categorical=1
    numerical=2
    temporal=3

    @staticmethod
    def getType(s):
        if len(s)>=7 and s[0:7]=='varchar':
            return Type.categorical
        if len(s)>=4 and s[0:4]=='char':
            return Type.categorical
        if len(s)>=3 and s[0:3]=='int':
            return Type.numerical
        if s=='int' or s=='double' or s=='float':
            return Type.numerical
        if s=='date' or s=='datetime':
            return Type.temporal


class Features(object):
    def __init__(self,name,type,origin):
        self.name=name
        self.type=type
        self.origin=origin
        self.min=self.minmin=self.max=self.distinct=self.ratio=self.bin_num=0
        self.interval=''
        self.distinct_values=[]
        self.interval_bins=[]










