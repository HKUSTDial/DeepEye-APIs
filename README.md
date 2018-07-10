DeepEye - APIs
===========================
This repository share the APIs of the DeepEye's visualization recommendation module. A live demo of DeepEye: http://deepeye.tech

Description
===========================
### Visualization Ranking: 
the task is, given two visualization nodes, to decide which one is better. Hence we need to rank multiple visualization nodes. We support three ranking approaches:
1. **Learning-to-rank**: We use the LambdaMART algorithm. [More Details](http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/icde18-deepeye.pdf)
2. **Parial Order-based approach**: the basic idea is that we define some partial orders which are used to decide which visualization node is better. Then we build a graph based on the partial orders, where each vertex is a visualization node and the directed edge between two nodes is decided by the partial order. At last, we can use the graph to compute a score for each visualization node based on topology sorting, i.e., the smaller the topology order is, the larger the score is. [More Details](http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/icde18-deepeye.pdf)
3. **Diversified Ranking**: We aim to select diversified top-k visualization nodes since there may be many similar visualizations showing redundant information. For example, v1 > v2 and v2 > v3 do not necessarily mean that v1 + v2 > v1 + v3, since v1 and v2 might be very “similar". Our basic idea is to construct a graph in which nodes are visualizations, and weight of the edge between two nodes denotes the distance between them. Then we use the graph, our defined relevance and diversity measurement to calculate diversified top-k visualizations.

Usage
===========================
### 1. Dependence 
- [x] Python 2.7
- [x] MySQL 5.7
- [x] [MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html#installation)

### 2. Input

### 3. Output

### 4. Example 
Publications
===========================
- Yuyu Luo, Xueqi Qin, Nan Tang, Guoliang Li. [DeepEye: Towards Automatic Data Visualization](http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/icde18-deepeye.pdf). **ICDE 2018**
- Yuyu Luo, Xuedi Qin, Nan Tang Guoliang Li, Xinran Wang. [DeepEye: Creating Good Data Visualizations by Keyword Search](http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/sigmod18-deepeye.pdf). **SIGMOD 2018 Demo**

Contributors
===========================
|#|Contributor|Affiliation|Contact|
|---|----|-----|-----|
|1|[Guoliang Li](http://dbgroup.cs.tsinghua.edu.cn/ligl/)|Professor, Tsinghua University| LastName+FirstName@tsinghua.edu.cn
|2|[Nan Tang](http://da.qcri.org/ntang/index.html)|Senior Scientist, Qatar Computing Research Institute|ntang@hbku.edu.qa
|3|Xuedi Qin| PhD Candidate, Tsinghua University| qxd17@mails.tsinghua.edu.cn
|4|Yuyu Luo| M.S. student, Tsinghua University| luoyuyu@tsinghua.edu.cn
##### ++If you have any questions about it, please feel free to contact Yuyu Luo (luoyuyu@tsinghua.edu).cn++
